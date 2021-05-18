"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from app import views

urlpatterns = [
    path('', views.login, name='login'),
    path('register', views.register, name='register'),
    path('admin/', admin.site.urls),
    path('gameStore', views.store, name='store'),
    path('library', views.library, name='library'),
    path('inventory', views.inventory, name='inventory'),
    path('marketplace', views.marketplace, name='marketplace'),

    path('library/<int:game_instance_id>', views.library_game, name='library_game'),
    path('library/<int:game_instance_id>/create_badge', views.create_badge, name='create_badge'),
    path('marketplace_detail/<int:collectible_id>', views.marketplace_detail, name='marketplace_detail'),
    path('marketplace_detail/<int:collectible_id>/buy_offer/<int:offer_id>/<int:user_id>', views.buy_offer, name='buy_offer'),
    path('myaccount/<int:user_id>', views.user_detail, name='user_detail'),
    path('gameStore/<int:game_id>', views.store_game, name='store_game'),
    path('gameStore/<int:game_id>/buy_store_game/<int:user_id>', views.buy_store_game, name='buy_store_game'),
    path('inventory/<int:collectible_instance_id>', views.inventory_collectible, name='inventory_collectible'),
    path('inventory/<int:collectible_instance_id>/removeOffer/<int:offer_id>', views.remove_offer, name='remove_offer'),

]
