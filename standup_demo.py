from datetime import datetime, timedelta
from crewai import Agent, Task, Crew
from crewai_tools import MergeAgentHandlerTool

tools = MergeAgentHandlerTool.from_tool_pack(
    tool_pack_id="",
    registered_user_id="",
    tool_names=["github__get_commits", "slack__post_message"],
)

agent = Agent(
    role="GitHub Reporter",
    goal="Report my commits to Slack",
    backstory="You are a helpful assistant that checks a developer's GitHub activity and writes concise, natural standup updates.",
    tools=tools,
    verbose=True
)

yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

task = Task(
    description="Write a standup update from {yesterday} githb commit and post a summary of the message to the #daily-standup channel.",
    agent=agent,
    expected_output="Standup commit update in the format: Yesterday, Today, Blockers and confirmation that the message was posted to slack"
)

crew = Crew(
    agents=[agent],
    tasks=[task],
    verbose=True
)

result = crew.kickoff()
