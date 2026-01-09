from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from graph import research_app

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/research")
async def start_research():
    initial_state = {
        "domain": "", "questions": [], "chosen_question": "", "research_data": [], 
        "hypothesis": "", "critique": "", "confidence_scores": {}, 
        "iteration_count": 0, "final_paper": "", "plotly_json": "", "logs": ["System active."]
    }
    # Increased recursion_limit to allow for 5 cycles
    result = research_app.invoke(initial_state, {"recursion_limit": 50})
    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)