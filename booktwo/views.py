# views.py
from django.shortcuts import render
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from book.models import Contactus
from booktwo.models import Bookshelf,review
from math import ceil 
# Create your views here.

def getstarted(request):
	if request.user.is_authenticated:
		return render(request,"interior2.html")
	else:
		messages.warning(request,"Login first")
		return render(request,"index.html")

def fantasy(request):
	return render(request,"categories.html")

def romance(request):
	return render(request,"categories2.html")

def horror(request):
	return render(request,"categories3.html")

def fiction(request):
	return render(request,"categories4.html")

def biography(request):
	return render(request,"categories5.html")
def fantasydomestic(request):
	allbook=[]
	fandomobj=Bookshelf.objects.filter(book_genre='fantasy', book_nationality='domestic')
	n=len(fandomobj)
	nSlides= n // 3 + ceil((n/3)-(n//3))
	allbook.append([fandomobj,range(1,nSlides),nSlides])
	params={'allbook':allbook}
	return render(request,"bookshow.html",params)

def fantasyinternational(request):
	allbook=[]
	fandomobj=Bookshelf.objects.filter(book_genre='fantasy', book_nationality='international')
	n=len(fandomobj)
	nSlides= n // 3 + ceil((n/3)-(n//3))
	allbook.append([fandomobj,range(1,nSlides),nSlides])
	params={'allbook':allbook}
	return render(request,"bookshow.html",params)

def romancedomestic(request):
	allbook=[]
	fandomobj=Bookshelf.objects.filter(book_genre='romance', book_nationality='domestic')
	n=len(fandomobj)
	nSlides= n // 3 + ceil((n/3)-(n//3))
	allbook.append([fandomobj,range(1,nSlides),nSlides])
	params={'allbook':allbook}
	return render(request,"bookshow.html",params)

def romanceinternational(request):
	allbook=[]
	fandomobj=Bookshelf.objects.filter(book_genre='romance', book_nationality='international')
	n=len(fandomobj)
	nSlides= n // 3 + ceil((n/3)-(n//3))
	allbook.append([fandomobj,range(1,nSlides),nSlides])
	params={'allbook':allbook}
	return render(request,"bookshow.html",params)

def horrordomestic(request):
	allbook=[]
	fandomobj=Bookshelf.objects.filter(book_genre='horror', book_nationality='domestic')
	n=len(fandomobj)
	nSlides= n // 3 + ceil((n/3)-(n//3))
	allbook.append([fandomobj,range(1,nSlides),nSlides])
	params={'allbook':allbook}
	return render(request,"bookshow.html",params)

def horrorinternational(request):
	allbook=[]
	fandomobj=Bookshelf.objects.filter(book_genre='horror', book_nationality='international')
	n=len(fandomobj)
	nSlides= n // 3 + ceil((n/3)-(n//3))
	allbook.append([fandomobj,range(1,nSlides),nSlides])
	params={'allbook':allbook}
	return render(request,"bookshow.html",params)

def fictiondomestic(request):
	allbook=[]
	fandomobj=Bookshelf.objects.filter(book_genre='fiction', book_nationality='domestic')
	n=len(fandomobj)
	nSlides= n // 3 + ceil((n/3)-(n//3))
	allbook.append([fandomobj,range(1,nSlides),nSlides])
	params={'allbook':allbook}
	return render(request,"bookshow.html",params)

def fictioninternational(request):
	allbook=[]
	fandomobj=Bookshelf.objects.filter(book_genre='fiction', book_nationality='international')
	n=len(fandomobj)
	nSlides= n // 3 + ceil((n/3)-(n//3))
	allbook.append([fandomobj,range(1,nSlides),nSlides])
	params={'allbook':allbook}
	return render(request,"bookshow.html",params)

def biographydomestic(request):
	allbook=[]
	fandomobj=Bookshelf.objects.filter(book_genre='biography', book_nationality='domestic')
	n=len(fandomobj)
	nSlides= n // 3 + ceil((n/3)-(n//3))
	allbook.append([fandomobj,range(1,nSlides),nSlides])
	params={'allbook':allbook}
	return render(request,"bookshow.html",params)

def biographyinternational(request):
	allbook=[]
	fandomobj=Bookshelf.objects.filter(book_genre='biography', book_nationality='international')
	n=len(fandomobj)
	nSlides= n // 3 + ceil((n/3)-(n//3))
	allbook.append([fandomobj,range(1,nSlides),nSlides])
	params={'allbook':allbook}
	return render(request,"bookshow.html",params)
def reviewbook(request):
	id=request.GET.get('id')
	obj=Bookshelf.objects.get(id=id)
	user1=request.user.email
	userdetails=User.objects.get(email=user1)
	if request.method == 'POST':
		star_rating=request.POST.get('rating')
		item_review=request.POST.get('item_review')
		saveobj=review(user=userdetails,item=obj,rating=star_rating,review_desp=item_review)
		saveobj.save()
		robj = review.objects.filter(item=obj)
		context = {'reviews': robj}
		return render(request, "reviewpage.html",context)
	robj = review.objects.filter(item=obj)
	context = {'reviews': robj}
	return render(request, "reviewpage.html",context)
	
		