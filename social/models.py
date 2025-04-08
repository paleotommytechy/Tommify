from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name="liked_posts", blank=True)
    following = models.ManyToManyField(User, related_name='post_following', blank=True)
    
    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return f"{self.user.username} - {self.content[:30]}"
        
        
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "user_likes")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name = "post_likes")
    
    class Meta:
        unique_together = ('post', 'user')
        

        
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "user_comment")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name = "post_comment")
    likes = models.ManyToManyField(User, related_name="liked_comment", blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def total_likes(self):
        return self.likes.count()
    
    def __str__(self):
        return f"{self.user.username}: {self.content[:20]}"
    
class Friendship(models.Model):
    follower = models.ForeignKey(User, related_name= "following" ,on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name="followers", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'following')

    def __str__(self):
        return f"{self.follower} follows {self.following}"
        
        
        
