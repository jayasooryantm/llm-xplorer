from django.db import models


class GameTweet(models.Model):
    game_name = models.CharField(max_length=100)
    sentiment_type = models.CharField(max_length=20)
    tweet = models.TextField()

    def __str__(self):
        return (f"{self.tweet}")
