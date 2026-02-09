import ollama
import json


def map_to_corep(context, user_query):

    prompt = f"""
You are an expert regulatory reporting assistant for COREP Own Funds.

Your task is to map the user scenario to the correct COREP field.

STRICT RULES:
You are performing structured data extraction, NOT conversation.

- ALWAYS populate every field.
- NEVER leave fields empty.
- If unsure, infer from context.
- If truly missing, add it to "missing_data".

IMPORTANT:

For Common Equity Tier 1 capital, use:

field_code: "CET1"

rule_reference: "CET1 must be reported under Own Funds"

explanation: Explain WHY the capital qualifies as CET1 using the context.

Return ONLY valid JSON.

JSON FORMAT:

{{
 "template":"Own Funds",
 "fields":[
    {{
      "field_code":"CET1",
      "value":"",
      "currency":"GBP",
      "rule_reference":"",
      "explanation":"",
      "confidence":"High"
    }}
 ],
 "missing_data":[]
}}

Context:
{context}

User Scenario:
{user_query}
"""


    response = ollama.chat(
        model='llama3',
        messages=[{"role": "user", "content": prompt}],
        options={"temperature": 0.1}
    )

    content = response['message']['content']

    # Extract JSON safely
    start = content.find("{")
    end = content.rfind("}") + 1

    json_str = content[start:end]

    return json.loads(json_str)
