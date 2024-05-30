from django.shortcuts import render
from .forms import tweet_to_llm

from django.shortcuts import render
import subprocess
import json


CONTEXT = "you have to read and analyze the prompt that given with this context and categorize the setiment of the text. POSITIVE, NEGATIVE, NEUTRAL, IRRELAVENT are the categories. only reply the category in json format. The text is "


def check_sentiment(tweet: str):
    # Get context data from the request (modify as needed based on your model)
    context = CONTEXT
    prompt = context + tweet
    command = ["python3",
               "/Users/jaya/Downloads/gpt2 app/gpt2.py", "--text", prompt]
    script_process = subprocess.run(command)
    try:
        with open("gpt2_output.txt", "r") as f:
            response_data = json.load(f)
    except FileNotFoundError:
        response_data = {"error": "Error: GPT2 script output not found."}

    return response_data


def attention_viz():
    pass


def home(request):
    form = tweet_to_llm(request.POST)
    tweet = ""
    sentiment = ""

    if request.method == "POST" and form.is_valid():
        tweet = form.cleaned_data["tweet"]
        sentiment = check_sentiment(tweet)
        print(sentiment)

    return render(request, "home.html", {"form": form, "tweet": tweet, "sentiment": sentiment})
