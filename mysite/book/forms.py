#coding=utf8
#this operation is also for github lab
from django import forms
from models import Author
class add_book(forms.Form):
                title = forms.CharField(max_length = 20)
		AuthorID = forms.CharField(max_length = 20)
                #authorid = forms.ForeignKey(Author)
		#Age = forms.IntegerField()
		#Country = forms.CharField(label='国籍',max_length = 20)
		publisher = forms.CharField(max_length = 20)
		publishdate = forms.DateField()
		price = forms.FloatField()
		
class add_author(forms.Form):
                name = forms.CharField(max_length = 20)
                age = forms.IntegerField()
                country = forms.CharField(max_length = 20)
            
class update_book(forms.Form):
		AuthorID = forms.CharField(max_length = 20)
		publisher = forms.CharField(max_length = 20)
		publishdate = forms.DateField()
		price = forms.FloatField()

