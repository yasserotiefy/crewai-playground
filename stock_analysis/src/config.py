from crewai.llm import LLM

ollama_llm = LLM(
    model="ollama/gemma:2b",
    base_url="http://localhost:11434"
)

ollam_embedder = dict(
    provider='ollama',
    config=dict(
        model="nomic-embed-text",
    )
)
