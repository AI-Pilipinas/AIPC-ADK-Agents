# Automation Analyst Agent

An intelligent agent that analyzes job descriptions and roles to identify automation opportunities. This agent breaks down job responsibilities into discrete tasks and evaluates their automation potential using a structured approach.

## Overview

The Automation Analyst agent takes a job description or role as input and produces a detailed analysis in the form of a markdown table. For each task identified in the role, it provides:

- A clear description
- Automation potential rating (High, Mid, Low)
- Rationale for the automation assessment
- Strategic recommendations for automation implementation

## Features

- **Task Decomposition**: Breaks down complex job roles into discrete, analyzable tasks
- **Automation Potential Assessment**: Uses a three-tier rating system (High ✅, Mid ⚠️, Low ❌)
- **Structured Analysis**: Provides clear rationale for each automation assessment
- **Strategic Recommendations**: Includes actionable next steps for automation implementation
- **Business-Focused Output**: Delivers professional, concise analysis suitable for business strategy

## Usage

The agent accepts plain-language job descriptions or role titles as input and returns a markdown table with the following structure:

| Task        | Description        | Automation Potential | Rationale              |
| ----------- | ------------------ | -------------------- | ---------------------- |
| [Task Name] | [Task Description] | [High/Mid/Low]       | [Assessment Rationale] |

The analysis concludes with an "Automation Opportunity Summary" that includes:

- Percentage breakdown of automation potential
- Strategic recommendations for workflow redesign
- Suggested tool integration opportunities

## Technical Details

- Built using the Google ADK Agents framework
- Utilizes the Gemini 2.0 Flash model for analysis
- Implements a structured prompt template for consistent output

## Example Output

For an Executive Assistant role, the agent might identify tasks like:

- Calendar Scheduling (Mid ⚠️)
- Email Management (High ✅)
- Stakeholder Coordination (Low ❌)

And provide strategic recommendations for automation implementation.

## Dependencies

- google.adk.agents
- gemini-2.0-flash model

## File Structure

```
automation_analyst/
├── __init__.py
├── agent.py          # Main agent configuration
├── prompt.py         # Agent instructions and prompt template
└── .gitignore
```
