from langgraph.graph import StateGraph, END
from agents import *

workflow = StateGraph(AgentState)

workflow.add_node("scout", domain_scout_agent)
workflow.add_node("generator", question_generator_agent)
workflow.add_node("iteration_manager", increment_iteration_agent)
workflow.add_node("alchemist", data_alchemist_agent)
workflow.add_node("designer", experiment_designer_agent)
workflow.add_node("critic", critic_agent)
workflow.add_node("uncertainty", uncertainty_agent)
workflow.add_node("paper_gen", paper_generator_agent)

workflow.set_entry_point("scout")
workflow.add_edge("scout", "generator")
workflow.add_edge("generator", "iteration_manager")
workflow.add_edge("iteration_manager", "alchemist")
workflow.add_edge("alchemist", "designer")
workflow.add_edge("designer", "critic")
workflow.add_edge("critic", "uncertainty")

def decide_to_iterate(state: AgentState):
    score = state["confidence_scores"].get("current_cycle", 0)
    count = state.get("iteration_count", 0)
    # 5 cycle limit and 60% threshold logic
    if score < 60 and count < 5:
        return "iteration_manager"
    return "paper_gen"

workflow.add_conditional_edges("uncertainty", decide_to_iterate)
workflow.add_edge("paper_gen", END)

research_app = workflow.compile()