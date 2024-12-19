from crewai import Agent
from tools import web_tool

from dotenv import load_dotenv

load_dotenv()

import os
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

os.environ["OPENAI_MODEL_NAME"]="gpt-4o-mini"


## Create a senior blog content researcher

blog_researcher=Agent(
    role='AI Blog Researcher from News Website',
    goal='get the relevant latest AI related news from News Website',
    verboe=True,
    memory=True,
    backstory=(
       "Expert in understanding videos in AI Data Science , Machine Learning And GEN AI." 
    ),
    tools=[web_tool],
    allow_delegation=True
)

## creating a senior blog writer agent with YT tool

blog_writer=Agent(
    role='Blog Writer',
    goal='Narrate compelling tech stories about the News Article and also add the refrence links at the end of blog',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
    ),
    tools=[web_tool],
    allow_delegation=False


)