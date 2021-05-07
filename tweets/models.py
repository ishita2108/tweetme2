import random
from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

class TweetLike(models.Model):
    user =  models.ForeignKey(User, on_delete = models.CASCADE)
    tweet =  models.ForeignKey('Tweet', on_delete = models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add = True)


class Tweet(models.Model):
    #id = modles.AutoField(primary_key = True)             Builtin in django
    parent = models.ForeignKey('self', on_delete = models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)  # a user can have many tweets
    likes = models.ManyToManyField(User,related_name='tweet_user', blank=True, through=TweetLike)
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to ='images/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add = True)

    # def __str__(self):
    #     return self.content

    class Meta:
        ordering = ['-id']
    @property
    def is_retweet(self):
        return self.parent != None
        
    def serialize(self):
        '''
        Old Method to serializr before using DRF
        '''
        return{
            "id": self.id,
            "content": self.content,
            "likes": random.randint(0,200)
        }
