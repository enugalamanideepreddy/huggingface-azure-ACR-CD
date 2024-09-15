# from transformers import pipeline
from fastapi import FastAPI, Response
from pydantic import BaseModel

# pipe = pipeline("summarization", model="Falconsai/text_summarization")


app = FastAPI()


class Body(BaseModel):
    text: str


@app.get('/')
def root():
    return Response("<h1>A self-documenting API to interact with a summarizing model</h1>")


@app.post('/generate')
def predict(body: Body):
    # results = pipe(body.text, max_length=35, num_return_sequences=1)
    results = ['Dengoo Nidrapo']
    return results[0]
