from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, Categories, Like, DisLike, CartItem
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login , logout, authenticate
from django.contrib import messages
from .forms import NewUserForm

def buy_Skyrim(request):
	return HttpResponse("""<h1>DEMO VERSION!!!</h1>
							<a href ="http://127.0.0.1:8000/shop/">Shop</a>""")
def Bethesda(request):
		return render(request, "store/home.html", {'News' : Product.objects.all})

def show_categories(request):
	return render(request, "store/categories.html",{'cat': Categories.objects.all})

def separator(request, url_slug):
	categories_urls = [c.url_slug for c in Categories.objects.all()]
	if url_slug in categories_urls:
		posts = Product.objects.filter(news_category__url_slug = url_slug)
		return render(request, "store/s_category.html",{'posts': posts})

	if url_slug in [c.url_slug for c in Product.objects.all()]:	
		game = Product.objects.get(url_slug = url_slug)
		if request.GET.get('like'):
			if request.user.is_authenticated:
				if request.GET.get('like') == "1":
					Like.objects.update_or_create(user = request.user, liked=game) 
				if request.GET.get('like') == "0":
					DisLike.objects.update_or_create(user = request.user, disliked=game)
		like_count = Like.objects.filter(liked = game).count()
		dislike_count = DisLike.objects.filter(disliked = game).count()
		try:
			likedis = like_count + dislike_count
			like_percent = round((like_count / likedis) * 100)
			dislike_percent = 100 - like_percent
		except ZeroDivisionError:
			return render(request, "store/s_games.html",{'game': game})

		return render(request, "store/s_games.html",{'game': game, 
			                                         'like_per':like_percent})


	return HttpResponse("Error 404")

def _Registration(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request,user)
			return redirect("Store:home")
		else:
			for msg in form.error_messages:
				messages.error(request, f"{msg}:{form.error_messages[msg]}")
	form = NewUserForm
	return render(request, "store/registration.html", {"form" : form})

def logout_(request):
	logout(request)
	messages.info(request, "ЦЕ ВИ! Hапевно...")
	return redirect("Store:home")

def login_(request):
	if request.method =="POST":
		form = AuthenticationForm(request = request, data = request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username = username, password = password)
			if user is not None:
				login(request, user)
				messages.success(request, f"Привіт {username}")
				return redirect("Store:home")
			else:
				messages.info(request, f"""Що це таке {username} ?, або неправильний пароль)""")
		else:
			messages.error(request, f"""Неправильне ім'я або пароль""")
	form = AuthenticationForm
	return render(request, "store/login.html", {"form" : form})

def Ubisoft(request, number):
	return HttpResponse("""<h1>Lol you are %s</h1>""" % number)

def buying_cart(request):
	user = request.user
	if request.method =="POST":
		p = request.POST.get('product_id')
		product_id = int(p)
		product = Product.objects.get(id = product_id)
		CartItem.objects.update_or_create(product = product, user = user)
		products = [item for item in user.cartitem_set.all()]
		
	else:
		products = [item for item in user.cartitem_set.all()]
	return render(request, "store/s_cart.html",{"user" : user, "products" : products})	
