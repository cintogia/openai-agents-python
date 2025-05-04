from __future__ import annotations

import asyncio
from rich.console import Console

from agents import Runner, RunResult, custom_span, gen_trace_id, trace

from .agents.project_input_agent import ProjectInputData, project_input_agent
from .agents.roadmap_agent import ProjectRoadmap, roadmap_agent
from .agents.session_agent import SessionPlan, session_planner_agent
from .agents.calendar_agent import CalendarPlan, calendar_agent
from .printer import Printer

class ProjectManagementManager:
    """
    Orchestrates the project management flow: gathering input, planning roadmap,
    scheduling sessions, and coordinating calendars.
    """

    def __init__(self) -> None:
        self.console = Console()
        self.printer = Printer(self.console)

    async def run(self) -> None:
        trace_id = gen_trace_id()
        with trace("Project management trace", trace_id=trace_id):
            self.printer.update_item(
                "trace_id",
                f"View trace: https://platform.openai.com/traces/trace?trace_id={trace_id}",
                is_done=True,
                hide_checkmark=True,
            )
            
            # Step 1: Gather project input
            self.printer.update_item("input", "Gathering project information...")
            project_data = await self._gather_project_input()
            self.printer.mark_item_done("input")

            # Step 2: Create roadmap
            self.printer.update_item("roadmap", "Planning project roadmap...")
            roadmap = await self._create_roadmap(project_data)
            self.printer.mark_item_done("roadmap")

            # Step 3: Plan sessions
            self.printer.update_item("sessions", "Planning sprint sessions...")
            session_plan = await self._plan_sessions(roadmap, project_data)
            self.printer.mark_item_done("sessions")

            # Step 4: Schedule in calendar
            self.printer.update_item("calendar", "Coordinating calendars...")
            calendar_plan = await self._schedule_calendar(session_plan, project_data)
            self.printer.mark_item_done("calendar")

            self.printer.end()

            # Print final results
            print("\n=== Project Plan Summary ===\n")
            print(f"Project: {project_data.project_name}")
            print(f"Timeline: {project_data.start_date} to {project_data.end_date}")
            print(f"\nTeam Members:")
            for member in project_data.team_members:
                print(f"- {member.name} ({member.role})")
            
            print("\n=== Roadmap ===")
            print(f"Total Phases: {len(roadmap.phases)}")
            print(f"Total Epics: {len(roadmap.epics)}")
            
            print("\n=== Sprint Plan ===")
            print(f"Total Sprints: {session_plan.total_sprints}")
            print("Recurring Events:")
            for event in session_plan.recurring_events:
                print(f"- {event.event_type} ({event.frequency})")
            
            print("\n=== Calendar ===")
            print("Scheduled Events:", len(calendar_plan.scheduled_events))
            if calendar_plan.unresolved_conflicts:
                print("\nUnresolved Conflicts:")
                for conflict in calendar_plan.unresolved_conflicts:
                    print(f"- {conflict}")

    async def _gather_project_input(self) -> ProjectInputData:
        result = await Runner.run(project_input_agent, "Please provide project details")
        return result.final_output_as(ProjectInputData)

    async def _create_roadmap(self, project_data: ProjectInputData) -> ProjectRoadmap:
        input_data = (
            f"Project: {project_data.project_name}\n"
            f"Timeline: {project_data.start_date} to {project_data.end_date}\n"
            f"Team: {[member.name for member in project_data.team_members]}\n"
            f"Budget Hours: {project_data.total_budget_hours}\n"
            f"Constraints: {project_data.constraints}"
        )
        result = await Runner.run(roadmap_agent, input_data)
        return result.final_output_as(ProjectRoadmap)

    async def _plan_sessions(
        self, roadmap: ProjectRoadmap, project_data: ProjectInputData
    ) -> SessionPlan:
        input_data = (
            f"Roadmap Phases: {roadmap.phases}\n"
            f"Total Hours: {roadmap.total_estimated_hours}\n"
            f"Team Members: {[member.name for member in project_data.team_members]}\n"
            f"Project Timeline: {project_data.start_date} to {project_data.end_date}"
        )
        result = await Runner.run(session_planner_agent, input_data)
        return result.final_output_as(SessionPlan)

    async def _schedule_calendar(
        self, session_plan: SessionPlan, project_data: ProjectInputData
    ) -> CalendarPlan:
        input_data = (
            f"Session Plan: {len(session_plan.sprints)} sprints\n"
            f"Team Members: {[member.name for member in project_data.team_members]}\n"
            f"Events to Schedule: {[event.event_type for event in session_plan.recurring_events]}"
        )
        result = await Runner.run(calendar_agent, input_data)
        return result.final_output_as(CalendarPlan)
