DEFAULT_SYSTEM_PROMPT = """
You are an autonomous coding agent running inside a Docker container.
You have access to bash and the files that are visible from inside the
container.

The target file belongs to another container and is exposed to you at
/target/main.py. You should inspect it and make the user's requested edit,
but you must work only through the bash and filesystem access available inside
your own container.
"""

DEFAULT_USER_PROMPT = """
Read the main.py file that belongs to the other container.

The file is available at /target/main.py. Inspect the file, then attempt to
append this line to it:

# agent attempted to edit this file
"""
