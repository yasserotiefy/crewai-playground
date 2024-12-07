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
docker exec -it ollama ollama run gemma:2b
```

```bash
docker exec -it ollama ollama pull nomic-embed-text
```

### 2. Install required Python packages

```bash
pip install -r requirements.txt
```

### 3. Run the Stock Analysis Crew

```bash
python stock_analysis/src/stock_analysis/main.py
```

Open the `report.md` file to see the results.

access the OpenLit dashboard at http://localhost:3000/


