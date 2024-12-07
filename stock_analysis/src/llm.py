from crewai.llm import LLM

llm = LLM(
    model="ollama/gemma:2b",
    base_url="http://localhost:11434"
)

embedder = dict(
    provider='ollama',
    config=dict(
        model="nomic-embed-text",
    )
)
