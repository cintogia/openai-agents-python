from pydantic import BaseModel
from typing import List
from agents import Agent

ROADMAP_PROMPT = (
    "You are a project roadmap planner. Given project requirements and constraints, "
    "create a detailed roadmap breaking down the project into phases, epics, and stories. "
    "Consider team capacity, timeline constraints, and dependencies between tasks. "
    "Organize work into sprints and ensure even distribution of work across the team."
)

class Story(BaseModel):
    title: str
    description: str
    estimated_hours: float
    assigned_to: str
    dependencies: List[str]
    priority: int

class Epic(BaseModel):
    title: str
    description: str
    stories: List[Story]
    phase: str

class ProjectRoadmap(BaseModel):
    phases: List[str]
    epics: List[Epic]
    total_estimated_hours: float
    risk_factors: List[str]

roadmap_agent = Agent(
    name="RoadmapPlannerAgent",
    instructions=ROADMAP_PROMPT,
    output_type=ProjectRoadmap,
) 