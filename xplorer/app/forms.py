from django import forms


class tweet_to_llm(forms.Form):
    tweet = forms.CharField(required=True, label="", widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": "Enter the tweet/comment"}))
