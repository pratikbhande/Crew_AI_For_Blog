# AI Blog Research and Writing Pipeline

## Overview
This project sets up a pipeline to automate the research and creation of blog content related to AI news. It consists of a system of agents and tools working together to gather the latest AI-related news, extract key insights, and generate engaging blog posts.

## Components
### 1. **Agent System**
The core functionality is built around agents that perform specialized tasks:
- **Blog Researcher**: An AI agent dedicated to finding the latest AI-related news articles from specified sources.
- **Blog Writer**: An AI agent responsible for summarizing the researched news and crafting compelling blog content, including references.

### 2. **Tools**
Tools are utilities that assist the agents in accomplishing their tasks. 
- **WebsiteSearchTool**: Enables agents to search and extract information from specific websites or broader sources.

### 3. **Tasks**
Tasks define specific objectives for the agents:
- **Research Task**: Conducts in-depth research to retrieve relevant news articles and summarize their content.
- **Writing Task**: Converts the researched content into an engaging blog post with proper references.

### 4. **Crew**
A "Crew" orchestrates the agents and tasks, ensuring sequential execution and proper coordination.

---

## Files

### 1. `agent.py`
Defines the AI agents:
- **Blog Researcher**:
  - Role: Research AI news articles.
  - Tools: `web_tool` (WebsiteSearchTool restricted to TechCrunch AI category).
  - Features: Memory, verbose execution, and task delegation.
- **Blog Writer**:
  - Role: Create engaging blog posts based on the research.
  - Tools: `web_tool`.
  - Features: Memory and verbose execution.

### 2. `tools.py`
Defines the tools used by the agents:
- **WebsiteSearchTool**:
  - Configured to search content specifically within the `https://techcrunch.com/category/artificial-intelligence/` domain.

### 3. `tasks.py`
Defines the tasks for the pipeline:
- **Research Task**:
  - Description: Research and summarize detailed information about the latest AI news.
  - Output: A comprehensive 3-paragraph report.
  - Agent: `blog_researcher`.
- **Writing Task**:
  - Description: Summarize research into a blog format with references.
  - Output: Blog content written to `new-blog-post.md`.
  - Agent: `blog_writer`.

### 4. `crew.py`
Coordinates the execution of agents and tasks:
- Defines the crew consisting of the `blog_researcher` and `blog_writer` agents.
- Executes tasks sequentially to produce blog content.
- Configures options for memory, caching, and execution limits.

---

## Usage
### 1. Prerequisites
- Install necessary dependencies: `crewai`, `crewai_tools`, `dotenv`.
- Set up an environment file (`.env`) containing:
  ```
  OPENAI_API_KEY=your_openai_api_key
  ```

### 2. Configuration
- Ensure the `web_tool` in `tools.py` is configured for the desired website.
- Update the `output_file` in `tasks.py` for the writing task if needed.

### 3. Execution
Run the main script in `crew.py`:
```bash
python crew.py
```

### 4. Output
- The research summary is processed into a blog post.
- The blog content is saved to `new-blog-post.md`.

---

## Customization
- **Adding Tools**: Add new tools in `tools.py` and register them with the agents.
- **Expanding Roles**: Modify `agent.py` to include more agents or extend existing roles.
- **Task Adjustments**: Modify `tasks.py` to include additional or alternate tasks.

---

## Future Enhancements
- Support for multiple news sources.
- Integration with a CMS for automated publishing.
- Advanced natural language processing for content personalization.

---

## License
This project is open-source and available under the MIT License.

