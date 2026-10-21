
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# 1. Load the API key from .env
load_dotenv()

if not os.getenv("OPENAI_API_KEY"):
    raise ValueError(
        "OPENAI_API_KEY not found. Please check your .env file."
    )

# 2. Initialize the LangChain chat model
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7,
)

# 3. Write a clear and specific prompt
prompt = """
Suggest exactly 5 healthy breakfast ideas.

For this task, healthy means:
- Include nutritious ingredients.
- Prefer whole grains, fruits, vegetables, or protein sources.
- Avoid excessive added sugar and deep-fried foods.

Output rules:
- Number the ideas from 1 to 5.
- Write exactly one idea per line.
- Keep each idea short and practical.
- Do not include an introduction, conclusion, or extra explanation.
"""

# 4. Ask the model for a response
reply = llm.invoke(prompt)

# 5. Print only the actual text, not the entire message object
print(reply.content)
