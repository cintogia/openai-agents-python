import asyncio

# This is importing from the manager.py file in the same directory
from .manager import ProjectManagementManager


# Entrypoint for the financial bot example.
# Run this as `python -m examples.financial_research_agent.main` and enter a
# financial research query, for example:
# "Write up an analysis of Apple Inc.'s most recent quarter."
async def main() -> None:
    print("Welcome to the Project Management Assistant!")
    print("I'll help you plan and organize your project.")
    mgr = ProjectManagementManager()
    await mgr.run()


if __name__ == "__main__":
    asyncio.run(main())
