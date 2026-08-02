# Contact Manager CLI

A simple command-line contact manager built in Python. Supports adding, viewing, searching, and deleting contacts, with data automatically saved to a local JSON file so it persists across restarts.

## Features

- Add, view, search, and delete contacts
- Case-insensitive partial search by name
- Automatic JSON-based persistence (data survives program restarts)
- Input validation and error handling (e.g. invalid numbers, missing files)

## How to Run

1. Make sure Python is installed on your system.
2. Clone this repository:
```
   git clone https://github.com/<your-username>/contact-manager-cli.git
   cd contact-manager-cli
```
3. Create and activate a virtual environment:
```
   python -m venv venv
   venv\Scripts\activate
```
   *(Run this in Command Prompt. If using PowerShell, you may need to allow script execution first — see [about_Execution_Policies](https://go.microsoft.com/fwlink/?LinkID=135170).)*
4. Run the app:
```
   python main.py
```

## What I Learned

- Setting up a clean Python development environment using virtual environments
- Git and GitHub fundamentals: cloning, staging, committing, and pushing changes
- Recovering from a real mistake — removing accidentally committed sensitive data from Git history using `git filter-repo`
- Building CRUD (Create, Read, Update, Delete) logic using Python lists and dictionaries
- Handling errors gracefully with `try`/`except` (e.g. `ValueError`, `FileNotFoundError`)
- Reading and writing JSON files for data persistence using Python's built-in `json` module
- Debugging real environment issues: Windows Python aliases, PowerShell execution policies, and Git identity configuration

## Tech Stack

- Python 3 (standard library only — no external dependencies)