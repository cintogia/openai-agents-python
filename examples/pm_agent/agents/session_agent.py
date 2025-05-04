from pydantic import BaseModel
from typing import List
from agents import Agent

SESSION_PLANNER_PROMPT = (
    "You are a sprint and session planning specialist. Given a project roadmap, "
    "break it down into concrete sprint sessions, planning meetings, and milestones. "
    "Consider team availability, sprint cadence, and necessary ceremonies like "
    "standups, sprint planning, and backlog refinement."
)

class SessionEvent(BaseModel):
    event_type: str  # "standup", "sprint_planning", "backlog_refinement", "milestone_review"
    duration_minutes: int
    required_attendees: List[str]
    frequency: str  # "daily", "weekly", "bi-weekly", "once"
    description: str

class Sprint(BaseModel):
    sprint_number: int
    start_date: str
    end_date: str
    stories: List[str]  # References to Story titles
    planned_hours: float
    team_members: List[str]

class SessionPlan(BaseModel):
    sprints: List[Sprint]
    recurring_events: List[SessionEvent]
    milestones: List[str]
    total_sprints: int

session_planner_agent = Agent(
    name="SessionPlannerAgent",
    instructions=SESSION_PLANNER_PROMPT,
    output_type=SessionPlan,
) 