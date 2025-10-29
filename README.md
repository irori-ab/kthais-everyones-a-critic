# AI webapp Case: Everyone's a critic

## Goals

Explore common concepts around developing webapps that are not typically taught in classes:

* version control (Git, pull requests, code review)
* build pipelines (unit tests, Github Actions)
* deploy pipelines (GCP Cloud Run, Github Actions)

## Case

We're developing a chat bot to help give people constructive feedback on their writing, e.g.
essays, email, marketing material. 

There will be a simple UI with a chat interface and some options to tweak the type of 
critique given.

## Pre-requisites

### Fork this repository

Click the **Fork** button top right in GitHub.

Invite a team of collaborators with **Write** access. You can keep your own copy but add at least someone else to try out 
the code review flows.

### Get Groq API key

- Sign up for [Groq](https://console.groq.com)
- Get an [API key](https://console.groq.com/keys)
- Save it as a Streamlit secret (NOTE: folder in .gitignore !)

    ```bash
    mkdir .streamlit/
    echo "groq_api_key = \"gsk_...\"" >> .streamlit/secrets.toml
    ```

### Install `uv`

* Mac: `brew install uv`
* Windows: `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`

## Running 

```bash 
source ./.venv/bin/activate
streamlit run critic.py
```

## Run tests

```bash
uv run pytest
```

## Bootstrapping 

```bash
uv init
uv add streamlit langchain-groq pytest
uv add --editable --dev kthais-everyones-a-critic
```

Read more: https://github.com/data-sloth/uv-streamlit-setup
