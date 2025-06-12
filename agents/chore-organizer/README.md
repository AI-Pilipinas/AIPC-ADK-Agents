# Chore Organizer Agent

A sophisticated AI-powered chore organization system that helps users create personalized household task schedules. This agent uses an intelligent multi-stage workflow with **parallel processing**, **iterative optimization**, and **sequential coordination** to collect user preferences, analyze tasks, and generate optimized chore plans.

## 🏗️ Architecture Overview

The Chore Organizer Agent uses a **hierarchical multi-agent architecture** with intelligent flow control and multiple agent types:

```
ChoreOrganizerAgent (BaseAgent - Custom Orchestrator)
├── Stage 1: chore_collector_agent (LlmAgent - Data Collection)
└── Stage 2: process_sequencer_agent (SequentialAgent - Data Processing)
    ├── priority_assigner_agent (ParallelAgent - Concurrent Analysis)
    │   ├── effort_scorer_agent (LlmAgent)
    │   ├── urgency_flag_agent (LlmAgent)  
    │   └── preference_setter_agent (LlmAgent)
    ├── priority_merger_agent (LlmAgent - Data Synthesis)
    ├── chore_balancer_agent (LoopAgent - Iterative Optimization)
    │   ├── scheduler_agent (LlmAgent)
    │   └── balance_navigator_agent (LlmAgent with exit_loop tool)
    └── plan_formatter_agent (LlmAgent - Output Generation)
```

## 🔄 Workflow Overview

The agent follows a **sequential workflow** with **parallel processing** and **iterative optimization**:

1. **Collection Stage**: Conversational data gathering
2. **Completion Check**: Verify structured data is ready
3. **Validation Stage**: Ensure chores are viable
4. **Parallel Analysis**: Concurrent effort, urgency, and preference scoring
5. **Priority Synthesis**: Merge analysis results into unified priorities
6. **Iterative Balancing**: Loop-based schedule optimization with validation
7. **Formatting**: Generate user-friendly output

## 📋 Detailed Agent Breakdown

### 🎯 ChoreOrganizerAgent (Main Orchestrator)

**Type**: `BaseAgent` (Custom Implementation)
**Role**: Master coordinator and workflow controller

**Responsibilities**:
- **Flow Control**: Manages sequential execution of sub-agents
- **State Management**: Handles session data and intermediate results
- **Validation**: Ensures data completeness before proceeding
- **Error Handling**: Graceful degradation and user-friendly error messages
- **JSON Parsing**: Robust parsing of structured data from conversational input

**Key Features**:
- ✅ **Smart Completion Detection**: Only proceeds when data collection is complete
- ✅ **Robust JSON Parser**: Handles various formatting issues (markdown, whitespace, embedded text)
- ✅ **Empty State Handling**: Provides helpful responses when no chores are provided
- ✅ **Error Recovery**: Graceful handling of workflow errors

---

### 💬 chore_collector_agent (Stage 1: Data Collection)

**Type**: `LlmAgent` with tools
**Role**: Conversational data gathering specialist

**Responsibilities**:
- **User Interaction**: Friendly, step-by-step conversation flow
- **Context Gathering**: Collects user availability, time budget, household size
- **Chore Extraction**: Converts natural language descriptions into structured tasks
- **Data Structuring**: Outputs structured JSON with user context and chores

**Tools**: `get_current_date()` function for temporal context
**Output Key**: `chore_list`

**Conversation Flow**:
1. **Greeting & Name**: Warm introduction and name collection
2. **Date Collection**: Uses `get_current_date()` function for temporal context
3. **Availability**: Days of the week user is available
4. **Time Budget**: Daily time commitment for chores
5. **Household Info**: Number of people (affects task scope)
6. **Chore Gathering**: Free-form chore description and extraction

**Output Format**:
```json
{
  "user_context": {
    "name": "User's name",
    "date": "Current date",
    "available_days": ["Monday", "Tuesday", ...],
    "daily_time_budget": "45-60 minutes",
    "household_size": 3
  },
  "chores": [
    {
      "name": "Clear, actionable task name",
      "category": "cleaning/cooking/laundry/organization",
      "duration": 30,
      "location": "specific room/area",
      "tools": ["required items/equipment"],
      "deadline": "date or 'flexible'",
      "frequency": "daily/weekly/one-time"
    }
  ]
}
```

---

### ⚙️ process_sequencer_agent (Stage 2: Data Processing)

**Type**: `SequentialAgent`
**Role**: Sequential workflow coordinator for chore optimization

