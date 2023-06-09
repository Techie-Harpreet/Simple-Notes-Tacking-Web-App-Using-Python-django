from django.db import models
from django.contrib.auth.models import User
import uuid





class Notes(models.Model):
    nid = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False) 
    title = models.CharField(max_length=500)
    description = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)


    def __str__(self):
        return self.title

