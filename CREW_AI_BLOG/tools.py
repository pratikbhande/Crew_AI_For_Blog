from crewai_tools import WebsiteSearchTool

# Example of initiating tool that agents can use 
# to search across any discovered websites
web_tool = WebsiteSearchTool()

# Example of limiting the search to the content of a specific website, 
# so now agents can only search within that website
web_tool = WebsiteSearchTool(website='https://techcrunch.com/category/artificial-intelligence/')