from django.contrib import admin
from .models import Distributor, User, Game, Collectible, Game_instance, Collectible_instance, Offer
# Register your models here.

admin.site.register(Distributor)
admin.site.register(User)
admin.site.register(Game)
admin.site.register(Collectible)
admin.site.register(Game_instance)
admin.site.register(Collectible_instance)
admin.site.register(Offer)