**Architecture**: Contains four specialized processing stages that execute in order

---

#### 🔄 priority_assigner_agent (Parallel Analysis Stage)

**Type**: `ParallelAgent`
**Role**: Concurrent analysis of chore characteristics

**Sub-Agents** (Running in Parallel):
- **effort_scorer_agent** (`LlmAgent`)
- **urgency_flag_agent** (`LlmAgent`)  
- **preference_setter_agent** (`LlmAgent`)

##### 💪 effort_scorer_agent
**Output Key**: `effort_scores`
**Scoring Criteria**:
- **Physical Effort** (1-10): Light → Medium → Heavy
- **Mental Effort** (1-10): Routine → Planning → Complex
- **Energy Type**: Determines best timing
- **Best Time**: Morning/afternoon/evening recommendations

**Output Format**:
```json
{
  "effort_scores": [
    {
      "chore_name": "Clean master bathroom",
      "physical_effort": 6,
      "mental_effort": 3,
      "total_effort": 5,
      "energy_type": "medium",
      "best_time": "morning"
    }
  ]
}
```

##### ⚡ urgency_flag_agent
**Output Key**: `urgency_flags`
**Analysis**: Time sensitivity and deadline evaluation
- Evaluates deadlines and time constraints
- Flags critical vs. flexible tasks
- Provides urgency levels (CRITICAL/HIGH/MEDIUM/LOW)

##### ❤️ preference_setter_agent
**Output Key**: `preferences`
**Analysis**: User preference and completion likelihood
- Assesses user preferences and patterns
- Estimates completion likelihood
- Provides grouping suggestions for efficiency

---

#### 🔗 priority_merger_agent (Data Synthesis Stage)

**Type**: `LlmAgent`
**Role**: Combines parallel analysis results into unified priorities

**Input Sources**:
- `{effort_scores}` from effort_scorer_agent
- `{urgency_flags}` from urgency_flag_agent
- `{preferences}` from preference_setter_agent

**Processing Algorithm**:
- **Urgency Weight**: 40% (time-sensitive tasks get priority)
- **Effort Weight**: 30% (balance high and low effort tasks)
- **Preference Weight**: 30% (user satisfaction and completion likelihood)

**Output Key**: `prioritized_chores`
**Output Format**:
```json
{
  "prioritized_chores": [
    {
      "chore_name": "Clean master bathroom",
      "priority_score": 85,
      "urgency_level": "HIGH",
      "effort_level": "medium",
      "preference_score": 7,
      "deadline": "2024-01-18",
      "duration": 45,
      "best_time": "morning",
      "group_with": ["related tasks"]
    }
  ]
}
```

---

#### ⚖️ chore_balancer_agent (Iterative Optimization Stage)

**Type**: `LoopAgent` (max 3 iterations)
**Role**: Iterative schedule optimization with validation

**Sub-Agents** (Sequential within loop):

##### 📅 scheduler_agent
**Type**: `LlmAgent`
**Role**: Creates daily schedules from prioritized chores
**Output Key**: `weekly_schedule`

**Scheduling Strategy**:
- **Weekdays**: 30-60 minutes max
- **Weekends**: 2-4 hours max  
- **Balance**: Mix high/medium/low effort tasks
- **Deadlines**: Schedule critical items first

**Output Format**:
```json
{
  "schedule": [
    {
      "day": "Monday",
      "date": "2024-01-15", 
      "total_time": 45,
      "tasks": [
        {
          "chore_name": "Do laundry",
          "priority_score": 85,
          "duration": 30,
          "start_time": "09:00",
          "effort_level": "medium",
          "urgency_level": "HIGH"
        }
      ]
    }
  ]
}
```

##### 🎯 balance_navigator_agent
**Type**: `LlmAgent` with tools
**Role**: Schedule validation and optimization guidance
**Tools**: `exit_loop()` function to terminate iteration when optimal
**Output Key**: `balanced_weekly_schedule`

**Validation Criteria**:
- **Daily Limits**: Max 4 hours, max 2 high-energy tasks
- **Weekly Distribution**: Balanced energy levels, critical task scheduling
- **Sustainability**: At least 1 chore-free day, energy management
- **Priority Validation**: Deadline compliance, dependency checking

**Loop Termination**: Calls `exit_loop()` when schedule meets all criteria (8+ balance score)

---

#### 📄 plan_formatter_agent (Output Generation Stage)

**Type**: `LlmAgent`
**Role**: User-friendly output generation

