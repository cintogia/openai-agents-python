from pydantic import BaseModel
from typing import List
from agents import Agent

PROJECT_INPUT_PROMPT = (
    "You are a project manager's assistant responsible for gathering initial project information. "
    "Ask for and validate the following project details:\n"
    "1. Project timeline (start date and end date)\n"
    "2. Team members (names and roles)\n"
    "3. Budget information (total hours, cost per hour)\n"
    "4. Any specific constraints or requirements\n"
    "Ensure all inputs are properly formatted and validated."
)

class TeamMember(BaseModel):
    name: str
    role: str
    hourly_rate: float
    available_hours_per_week: float

class ProjectInputData(BaseModel):
    project_name: str
    start_date: str
    end_date: str
    team_members: List[TeamMember]
    total_budget_hours: float
    total_budget_cost: float
    constraints: List[str]

project_input_agent = Agent(
    name="ProjectInputAgent",
    instructions=PROJECT_INPUT_PROMPT,
    output_type=ProjectInputData,
) 