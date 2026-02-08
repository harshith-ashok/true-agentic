import json

IDEA_EXTRACTION_PROMPT_VERSION = "v1.0"

SYSTEM_PROMPT = """
You are an information extraction system.

Your task is to extract at most 3 atomic ideas from the input.

Definition of an idea:
- A single, self-contained statement
- Reflects intent, belief, decision, uncertainty, or constraint
- Would still matter if reread weeks later

Do NOT:
- Paraphrase conversational filler
- Merge multiple ideas into one
- Invent or infer beyond the text
- Provide advice or commentary

If no meaningful ideas are present, return an empty list.

Output ONLY valid JSON that conforms exactly to the schema provided.
"""

USER_TEMPLATE = """
Extract ideas from the following input.

Input:
\"\"\"
{content}
\"\"\"

Schema:
{{
  "ideas": [
    {{
      "content": "string",
      "idea_type": "principle | decision | question | constraint | observation",
      "confidence": 0.0
    }}
  ]
}}
"""


async def extract_ideas(llm_client, content: str) -> list[dict]:
    response = await llm_client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": USER_TEMPLATE.format(content=content)}
        ],
        temperature=0.0,
    )

    raw = response.choices[0].message.content

    try:
        data = json.loads(raw)
        ideas = data.get("ideas", [])
        return ideas[:3]
    except Exception:
        return []
