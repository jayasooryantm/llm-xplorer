from django.db import models

from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from huggingface_hub import login


class GameTweet(models.Model):
    game_name = models.CharField(max_length=100)
    sentiment_type = models.CharField(max_length=20)
    tweet = models.TextField()

    def __str__(self):
        return (f"{self.tweet}")


class MLModel:
    def __init__(self, model_name='openai-community/gpt2'):
        login(token="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")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)

    def get_attention(self, text):
        inputs = self.tokenizer(text, return_tensors='pt')
        outputs = self.model(**inputs, output_attentions=True)
        return inputs, outputs.attentions
