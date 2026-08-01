# AI Coding Agent

## Architecture

This project contains a lightweight Python-based AI coding agent that explores a repository, creates an execution plan, and applies product-oriented improvements to an existing Node.js application.

- Python 3.11
- OpenRouter / OpenAI compatible SDK
- Filesystem-based repository exploration

## Agent Workflow

1. Explore the repository
2. Identify relevant files
3. Create an execution plan
4. Modify the codebase
5. Summarize the changes

## Repository Exploration

The agent recursively scans JavaScript files and ignores `node_modules`. It identifies models, controllers, routes, and server configuration files automatically.

## Product Decision

From the request:

> Improve the application so users can better organise and search their notes.

The agent implemented:

- Tags for organizing notes
- Search across title, content, and tags
- Filter by tag

## Modified Repository

Add the GitHub URL of your modified repository here.

## Assumptions and Trade-offs

- Regex-based search was used for simplicity and compatibility.
- Existing APIs remain backward compatible.
- Notes without tags continue to work unchanged.
- The focus was on a small, production-safe enhancement within the time limit.