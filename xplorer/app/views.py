import io
import base64

from huggingface_hub import login
import seaborn as sns
from django.shortcuts import render
from .forms import tweet_to_llm
from .models import MLModel

from django.shortcuts import render

from matplotlib import pyplot as plt
import matplotlib
matplotlib.use('Agg')


mlmodel = MLModel()

CONTEXT = "you have to read and analyze the prompt that given with this context and categorize the setiment of the text. POSITIVE, NEGATIVE, NEUTRAL, IRRELAVENT are the categories. only reply the category in json format. The text is "


def home(request):
    form = tweet_to_llm(request.POST)
    tweet = None
    image_base64 = None

    if request.method == "POST" and form.is_valid():
        tweet = form.cleaned_data["tweet"]

        context = CONTEXT
        prompt = context + tweet

        inputs, attentions = mlmodel.get_attention(prompt)

        num_heads = attentions[-1].shape[1]
        fig, axes = plt.subplots(1, num_heads, figsize=(20, 15))
        if num_heads == 1:
            axes = [axes]  # Make sure axes is iterable if there's only one head
        for i, ax in enumerate(axes):
            attn_data = attentions[-1][0, i].detach().numpy()
            cax = ax.matshow(attn_data, cmap='viridis')
            ax.set_title(f'Head {i+1}')
        fig.colorbar(cax, ax=axes, orientation='vertical', fraction=.1)
        # plt.tight_layout()

        # Convert plot to PNG image
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        image_png = buf.getvalue()
        buf.close()
        image_base64 = base64.b64encode(image_png).decode('utf-8')

    return render(request, "home.html", {"form": form, "tweet": tweet, "sentiment": "N/A", "plot": image_base64})
