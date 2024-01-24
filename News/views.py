from django.shortcuts import render, redirect
from django.views import View


from .forms import NewsForm
from .models import News, LikeNews, Haqida
from User.models import User


# class OpenNews(View):
# 	def get(self, request, id):
# 		news = News.objects.get(id=id)
# 		return render(request, 'opennews.html', {'news':news})


class Haqida(View):
	def get(self, request):
		# haqida = Haqida.objects.all()
		return render(request, 'about.html')


class CreateNews(View):
	def get(self, request):
		form = NewsForm()
		return render(request, 'create.html', {'form':form})

	def post(self, request):
		form = NewsForm(data=request.POST, files=request.FILES)
		if form.is_valid():
			form.save()
			return redirect('home')
		return render(request, 'create.html', {'form':form})


class EditNews(View):
	def get(self, request, id):
		news = News.objects.get(id=id)
		form = NewsForm(instance=news)
		return render(request, 'create.html', {'form':form})

	def post(self, request, id):
		news = News.objects.get(id=id)
		form = NewsForm(instance=news, data=request.POST, files=request.FILES)
		if form.is_valid():
			# user = form.cleaned_data['user']
			# user = News.objects.create(
			# 	user=request.user
            # )
			form.save()
			return redirect('home')
		return render(request, 'create.html', {'form':form})


class DeleteNews(View):
	def get(self, request, id):
		news = News.objects.get(id=id)
		news.delete()
		return redirect('home')
