# Local LLM
### A local AI assistant

## Stack
- Python
- Ollama
- DeepSeek R-1
- Chainlit

## How to Run
1. Install dependencies:
    ```
    pip install -r requirements.txt   
    ```
2. Start Ollama:
   ```
   ollama serve
   ```
3. On a new terminal, run app:
    ```
    chainlit run src.app.py -w
    ```