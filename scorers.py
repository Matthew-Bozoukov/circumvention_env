import os
from inspect_ai.model import Model, get_model
from inspect_ai.scorer import Score, Scorer, Target, accuracy, scorer, stderr
from inspect_ai.solver import TaskState

def scoring_function(state: TaskState,
    grader_model: str | Model | None,
    ):
    
    response = response_with_reasoning(state)

def response_with_reasoning(state: TaskState) -> str:
    content = state.output.choices[0].message.content

    if isinstance(content, str):
        return content

    parts: list[str] = []
    for item in content:
        item_type = getattr(item, "type", None)

        if item_type == "reasoning":
            reasoning = getattr(item, "summary", None) or getattr(item, "reasoning", "")
            if reasoning and not getattr(item, "redacted", False):
                parts.append(f"<model_reasoning>\n{reasoning}\n</model_reasoning>")
        elif item_type == "text":
            text = getattr(item, "text", "")
            if text:
                parts.append(f"<model_response>\n{text}\n</model_response>")

    return "\n\n".join(parts) or state.output.completion



def reward_hacker_scorer(grader_model: str | Model| None)-> Scorer:

    async def score(state: TaskState, target: Target)-> Score:
        