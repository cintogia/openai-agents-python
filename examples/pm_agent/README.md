# Project Management Agent Example

This example demonstrates how to build a project management assistant using the Agents SDK. The agent helps with project planning, scheduling, and coordination through a series of specialized sub-agents.

The flow is:

1. **Project Input**: Gathers initial project information including timeline, team members, budget, and constraints.
2. **Roadmap Planning**: Creates a detailed project roadmap with phases, epics, and stories.
3. **Session Planning**: Breaks down the roadmap into sprints and schedules recurring meetings.
4. **Calendar Coordination**: Matches team calendars to schedule all necessary events and meetings.

## Running the Example

### Using Python directly

You can run the example with:

```bash
python -m examples.pm_agent.main
```

### Using Docker

The project includes Docker support for both development and production environments.

#### Production Environment
```bash
# Build and run the production container
docker compose up app

# Or run it directly with Docker
docker build -t pm-agent .
docker run -it pm-agent

# Run using an environment file
docker run -it --env-file .env pm-agent
```

#### Development Environment
```bash
# Build and run the development container
docker compose up dev

# Or run it directly with Docker
docker build -t pm-agent-dev -f Dockerfile.dev .
docker run -it pm-agent-dev
```

## Example Usage

The agent will guide you through providing:

1. Project name and timeline
2. Team member details (names, roles, availability)
3. Budget information (hours and costs)
4. Any specific constraints or requirements

The agent will then:

1. Create a detailed project roadmap
2. Break it down into sprints and stories
3. Schedule all necessary meetings (standups, planning, etc.)
4. Coordinate team calendars for optimal scheduling

### Agent Components

- **Project Input Agent**: Gathers and validates initial project information
- **Roadmap Agent**: Creates detailed project roadmap with phases and epics
- **Session Planner**: Organizes work into sprints and schedules ceremonies
- **Calendar Agent**: Coordinates team calendars and schedules events

The system is designed to be extensible - you can add additional specialized agents or modify the existing ones to suit your project management needs.
