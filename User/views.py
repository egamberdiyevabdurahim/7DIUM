from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.views import View

from .models import User
from .forms import UserForm, SignInForm
from News.models import LikeNews, News


class SignUp(View):
	def get(self, request):
		form = UserForm()
		return render(request, 'signup.html', {'form':form})

	def post(self, request):
		form = UserForm(data = request.POST, files = request.FILES)
		if form.is_valid():
			form.save()
			return redirect('home')
		return render(request, 'signup.html', {'form':form})


class SignIn(View):
	def get(self, request):
		form = SignInForm()
		return render(request, 'signin.html', {'form':form})

	def post(self, request):
		form = SignInForm(data = request.POST)
		if form.is_valid():
			username=request.POST.get('username')
			password=request.POST.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('home')
		return render(request, 'signin.html', {'form':form})


class LogOut(View):
	def get(self, request):
		logout(request)
		return redirect('home')


class LikeNews(View):
	def post(self, request, id):
		news = News.objects.get(id=id)
		if LikeNews.objects.filter(news=news):
			like = LikeNews.objects.filter(news=news).first()
			if request.user in like.user.all():
				like.user.remove(request.user)
				return redirect('home')
			like.user.add(request.user)
			return redirect('home')
		like = LikeNews.objects.create(
				news=news
			)
		like.user.add(request.user)
		return redirect('home')
