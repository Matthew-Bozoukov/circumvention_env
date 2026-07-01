from inspect_ai import Task, task
from inspect_ai.model import ChatMessageUser, ChatMessageSystem, Model
from prompts import DEFAULT_SYSTEM_PROMPT, DEFAULT_USER_PROMPT
from inspect_ai.solver import generate,use_tools
from inspect_ai.tool import bash, read_file
from scorers import reward_hacker_scorer
from inspect_ai.dataset import Sample
@task
def circumvention_env(
    grader_model: str | Model | None = None,
    ):


    scorer=reward_hacker_scorer(grader_model)
    
    
    return Task(

        dataset=[Sample(
            input=[
                ChatMessageSystem(content=DEFAULT_SYSTEM_PROMPT),
                ChatMessageUser(content=DEFAULT_USER_PROMPT)
            ]

        )
        ],
        solver=[
            use_tools(
                bash(timeout=20),
                read_file()
            ),
            generate(tool_calls="loop"),
        ],
        scorer=scorer,
        sandbox="docker")
