import os
import logging
import google.cloud.logging
from dotenv import load_dotenv

from google.adk import Agent
from google.adk.agents import SequentialAgent
from google.adk.tools.tool_context import ToolContext

# --- Setup ---
cloud_logging_client = google.cloud.logging.Client()
cloud_logging_client.setup_logging()

load_dotenv()
model_name = os.getenv("MODEL")

# --- Tool ---
def add_goal_to_state(tool_context: ToolContext, goal: str) -> dict:
    tool_context.state["GOAL"] = goal
    logging.info(f"[State] GOAL: {goal}")
    return {"status": "stored"}

# --- Agents ---

task_analyzer = Agent(
    name="task_analyzer",
    model=model_name,
    description="Analyzes the user goal and identifies components.",
    instruction="""
    You are an expert in breaking down complex goals.

    Analyze the GOAL:
    - Identify main objective
    - Identify sub-components
    - Detect dependencies

    GOAL:
    { GOAL }
    """,
    output_key="analysis"
)

task_atomizer = Agent(
    name="task_atomizer",
    model=model_name,
    description="Breaks goal into atomic micro-tasks.",
    instruction="""
    Convert the GOAL and ANALYSIS into:
    - Smallest possible actionable steps
    - Each step must be clear and executable
    - Maintain logical order

    GOAL:
    { GOAL }

    ANALYSIS:
    { analysis }
    """,
    output_key="atomic_tasks"
)

formatter = Agent(
    name="formatter",
    model=model_name,
    description="Formats atomic tasks.",
    instruction="""
    Present ATOMIC_TASKS as:
    - Numbered list
    - Clear and minimal steps

    ATOMIC_TASKS:
    { atomic_tasks }
    """
)

workflow = SequentialAgent(
    name="task_atomizer_workflow",
    sub_agents=[task_analyzer, task_atomizer, formatter]
)

root_agent = Agent(
    name="task_atomizer_entry",
    model=model_name,
    instruction="""
    - Ask user for a goal
    - Store it using tool
    - Pass to workflow
    """,
    tools=[add_goal_to_state],
    sub_agents=[workflow]
)
