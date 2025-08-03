from typing import Any
import httpx

from mcp.server import FastMCP

mcp = FastMCP("Server-name")

# mcp
# 1. tools -> functions, but then how does this differ from the resources 
# 2. prompts -> predefined prompts
# 3. resources -> files/web api

# Provide functionality through tools, sort of POST method; they are used to execute code or otherwise produce a side effect
@mcp.tool()
def add(a:int, b:int) -> int:
    """Add two numbers"""
    return a + b

# exposes data through resources; think of these as GET endpoints; they are used to load information into the LLM context
@mcp.resource("greeting://{name}") # why this in the resource??
def get_greeting(name:str) -> str:
    """Get a personalised greeting"""
    return f"Hello {name}"



# Define interactions patterns through Prompts; reusable templates for LLM interactons 
@mcp.prompt()
def report()->str:
    """Generate a prompt asking the AI to summarize the current to-do list
    Returns: 
        str: AI ready prompt string, or a default message if the list is empty
    """
    _todo_list= []
    if not _todo_list:
        return "There are no todo items"
    
    return f"Summarize the following to-do items: {','.joint(_todo_list)}"

# if __name__ == '__main__':
#     mcp.run(transport='stdio')
