from django.contrib import admin
from .models import User, Interest, Product

admin.site.register(User)
admin.site.register(Interest)
admin.site.register(Product)

from .models import Video
admin.site.register(Video)
