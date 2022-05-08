"""textutil URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from . import views




urlpatterns = [
    path('admin/', admin.site.urls),# shows the admin page
    # path('', views.index,name='index'),# '' means home page
    # path('about',views.about,name="about"), # show the about page
    # path('contact',views.contact,name="contact")
    # path('',views.index,name='index'),
    path('',views.index,name='index'),
    # path('analyze',views.analyze,name='analyze'),
    path('speak',views.speak,name='speak'),
    path('speakme',views.speakme,name='speakme'),
    # path('login/',loginaction,name='login'),
    path('signup/',include('signup.urls')),
    path('login/',include('login.urls')),

    # path('capfirst',views.capfirst,name='capfirst'),
    # path('newlineremove',views.newlineremove,name='newlineremove'),
    # path('spaceremove',views.spaceremove,name='spaceremove'),
    # path('charcount',views.charcount,name='charcount'),

]
