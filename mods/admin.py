from django.contrib import admin
from .models import Mod, Game, ModTag, ModImage
# Register your models here.

admin.site.register(Mod)
admin.site.register(Game)
admin.site.register(ModTag)
admin.site.register(ModImage)