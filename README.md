# LLM chatbot powered by Docker Model Runner
The LLM chatbot by streamlit using docker model runner.  
You need to upgrade Docker Desktop to version 4.40.

## Usage
1. Check "Enable host-side TCP support" and select port 8000 on Docker Desktop.
1. Pulls a model from Docker Hub to your local environment.
    ```shell
    docker model pull ai/mistral
    ```
1. Run a model and interact with it in chat mode.
    ```shell
    make run-model
    ```
1. Startup another console and run app.
    ```shell
    make run-app
    ```