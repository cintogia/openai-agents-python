from pydantic import BaseModel
from typing import List
from agents import Agent

CALENDAR_PROMPT = (
    "You are a calendar coordination specialist. Given a session plan and team member "
    "calendars, schedule all necessary meetings and events. Consider time zones, "
    "existing commitments, and preferred working hours. Ensure all team members "
    "can attend critical meetings and suggest alternative times if conflicts exist."
)

class CalendarEvent(BaseModel):
    title: str
    start_time: str
    end_time: str
    attendees: List[str]
    event_type: str
    description: str
    recurrence: str = None  # Optional recurrence rule

class CalendarPlan(BaseModel):
    scheduled_events: List[CalendarEvent]
    unresolved_conflicts: List[str]
    recommendations: List[str]

calendar_agent = Agent(
    name="CalendarAgent",
    instructions=CALENDAR_PROMPT,
    output_type=CalendarPlan,
    # Note: In practice, you would add calendar API tools here
    tools=[],  # Add calendar integration tools
) 