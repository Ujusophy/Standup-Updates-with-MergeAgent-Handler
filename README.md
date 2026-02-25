# Standup-Updates-with-MergeAgent-Handler

This project generates a daily standup update from GitHub commits and posts it to Slack using **CrewAI** and **Merge Agent Handler tools**.

---

## How It Works

1. A CrewAI agent fetches GitHub commits using `github__get_commits`
2. The LLM summarizes the commits into a standup format:
   - Yesterday
   - Today
   - Blockers
3. The summary is posted to Slack using `slack__post_message`

---

## Required Keys & IDs
- **OpenAI API key**
- **Merge Agent Handler API Key**
- **Tool Pack ID**
- **Registered User ID**
- Slack + GitHub connected to the tool pack

---
## Configure Tool Input value in Merge Handler Console
These defaults allow the agent to fetch commits without being blocked by missing required parameters.
#### Slack Tool (`post_message`)
- `channel` → Slack Channel ID 
#### GitHub Tool (`get_commits`)
- `owner` → GitHub username
- `author` → GitHub username
- `repo` → GitHub repo
---

## Installation

### Clone the Repository
```bash
git clone https://github.com/Ujusophy/Standup-Updates-with-MergeAgent-Handler.git
```
### Project folder
```bash
cd Standup-Updates-with-MergeAgent-Handler
```
### Create and Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate 
```
### Install Dependencies
```bash
pip install -r requirements.txt
```
### Set Environment Variables
```bash
export OPENAI_API_KEY="your-openai-api-key"
export AGENT_HANDLER_API_KEY="your-merge-api-key"
```
### Run the Project
```bash
python standup_demo.py
```

### To Log run
```bash
LOG_LEVEL=DEBUG python standup_demo.py
```
