from crewai import Task
from tools import web_tool
from agents import blog_researcher,blog_writer

## Research Task
research_task = Task(
  description=(
    "Identify the News Article."
    "Get detailed information about the News from the website."
  ),
  expected_output='A comprehensive 3 paragraphs long report based on the {topic} of News.',
  tools=[web_tool],
  agent=blog_researcher,
)

# Writing task with language model configuration
write_task = Task(
  description=(
    "get the info from the News Website on the topic {topic}."
  ),
  expected_output='Summarize the info from the News website on the topic{topic} and create the content for the blog',
  tools=[web_tool],
  agent=blog_writer,
  async_execution=False,
  output_file='new-blog-post.md'  # Example of output customization
)