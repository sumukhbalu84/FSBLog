from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone
# Create your models here. 2 Models here: Post , Comment

class Post(models.Model):
    author = models.ForeignKey('auth.user')
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
         self.published_date = timezone.now()# timezone.now() essentially returns the Current Time and Date.
         self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)#comments are filtered based on whether they are approved or not!

    def get_absolute_url(self): #the get absolute URL is used as in for eg after creating an instance of a post where do you want to redirect the user amd to which URL.
        return reverse('post_detail',kwargs={'pk':self.pk})

    def __str__(self):#String override Method, compulsory for every Model.
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.post',related_name='comments')#Post is a foreign key because a comment needs to be attached to a code innit.
    author = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    approved_comment = models.BooleanField(default=False)


    def approve(self):#in case the comment is approved this is what has to be done!
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self):#String override Method, compulsory for every Model.
        return self.text
