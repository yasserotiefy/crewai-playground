from crewai.llm import LLM

llm = LLM(
    model="ollama/llama3.2:1b",
    base_url="http://localhost:11434"
)
