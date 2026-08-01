# AI Coding Agent

## Architecture

This project contains a lightweight Python-based AI coding agent that explores an unfamiliar repository, identifies relevant files, creates an execution plan, and implements a product-oriented enhancement in an existing Node.js application.

**Components**

- `explorer.py` – scans the repository and identifies relevant JavaScript files
- `planner.py` – generates a brief execution plan
- `summarizer.py` – summarizes the planned work
- `main.py` – orchestrates the workflow

The target application remains a Node.js + Express + MongoDB application and is not rewritten in Python.

---

## Agent Workflow

1. Explore the repository structure
2. Identify relevant models, controllers, routes, and configuration files
3. Create a brief execution plan
4. Modify the codebase
5. Summarize the changes

---

## Repository Exploration

The agent recursively scans `.js` files while ignoring `node_modules`.

It automatically discovered the key files:

- `app/models/note.model.js`
- `app/controllers/note.controller.js`
- `app/routes/note.routes.js`
- `server.js`

---

## Product Decision

Given the request:

> Improve the application so users can better organise and search their notes.

The implementation chosen was:

- **Tags for note organization**
- **Search across title, content, and tags**
- **Filter notes by tag**

This provides a meaningful improvement while preserving the existing API structure and functionality.

---

## Changes Made

### Note model

Added:

```js
tags: {
    type: [String],
    default: []
}
```

### Create note API

Accepts an optional `tags` array.

### Update note API

Allows updating tags along with title and content.

### Search

Added query parameter:

```bash
GET /notes?q=react
```

Searches title, content, and tags.

### Tag filter

Added query parameter:

```bash
GET /notes?tag=interview
```

Returns notes containing the specified tag.

---

## Compatibility Fix

The original project used an older Mongoose version that was incompatible with the local MongoDB server. Mongoose was upgraded to version 8 and the connection code was updated accordingly.

---

## Assumptions and Trade-offs

- Regex-based search was used for simplicity and compatibility.
- Existing endpoints remain backward compatible.
- Notes without tags continue to work unchanged.
- The implementation focuses on a small, production-safe enhancement that fits within the 2–3 hour time limit.

---

## How to Run

### AI Agent

```bash
pip install -r requirements.txt
python main.py
```

### Enhanced Application

```bash
cd node-easy-notes-app
npm install
npm start
```

---

## Repositories

- AI Agent: https://github.com/IsravelTECH/ai-note-agent
- Enhanced App: https://github.com/IsravelTECH/node-easy-notes-app-enhanced