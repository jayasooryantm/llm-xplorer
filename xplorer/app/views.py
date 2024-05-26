from django.shortcuts import render
from .forms import tweet_to_llm


def home(request):
    form = tweet_to_llm(request.POST)
    tweet = ""

    if request.method == "POST" and form.is_valid():
        tweet = form.cleaned_data["tweet"]

    return render(request, "home.html", {"form": form, "tweet": tweet})
