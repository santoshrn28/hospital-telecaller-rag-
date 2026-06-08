from fastapi import FastAPI, Request
from rag import retrieve_context
import openai

app = FastAPI()

openai.api_key = "YOUR_API_KEY"

def generate_response(query):
    context = retrieve_context(query)

    prompt = f"""
    You are a hospital call assistant.
    Answer politely and clearly.

    Context:
    {context}

    Question:
    {query}
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response['choices'][0]['message']['content']


@app.post("/query")
async def handle_query(req: Request):
    data = await req.json()
    user_query = data["query"]

    response = generate_response(user_query)

    return {"response": response}
