# Security Statement
Eric Dominguez

## Intended Users
This repo is meant for me as a student working on coursework, along with my instructor and TAs who need access to grade my assignments through Gradescope.

## Risk Assessment
The code and data here are low risk if someone got access to them. The datasets (in mod02_data, mod04_data, mod06_data) are just sample data for homework exercises, not real or sensitive information. The code is just homework solutions and doesn't include any passwords, API keys, or anything private. If someone got into this repo, the biggest concern would probably be another student copying my homework, not an actual security breach.

## Security Steps Taken
- There's a branch protection rule on main that requires every change to go through a pull request and get approved by a code owner before it can be merged. It also blocks force-pushes and deletion of the branch.
- A CODEOWNERS file lists my instructor as the required reviewer for any pull request, so changes to main need their approval.
- My .gitignore keeps my local virtual environment (3000-env/) and OS files (.DS_Store) out of the repo, so only actual code and course data get committed.
- This is just a personal fork for my own coursework, not something shared publicly or used in production, so there's not much exposure to begin with.
- No credentials or secrets are stored anywhere in the repo.

Given these protections are already set up, and the content isn't sensitive, I don't think I need any extra security measures for this repo right now.