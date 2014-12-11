## Define database models

'''
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __unicode__(self):
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title
'''

from django.db import models
from djangotoolbox.fields import ListField
from djangotoolbox.fields import EmbeddedModelField

class Post(models.Model):
	'''Stores Post objects'''
	# Store time
	created_on = models.DateTimeField(auto_now_add=True, null=True) 
	title = models.CharField(max_length=128)
	text = models.TextField()
	tags = ListField()
	comments = ListField(EmbeddedModelField('Comment'))

class Comment(models.Model):
	'''Stores Comment objects, part of Posts'''
	created_on = models.DateTimeField(auto_now_add=True)
	author = EmbeddedModelField('Author')
	text = models.TextField()

class Author(models.Model):
	name = models.CharField(max_length=128)
	email = models.CharField(max_length=128)

