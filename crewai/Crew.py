from crewai import Crew, Process
from Agents import researcher, writer
from Tasks import research_task, write_task

# Forming the tech-focused crew with some enhanced configurations
crew = Crew(
  agents=[researcher, writer],
  tasks=[research_task, write_task],
  process=Process.sequential,  # Optional: Sequential task execution is default
  memory=True,
  cache=True,
  max_rpm=100,
  share_crew=True
)

result = crew.kickoff(inputs={'topic': 'AI in healthcare'})
print(result)
