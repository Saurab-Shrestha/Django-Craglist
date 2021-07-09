from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Search(models.Model):
    search = models.CharField(max_length=500,null=True)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.search)

    class Meta:
        verbose_name_plural ="Searches"


""" text editor Text-to-HTML """
class Editor(models.Model):
    body = RichTextField(blank=True, null = True)


""" Todo App """
class Todo(models.Model):
    title = models.CharField(max_length = 350)
    completed = models.BooleanField(default = False)
    created = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.title
    
    