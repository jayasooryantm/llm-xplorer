from django.shortcuts import render
from .forms import tweet_to_llm

from django.shortcuts import render
import subprocess

CONTEXT = "you have to read and analyze the prompt that given with this context and categorize the setiment of the text. POSITIVE, NEGATIVE, NEUTRAL, IRRELAVENT are the categories. only reply the category in json format. The text is "


def check_sentiment(tweet: str):
    # Get context data from the request (modify as needed based on your model)
    context = CONTEXT
    prompt = context + tweet
    # Construct the Ollama command with context (adjust based on your needs)
    ollama_command = ["ollama", "run", "llama3", prompt]

    # Execute Ollama command using subprocess
    try:
        response_bytes = subprocess.run(
            ollama_command, capture_output=True).stdout
        response_text = response_bytes.decode("utf-8").strip()
    except subprocess.CalledProcessError as error:
        response_text = f"Error calling Ollama: {error}"
    return response_text


def home(request):
    form = tweet_to_llm(request.POST)
    tweet = ""
    sentiment = ""

    if request.method == "POST" and form.is_valid():
        tweet = form.cleaned_data["tweet"]
        sentiment = check_sentiment(tweet)

    return render(request, "home.html", {"form": form, "tweet": tweet, "sentiment": sentiment})
