from django.db import models
#this operation is for github lab
# Create your models here.
class Author(models.Model):
    AuthorID = models.AutoField(primary_key = True)
    Name = models.CharField(max_length = 20)
    Age = models.IntegerField()
    Country = models.CharField(max_length = 20)
    def __unicode__(self):
	    return self.Name
		
class Book(models.Model):
    ISBN = models.AutoField(primary_key = True)
    Title = models.CharField(max_length = 20)
    AuthorID = models.ForeignKey(Author)
    Publisher = models.CharField(max_length = 20)
    PublishDate = models.DateField()
    Price = models.FloatField()
    def __unicode__(self):
	    return self.Title
