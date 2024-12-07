# Stock Analysis with CrewAI
> Intelligent stock analysis using agent RAG (Retrieval Augmented Generation) architecture powered by CrewAI

## Quick Start Guide

### 1. Install Dependencies


#### Clone and setup OpenLit

```bash
git clone git@github.com:openlit/openlit.git
```

#### Run OpenLit

```bash
cd openlit && docker compose up -d && cd ..
```


#### Setup Ollama

```bash
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```


```bash
docker exec -it ollama ollama run llama2:7b
```

### 2. Install required Python packages

```bash
pip install -r requirements.txt
```

