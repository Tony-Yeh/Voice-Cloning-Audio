PROMPT = """
## Task: Voice Cloning Evaluation

**Voice cloning** is a technique that synthesizes speech in a target speaker’s voice using a given text input and a reference audio of the target speaker.

You are given three audio clips, in the following order:

1. Target speaker reference audio  
2. Synthesized audio A (from voice cloning model A)  
3. Synthesized audio B (from voice cloning model B)

**Your task:**  
Ignore background noise and text accuracy — focus only on speaker similarity. Decide which synthesized audio sounds more like the target speaker in terms of voice identity (e.g., timbre, pitch, tone)? (a) Synthesized audio A (b) Synthesized audio B.
"""

STRICT_OUTPUT = """
**Output format:**
Respond with either **(a)** or **(b)** only.
"""


def getPrompt(
    strict: bool = False,
):
    if strict:
        return PROMPT + STRICT_OUTPUT
    else:
        return PROMPT
