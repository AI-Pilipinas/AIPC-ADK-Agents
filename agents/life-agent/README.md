# Personal Life Agent

A multi-purpose personal assistant built with the Google Agent Development Kit (ADK) that helps with daily tasks and provides helpful information and motivation.

## Overview

The Personal Life Agent demonstrates how to build a multi-agent system with the ADK that serves as a personal assistant for day-to-day tasks. It uses a router pattern to delegate work to specialized sub-agents based on the user's needs.

### Key Features

- **Motivational Quotes**: Provides inspirational quotes to boost your mood
- **Mood Check**: Helps track and improve your emotional wellbeing
- **Fun Facts**: Shares interesting trivia and knowledge

## Agent Architecture

The Life Agent uses a hierarchical architecture with a main router agent and several specialized sub-agents:

1. **Root Agent (Router)**: Routes user requests to appropriate sub-agents
2. **Quote Agent**: Provides motivational and inspirational quotes
3. **Mood Check Agent**: Helps assess and track the user's mood
4. **Fun Fact Agent**: Shares interesting and educational fun facts

## Quick Start

### Prerequisites

- Python 3.9+
- Google ADK installed (`pip install google-adk`)

### Running the Agent

1. Clone the repository:
   ```bash
   git clone https://github.com/your-org/AIPC-ADK-Agents.git
   cd AIPC-ADK-Agents
   ```

2. Navigate to the agent directory:
   ```bash
   cd agents/life-agent
   ```

3. Set up environment variables:
   ```bash
   # Create your .env file from the example template
   cp .env.example .env
   
   # Open the .env file in your preferred editor and add your API keys
   # For example:
   # GOOGLE_API_KEY=your_api_key_here
   # OPENAI_API_KEY=your_openai_key_if_needed
   ```

4. Start the agent:
   ```bash
   # Launch the ADK web interface
   adk web
   ```

5. Open your browser and navigate to http://localhost:8000 to interact with your agent

## Example Conversations

Here are some examples of how you can interact with the Life Agent:

**Requesting a motivational quote:**
```
User: I need some motivation today.
Agent: "The only way to do great work is to love what you do." - Steve Jobs
```

**Checking your mood:**
```
User: I'm feeling a bit down today.
Agent: I'm sorry to hear that. On a scale of 1-10, how would you rate your mood? Let's talk about what might help improve it.
```

**Getting a fun fact:**
```
User: Tell me something interesting.
Agent: Here's a fun fact: Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly good to eat!
```

## Customization

### Modifying Prompts

You can customize the agent's behavior by editing the prompts in `prompts.py`. This file contains the instructions that guide each agent's responses.

### Adding New Sub-agents

To add a new specialized sub-agent:

1. Create a new file in the `sub_agents` directory
2. Define your agent using the ADK's Agent class
3. Add appropriate prompts in `prompts.py`
4. Import and add your new sub-agent to the list in `agent.py`

## How It Works

The Life Agent uses a prompt-based approach to guide agent behavior. When a user sends a message, the root agent analyzes the content and routes the request to the most appropriate sub-agent. Each sub-agent is specialized for a particular domain and has its own prompt instructions optimized for its specific task.

## Future Improvements

- Add a calendar management sub-agent
- Implement a to-do list feature
- Create a health and wellness tracking sub-agent
- Add personalization based on user preferences

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request with improvements or additional features.