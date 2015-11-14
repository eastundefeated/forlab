#coding=utf8
#this operation is for github lab too
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from models import Author,Book
from forms import add_book,add_author,update_book
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt

def index(request):
        books = Book.objects.all()
        if request.method == 'GET':
                if 'delete' in request.GET and request.GET['delete']:
                        ISBN = request.GET['delete']
                        book = Book.objects.filter(ISBN = ISBN)
                        book.delete()
                        books = Book.objects.all()
                        return render_to_response('index.html',{'books':books})
        else:
                books = Book.objects.all()
        return render_to_response('index.html',{'books':books})

def book_infomation(request,i):
        ISBN = i
        s = Book.objects.filter(ISBN = ISBN)
        if s:
                book = Book.objects.get(ISBN = ISBN)
                author = book.AuthorID
                return render_to_response('book_infomation.html',{'book':book,'author':author})
        error = "Error!"
        return render_to_response('book_infomation.html',{'error':error})
		
def search(request):
        if request.method == 'GET':
                if 'name' in request.GET and request.GET['name']:
                        name = request.GET['name']
                        s = Author.objects.filter(Name = name)
                        if s:
                                author = Author.objects.get(Name = name)
                                books = author.book_set.all()
                                return render_to_response('search.html',{'author':author,'books':books})
                        error = "The Author is not exist!"
                        return render_to_response('search.html',{'error':error})
        error = "Please Input a Author"
                #return render_to_response('search.html',{'error':error})
	return render_to_response('search.html')

@csrf_exempt
def add(request):
        #error = []
        authors = Author.objects.all()
	if request.method == 'POST':
                uf = add_book(request.POST)
                if uf.is_valid():
                        Title = uf.cleaned_data['title']
                        Publisher = uf.cleaned_data['publisher']
                        PublishDate = uf.cleaned_data['publishdate']
                        Price = uf.cleaned_data['price']
                        AuthorID = Author.objects.get(Name = uf.cleaned_data['AuthorID'])
                        book = Book.objects.create(Title = Title,AuthorID = AuthorID,Publisher = Publisher,
                                                   PublishDate = PublishDate,Price = Price)
                        book.save()
                        return HttpResponseRedirect('../index')
                error = "Error!Please Input Again!"
                return render_to_response('add.html',{'authors':authors,'error':error})
        else:
                authors = Author.objects.all()
        return render_to_response('add.html',{'authors':authors})

@csrf_exempt
def addauthor(request,option = "none"):
        if request.method == 'POST':
                af = add_author(request.POST)
                if af.is_valid():
                        Name = af.cleaned_data['name']
                        Age = af.cleaned_data['age']
                        Country = af.cleaned_data['country']
                        author = Author.objects.create(Name = Name,Age = Age,Country = Country)
                        author.save()
                        if str(option) == "add":
                                return HttpResponseRedirect('/add')
                        else:
                                return HttpResponseRedirect('/' + str(option) + '/')
                error = "Error!Please Input Again!"
                return render_to_response('addauthor.html',{'error':error})
        return render_to_response('addauthor.html')

@csrf_exempt
def update(request,i):
        try:
                ISBN = str(i)[:-1]
        except:
               error = "Error!"
               return render_to_response('update.html',{'ISBN':ISBN,'error':error,'Title':book.Title,'authors':authors,'Publisher':book.Publisher,'PublishDate':str(book.PublishDate),'Price':book.Price})
        authors = Author.objects.all()
        try :
                book = Book.objects.get(ISBN = ISBN)
        except:
                error = "Error!"
                return render_to_response('update.html',{'ISBN':ISBN,'error':error,'Title':book.Title,'authors':authors,'Publisher':book.Publisher,'PublishDate':str(book.PublishDate),'Price':book.Price})

        if request.method == 'POST':
                uf = update_book(request.POST)
                if uf.is_valid():
                        s = Author.objects.filter(Name = uf.cleaned_data['AuthorID'])
                        if s:
                                book.AuthorID = Author.objects.get(Name = uf.cleaned_data['AuthorID'])
                                book.Publisher = uf.cleaned_data['publisher']
                                book.PublishDate = uf.cleaned_data['publishdate']
                                book.Price = uf.cleaned_data['price']
                                book.save()
                                return HttpResponseRedirect('/book_infomation/' + ISBN)
                        else:
                                error = "Error!Please Input Again!"
                                return render_to_response('update.html',{'ISBN':ISBN,'error':error,'Title':book.Title,'authors':authors,'Publisher':book.Publisher,'PublishDate':str(book.PublishDate),'Price':book.Price})
        return render_to_response('update.html',{'ISBN':ISBN,'Title':book.Title,'authors':authors,'Publisher':book.Publisher,'PublishDate':str(book.PublishDate),'Price':book.Price})

def authors(request):
        authors = Author.objects.all()
        if request.method == 'GET':
                if 'delete' in request.GET and request.GET['delete']:
                        name = request.GET['delete']
                        author = Author.objects.filter(Name = name)
                        author.delete()
                        authors = Author.objects.all()
                        return render_to_response('authors.html',{'authors':authors})
        else:
                authors = Author.objects.all()
        return render_to_response('authors.html',{'authors':authors})
