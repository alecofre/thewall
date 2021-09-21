from login_app.models import User
from django.core.checks import messages
from django.db import models

# Create your models here.
class MessageManager(models.Manager):
     def verify_newMessage(self, postData):
          errors = {}

          if len(postData['new_message'].strip()) < 2 :
               errors['no_message'] = "ERROR: The message must have at least 1 character"
          
          return errors

class CommentManager(models.Manager):
     def verify_newComment(self, postData):
          errors = {}

          if len(postData['new_comment'].strip()) < 2 :
               errors['no_comment'] = "ERROR: The comment must have at least 1 character"
          
          return errors




class Message(models.Model):
     message = models.TextField(max_length=256)
     user = models.ForeignKey(User,related_name='posts', on_delete=models.CASCADE)
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)
     objects = MessageManager()

     def __str__(self) -> str:
         return super().__str__()

     def __repr__(self) -> str:
         return super().__repr__()


class Comment(models.Model):
     comment = models.TextField(max_length=256)
     message = models.ForeignKey(Message, related_name='comments', on_delete=models.CASCADE)
     user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)
     objects = CommentManager()

     def __str__(self) -> str:
         return super().__str__()

     def __repr__(self) -> str:
         return super().__repr__()

