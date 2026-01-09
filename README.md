🔬 Autonomous Multi-Agent Research Assistant
An intelligent, self-evolving research engine built with LangGraph that discovers niche scientific domains and synthesizes high-value research papers with zero human intervention.

🌟 Project Overview
This system uses a "Human-out-of-the-Loop" architecture. It doesn't just search the web; it critiques its own findings, quantifies its own uncertainty, and iterates until it reaches a high confidence score.

Key Features
Autonomous Discovery: Identifies emerging scientific trends (post-2024) using real-time search.

Self-Correction Loop: Implements a 5-cycle research process where a Critic Agent ruthlessly attacks the proposed logic.

Uncertainty Quantification: A dedicated agent scores research quality (0-100%); if the score is low, the system automatically restarts the research cycle.

Full-Stack Deployment: Backend containerized via Docker on Railway and Frontend hosted on Netlify.

🏗️ Agentic Architecture
The system is organized as a Stateful Graph where agents pass a shared "Research State" to one another:

Domain Scout: Uses Tavily API to find niche frontiers.

Question Generator: Formulates complex, multi-source research questions.

Experiment Designer: Devises formal hypotheses and methodologies.

Critic Agent: Checks for logic flaws and statistical validity.

Uncertainty Agent: Decides whether to finalize the paper or iterate based on confidence.

Paper Generator: Synthesizes the final findings into a professional Markdown report.

🛠️ Tech Stack
Orchestration: LangGraph (Python)

LLMs: Groq (Llama 3.1) & Google Gemini 1.5 Flash

Search: Tavily AI

API Framework: FastAPI

Frontend: React.js & Plotly (for interactive confidence charts)

Infrastructure: Docker, Railway, Netlify

🚀 Deployment & Installation

Local Setup (via Docker)
The easiest way to run the backend is using the provided Dockerfile.

Clone the Repo:

Bash

git clone https://github.com/PrathamMJain147/ai-research-assistant.git
cd ai-research-assistant
Add Environment Variables: Create a .env file in the root directory:

Code snippet

TAVILY_API_KEY=your_key
GROQ_API_KEY=your_key
GOOGLE_API_KEY=your_key
Build and Run:

Bash

docker build -t research-agent .
docker run -p 8000:8000 --env-file .env research-agent
