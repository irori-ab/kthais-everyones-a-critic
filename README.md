## Pre-requisites

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
