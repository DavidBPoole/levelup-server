# """levelup URL Configuration

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/4.1/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """

# from django.contrib import admin
# from django.urls import path
# from django.conf.urls import include
# from rest_framework import routers
# from levelupapi.views import GameTypeView, GameView, EventView, GamerView, register_user, check_user

# router = routers.DefaultRouter(trailing_slash=False)
# router.register(r'gametypes', GameTypeView, 'gametype')
# router.register(r'games', GameView, 'game')
# router.register(r'events', EventView, 'event')
# router.register(r'gamers', GamerView, 'gamer')

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include(router.urls)),
#     path('register', register_user),
#     path('checkuser', check_user),
# ]

# 11/17/2023 code:
# from django.urls import path
# from levelupapi.views import register_user, check_user

# urlpatterns = [
#     path('register', register_user),
#     path('checkuser', check_user),
# ]

# # Requests to http://localhost:8000/register will be routed to the register_user function
# path('register', register_user)
# # Requests to http://localhost:8000/checkuser will be routed to the login_user function
# path('checkuser', check_user),

# To run the server:
# python manage.py runserver

# **********************************************************************************************
# Old Setup Below:
# """levelup URL Configuration

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/4.1/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.contrib import admin
# from django.urls import path
# from django.conf.urls import include
# from rest_framework import routers
# from levelupapi.views import GameTypeView, GameView, EventView, GamerView


# router = routers.DefaultRouter(trailing_slash=False)
# router.register(r'gametypes', GameTypeView, 'gametype')
# router.register(r'games', GameView, 'game')
# router.register (r'events', EventView, 'event')
# router.register (r'gamers', GamerView, 'gamer')

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include(router.urls)),
# ]

# alternate code 2:
"""levelup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls import include
from rest_framework import routers
from levelupapi.views import GameTypeView, GameView, EventView, GamerView
from django.urls import path
from levelupapi.views import register_user, check_user

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'gametypes', GameTypeView, 'gametype')
router.register(r'games', GameView, 'game')
router.register(r'events', EventView, 'event')
router.register(r'gamers', GamerView, 'gamer')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('register', register_user),
    path('checkuser', check_user),
]
