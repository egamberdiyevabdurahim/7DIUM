"""
URL configuration for Sayt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from .views import Home
from News.views import Haqida, CreateNews, EditNews, DeleteNews
from User.views import SignUp, SignIn, LogOut, LikeNews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='home'),
    path('about/', Haqida.as_view(), name='haqida'),
    path('create/', CreateNews.as_view(), name='create'),
    path('edit/<int:id>', EditNews.as_view(), name='edit'),
    path('delete/<int:id>', DeleteNews.as_view(), name='delete'),
    path('sign-up/', SignUp.as_view(), name='signup'),
    path('sign-in/', SignIn.as_view(), name='signin'),
    path('log-out/', LogOut.as_view(), name='logout'),
    path('like/<int:id>', LikeNews.as_view(), name='like')
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
