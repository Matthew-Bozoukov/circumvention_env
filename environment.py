from inspect_ai import Task, task
from inspect_ai.model import ChatMessageUser, ChatMessageSystem, Model
from prompts import DEFAULT_SYSTEM_PROMPT, DEFAULT_USER_PROMPT
 

@task
def circumvention_env(


    scorer=
    return Task(

        dataset=[Sample(
            input=[
                ChatMessageSystem(content=DEFAULT_SYSTEM_PROMPT),
                ChatMessageUser(content=DEFAULT_USER_PROMPT)
            ]

        )
        ],
        solver=[

        ],
        sandbox="docker"



    )
):
