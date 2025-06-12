from google.adk.agents import BaseAgent, LlmAgent, ParallelAgent, LoopAgent, SequentialAgent
from google.adk.agents.invocation_context import InvocationContext
from typing import AsyncGenerator
from google.adk.events import Event
from typing_extensions import override
import json
from google.genai import types
import logging
from .sub_agents import chore_collector_agent, process_sequencer_agent

logger = logging.getLogger(__name__)

class ChoreOrganizerAgent(BaseAgent):
    """
    A sophisticated custom agent that orchestrates chore organization with intelligent flow control.
    
    This agent demonstrates advanced multi-agent patterns including:
    - Conditional execution based on runtime state
    - Error handling and graceful degradation
    - Dynamic workflow adaptation
    - State validation between steps
    """

    chore_collector: LlmAgent
    process_sequencer: SequentialAgent
        
    def __init__(
        self, 
        chore_collector: LlmAgent,
        process_sequencer: SequentialAgent
    ):
        
        super().__init__(
            name="chore_organizer_agent",
            description="An intelligent chore organization coordinator with adaptive workflow control.",
            chore_collector=chore_collector,
            process_sequencer=process_sequencer,
            sub_agents=[
                chore_collector,
                process_sequencer
            ]
        )
    
    @override
    async def _run_async_impl(self, ctx: InvocationContext) -> AsyncGenerator[Event, None]:
        """
        Custom orchestration logic with intelligent flow control.
        """
        logger.info(f"[{self.name}] Starting intelligent chore organization workflow")
        
        try:
            # STAGE 1: Data Collection & Validation
            async for event in self._run_chore_collection(ctx):
                yield event
                
            # Check if chore collection is complete with structured data
            # If still in conversation mode, don't proceed to validation
            if not self._is_chore_collection_complete(ctx):
                logger.info(f"[{self.name}] Chore collection still in progress - conversation mode")
                return
                
            # Validate we have chores to work with (only after collection is complete)
            if not self._has_valid_chores(ctx):
                logger.warning(f"[{self.name}] No valid chores found. Ending workflow gracefully.")
                async for event in self._generate_empty_plan_response(ctx):
                    yield event
                return
            
            async for event in self.process_sequencer.run_async(ctx):
                yield event
            
            logger.info(f"[{self.name}] Workflow completed successfully")
            
        except Exception as e:
            logger.error(f"[{self.name}] Workflow error: {str(e)}")
            async for event in self._handle_workflow_error(ctx, e):
                yield event
    
    async def _run_chore_collection(self, ctx: InvocationContext) -> AsyncGenerator[Event, None]:
        """Stage 1: Collect and validate chore data"""
        logger.info(f"[{self.name}] Stage 1: Collecting chore data and user context")
        
        async for event in self.chore_collector.run_async(ctx):
            yield event
        
        # Parse the data
        parsed_data = self._parse_json_data(ctx.session.state.get("chore_list", ""))
        
        print(f"[{self.name}] Parsed data: {parsed_data}")

        # Remove chore_list from the state
        ctx.session.state.pop("chore_list", None)
        
        # Put the chores and user_context in the expected locations
        ctx.session.state["chores"] = parsed_data.get("chores", [])
        ctx.session.state["user_context"] = parsed_data.get("user_context", {})
        
        logger.info(f"[{self.name}] Raw chore collection completed")
        logger.debug(f"[{self.name}] Collected data: {ctx.session.state}")
        
    def _is_chore_collection_complete(self, ctx: InvocationContext) -> bool:
        """Check if chore collection has produced final structured data"""
        # Simply check if we have parsed data in session state
        chores = ctx.session.state.get("chores", [])
        user_context = ctx.session.state.get("user_context", {})
        
        # If we have any structured data, collection is complete
        # (Even empty lists/dicts mean the JSON was parsed successfully)
        has_chores_data = isinstance(chores, list)
        has_user_data = isinstance(user_context, dict) and len(user_context) > 0
        
        is_complete = has_chores_data and has_user_data
        
        if is_complete:
            logger.info(f"[{self.name}] Chore collection complete - found {len(chores)} chores and user context")
        else:
            logger.info(f"[{self.name}] Chore collection incomplete - chores: {type(chores)}, user_context: {type(user_context)} (len: {len(user_context) if isinstance(user_context, dict) else 'N/A'})")
            
        return is_complete
    
    def _has_valid_chores(self, ctx: InvocationContext) -> bool:
        """Check if we have valid chores to work with"""
        chores = ctx.session.state.get("chores", [])
        if not chores or len(chores) == 0:
            return False
        
        # Check if we have at least one chore with a valid name
        valid_chores = [chore for chore in chores if isinstance(chore, dict) and chore.get("name", "").strip()]
        return len(valid_chores) > 0
    
    async def _generate_empty_plan_response(self, ctx: InvocationContext) -> AsyncGenerator[Event, None]:
        """Generate a helpful response when no chores are provided"""
        user_context = ctx.session.state.get("user_context", {})
        user_name = user_context.get("name", "there")
        
        empty_response = f"""Hi {user_name}! 
        It looks like you don't have any chores to organize right now. That's great! 🎉
        When you do have chores to organize, feel free to come back and I'll help you create a personalized plan that fits your schedule and preferences.\n\n
        
        Here are some things I can help you with when you're ready:
        • Breaking down big tasks into manageable steps
        • Scheduling chores around your availability
        • Prioritizing urgent vs. flexible tasks
        • Creating efficient cleaning routines

        Have a wonderful day! ✨
        """
        
        logger.info(f"[{self.name}] Generated empty plan response for {user_name}")
        yield Event(
            invocation_id=ctx.invocation_id,
            author=self.name,
            content=types.Content(
                role="model",
                parts=[types.Part(text=empty_response)]
            )
        )
    
    async def _handle_workflow_error(self, ctx: InvocationContext, error: Exception) -> AsyncGenerator[Event, None]:
        """Handle workflow errors gracefully"""
        user_context = ctx.session.state.get("user_context", {})
        user_name = user_context.get("name", "there")
        
        error_response = f"""Hi {user_name}, 
        I encountered an issue while organizing your chores: {str(error)}
        Please try again, and if the problem persists, you might want to simplify your chore list or contact support.
        Sorry for the inconvenience! 😅

        Here are some things I can help you with when you're ready:
        • Breaking down big tasks into manageable steps
        • Scheduling chores around your availability
        • Prioritizing urgent vs. flexible tasks
        • Creating efficient cleaning routines

        Have a wonderful day! ✨
        """
                
        logger.error(f"[{self.name}] Generated error response for {user_name}: {str(error)}")
        yield Event(
            invocation_id=ctx.invocation_id,
            author=self.name,
            content=types.Content(
                role="model",
                parts=[types.Part(text=error_response)]
            )
        )

    def _parse_json_data(self, data: str) -> dict:
        """Parse JSON data from a string, handling various formatting issues"""
        if not data or not data.strip():
            logger.info(f"[{self.name}] No data to parse")
            return {}
            
        original_data = data
        data = data.strip()
        
        # Check if this looks like conversational text rather than JSON
        if not self._contains_json_structure(data):
            logger.info(f"[{self.name}] Data appears to be conversational text, not JSON. Conversation may still be in progress.")
            return {}
            
        try:
            # Step 1: Remove markdown formatting
            data = self._clean_markdown(data)
            
            # Step 2: Extract JSON from potentially mixed content
            json_content = self._extract_json_content(data)
            
            if not json_content:
                logger.info(f"[{self.name}] No JSON content found in data")
                return {}
            
            # Step 3: Clean up formatting issues
            json_content = self._clean_json_formatting(json_content)
                
            print(f"[{self.name}] Parsing cleaned JSON data: {json_content[:200]}...")
            
            # Step 4: Parse the JSON
            parsed = json.loads(json_content)
            
            # Step 5: Validate the structure
            if not self._validate_parsed_structure(parsed):
                return {}
                
            logger.info(f"[{self.name}] Successfully parsed JSON with {len(parsed.get('chores', []))} chores")
            return parsed
            
        except json.JSONDecodeError as e:
            logger.error(f"[{self.name}] Failed to parse JSON data: {str(e)}")
            logger.error(f"[{self.name}] Original data: {original_data[:500]}")
            return {}
    
    def _contains_json_structure(self, data: str) -> bool:
        """Check if data contains JSON structure indicators"""
        json_indicators = ['{', '```json', '"user_context"', '"chores"']
        return any(indicator in data for indicator in json_indicators)
    
    def _clean_markdown(self, data: str) -> str:
        """Remove markdown formatting"""
        # Remove ```json and ``` markers
        if "```json" in data:
            data = data.split("```json", 1)[1]
        if data.startswith("```"):
            data = data[3:]
        if data.endswith("```"):
            data = data[:-3]
        return data.strip()
    
    def _extract_json_content(self, data: str) -> str:
        """Extract JSON content from potentially mixed text"""
        # Find the first { and last }
        start_idx = data.find('{')
        if start_idx == -1:
            return ""
        
        # Find the matching closing brace
        brace_count = 0
        end_idx = -1
        
        for i in range(start_idx, len(data)):
            if data[i] == '{':
                brace_count += 1
            elif data[i] == '}':
                brace_count -= 1
                if brace_count == 0:
                    end_idx = i
                    break
        
        if end_idx == -1:
            return ""
            
        return data[start_idx:end_idx + 1]
    
    def _clean_json_formatting(self, json_content: str) -> str:
        """Clean up formatting issues in JSON content"""
        # Replace literal \n\n with actual newlines
        json_content = json_content.replace('\\n\\n', '\n\n')
        json_content = json_content.replace('\\n', '\n')
        
        # Remove extra whitespace while preserving JSON structure
        import re
        # Clean up excessive whitespace but keep JSON structure intact
        json_content = re.sub(r'\s+', ' ', json_content)
        
        # Fix common JSON formatting issues
        json_content = json_content.replace('{ ', '{').replace(' }', '}')
        json_content = json_content.replace('[ ', '[').replace(' ]', ']')
        
        return json_content.strip()
    
    def _validate_parsed_structure(self, parsed: dict) -> bool:
        """Validate that parsed data has expected structure"""
        if "chores" not in parsed and "user_context" not in parsed:
            logger.warning(f"[{self.name}] Parsed data doesn't contain expected keys (chores, user_context)")
            return False
            
        # Validate chores structure if present
        if "chores" in parsed:
            chores = parsed["chores"]
            if not isinstance(chores, list):
                logger.warning(f"[{self.name}] Chores is not a list")
                return False
                
        # Validate user_context structure if present  
        if "user_context" in parsed:
            user_context = parsed["user_context"]
            if not isinstance(user_context, dict):
                logger.warning(f"[{self.name}] User context is not a dictionary")
                return False
                
        return True


root_agent = ChoreOrganizerAgent(
    chore_collector=chore_collector_agent,
    process_sequencer=process_sequencer_agent
)