from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.templating import Jinja2Templates
from nltk.tokenize import sent_tokenize, word_tokenize
import asyncio
import nltk

# Ensure necessary NLTK data is available
nltk.download('punkt')

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


async def response_from_api():
    answer = """Absolutely! When applying for a loan of $500 to be paid over a period of 10 years, 
    it's important to ensure that you meet our standard requirements. We typically require applicants
    to demonstrate a stable source of income, whether it's from employment, freelance work, 
    or any other reliable means. Additionally, maintaining a positive credit history significantly 
    strengthens your application, as it reflects your ability to manage financial obligations over an 
    extended period. This helps us assess your ability to repay the loan responsibly over the specified 
    timeframe. Do you currently have a stable income and a favorable credit history? These factors play a 
    crucial role in the loan approval process and increase the likelihood of a successful application for
    a long-term commitment like this."""

    # Tokenize the answer into words
    tokens = word_tokenize(answer)

    for token in tokens:
        yield token
        await asyncio.sleep(0.1)  # Simulates latency in response


async def get_sentences(question: str):
    """Assembles tokens into sentences and yields complete sentences as they are formed."""
    complete_sentences = " "
    async for token in response_from_api():
        complete_sentences += " " + token + " "
        sentences = sent_tokenize(complete_sentences)
        if len(sentences) > 1:
            for sentence in sentences[:-1]:
                yield sentence
            complete_sentences = sentences[-1]
    # Yield the last sentence
    if complete_sentences.strip():
        yield complete_sentences


async def stream_response(question):
    """Streams sentences generated from the input question."""
    async for sentence in get_sentences(question):
        yield sentence + "\n"


@app.post("/question/")
async def post_question(question: str = Form(...)):
    """Endpoint to receive a question and stream the processed answer as sentences."""
    return StreamingResponse(stream_response(question), media_type="text/plain")
