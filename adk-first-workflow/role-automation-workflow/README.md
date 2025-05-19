# Role Automation Workflow

A sequential agent workflow that automates the process of analyzing and optimizing job roles through three specialized stages: job description creation, automation analysis, and prompt engineering for automatable tasks.

## Overview

This workflow combines three specialized agents to create a comprehensive role automation pipeline:

1. **Job Description Agent**: Creates detailed job descriptions
2. **Automation Analyst**: Analyzes the job description for automation potential
3. **Prompt Engineer**: Generates prompts for highly automatable tasks

## Workflow Stages

### 1. Job Description Creation

- Takes role requirements and responsibilities as input
- Generates comprehensive job descriptions
- Ensures clarity and completeness of role requirements

### 2. Automation Analysis

- Analyzes the job description for automation potential
- Breaks down tasks into automatable components
- Provides detailed assessment of automation feasibility
- Outputs a structured analysis of automation opportunities

### 3. Prompt Engineering

- Focuses on highly automatable tasks identified in stage 2
- Creates specialized prompts for automation
- Optimizes prompts for maximum efficiency
- Ensures prompts are clear and actionable

## Features

- **Sequential Processing**: Structured workflow from job description to automation prompts
- **Specialized Agents**: Each stage handled by a dedicated agent
- **Comprehensive Analysis**: Complete coverage from role definition to automation implementation
- **Structured Output**: Clear, actionable results at each stage
- **Integration Ready**: Designed to work with existing automation systems

## Technical Architecture

The workflow is built using the Google ADK Agents framework and consists of:

```
role-automation-workflow/
├── sub_agents/           # Contains specialized sub-agents
│   ├── __init__.py      # Exports sub-agents
│   ├── agent.py         # Sub-agent implementations
│   └── prompt.py        # Sub-agent prompts
├── agent.py            # Main agent implementation
├── prompt.py           # Agent prompts and instructions
└── __init__.py         # Package initialization
```

## Usage

1. **Input**: Provide role requirements or existing job description
2. **Processing**: The workflow automatically processes through all three stages
3. **Output**: Receive:
   - Comprehensive job description
   - Automation analysis with potential ratings
   - Optimized prompts for automatable tasks

## Dependencies

- Google ADK Agents framework
- Sub-agent dependencies:
  - Job Description Agent
  - Automation Analyst
  - Prompt Engineer

## Example Workflow

1. **Input**: "Create a workflow for a Customer Support Representative role"
2. **Stage 1**: Job Description Agent creates detailed role description
3. **Stage 2**: Automation Analyst identifies automatable tasks
4. **Stage 3**: Prompt Engineer creates prompts for tasks like:
   - Email response automation
   - Ticket categorization
   - Basic query resolution

## Best Practices

- Ensure clear input requirements for optimal results
- Review automation analysis before proceeding to prompt engineering
- Test generated prompts in a controlled environment
- Regularly update agent prompts based on performance feedback

## Contributing

When contributing to this workflow:

1. Follow the established agent structure
2. Maintain clear separation between workflow stages
3. Document any changes to the sequential process
4. Update prompts and instructions as needed