**Input Sources**:
- `{balanced_weekly_schedule}` from chore_balancer_agent
- `{user_context}` from session state

**Processing**:
- **Human-Readable Formatting**: Converts data into friendly, actionable plans
- **Personalization**: Incorporates user's name and preferences
- **Clarity Enhancement**: Adds helpful tips and organization suggestions
- **Motivation**: Includes encouraging language and progress tracking

**Output**: Final formatted chore plan (no output_key - final response)

---

## 🛡️ Error Handling & Edge Cases

### **Conversation Still in Progress**
- **Detection**: Checks if JSON data has been produced by chore_collector
- **Response**: Gracefully returns early, allowing conversation to continue
- **Logging**: Tracks conversation state for debugging

### **No Chores Provided**
- **Detection**: Validates parsed chore data structure and content
- **Response**: Friendly message with helpful suggestions for future use
- **User Experience**: Encouraging rather than error-focused

### **Malformed Data**
- **JSON Parsing**: Multi-step parser with format error recovery
- **Structure Validation**: Ensures required fields are present
- **Fallback**: Returns empty data rather than crashing

### **Workflow Errors**
- **Exception Handling**: Catches and logs all workflow errors
- **User Communication**: Provides helpful error messages with suggestions
- **Recovery**: Graceful degradation with alternative paths

---

## 🚀 Key Features

### **Multi-Agent Pattern Utilization**
- ✅ **ParallelAgent**: Concurrent effort, urgency, and preference analysis
- ✅ **LoopAgent**: Iterative schedule optimization with validation
- ✅ **SequentialAgent**: Ordered workflow coordination
- ✅ **Custom BaseAgent**: Intelligent orchestration and flow control

### **Intelligent Flow Control**
- ✅ Sequential agent execution with completion verification
- ✅ Early termination for incomplete conversations
- ✅ Iterative optimization with smart exit conditions
- ✅ Robust state management between stages

### **Advanced Data Processing**
- ✅ Parallel analysis for comprehensive chore assessment
- ✅ Multi-factor priority scoring algorithm
- ✅ Iterative balance optimization with validation
- ✅ Graceful handling of edge cases

### **User-Centric Design**
- ✅ Conversational, non-overwhelming interaction
- ✅ Personalized output based on user context
- ✅ Motivational and practical guidance
- ✅ Helpful responses for various scenarios

---

## 🔧 Technical Implementation

### **Agent Types Used**
- **`BaseAgent`**: Custom orchestrator (ChoreOrganizerAgent)
- **`LlmAgent`**: Conversational and processing agents
- **`SequentialAgent`**: Workflow coordination (process_sequencer)
- **`ParallelAgent`**: Concurrent analysis (priority_assigner)
- **`LoopAgent`**: Iterative optimization (chore_balancer)

### **Tools Integration**
- **`get_current_date()`**: Temporal context for scheduling
- **`exit_loop()`**: Smart termination of optimization iterations

### **State Management**
- Session state tracks conversation progress
- Intermediate data passed between processing stages
- Clean state transitions with validation
- Multiple output keys for different processing stages

### **Event Handling**
- Proper Event generation with required structure
- Content formatting using `types.Content` and `types.Part`
- Author attribution for all generated events

---

## 📊 Example Output

Here's what users receive after a complete workflow:

```
🏠 David's Personalized Chore Plan (June 12-16, 2025)

Based on your availability (Mon-Thu) and 45-60 minute daily budget:

📅 MONDAY (55 minutes) 
• 🧺 Wash, dry, and fold laundry (60 min) - URGENT: School starts Monday!
💡 Start this first thing - you can do other tasks while it runs

📅 TUESDAY (50 minutes)
• 🚿 Clean both bathrooms (45 min)
• 🍽️ Quick dish maintenance (5 min)

📅 WEDNESDAY (45 minutes)  
• 🧹 Vacuum whole house (45 min)
💡 Great mid-week refresh!

📅 THURSDAY (60 minutes)
• 🍱 Meal prep lunches (60 min) - Due Sunday night
• 🧸 Tidy up playroom (30 min) - Can overlap with meal prep

🎯 WEEKEND PROJECTS (Optional)
• 🏠 Organize garage (2 hours) - Flexible timing

✨ You've got this, David! This plan respects your time and gets everything done efficiently.
```

This architecture demonstrates sophisticated multi-agent patterns with **parallel processing**, **iterative optimization**, and **intelligent flow control** to create reliable, user-friendly chore organization that adapts to individual needs and circumstances. 