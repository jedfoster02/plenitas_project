from django.contrib import admin
from .models import User, Interest, Product

admin.site.register(User)
admin.site.register(Interest)
admin.site.register(Product)

from .models import Video

from import_export.admin import ImportExportModelAdmin
from .models import Video

@admin.register(Video)
class VideoAdmin(ImportExportModelAdmin):
    pass

from import_export.admin import ImportExportModelAdmin

from import_export.admin import ImportExportModelAdmin
from .models import ViewingHistory

@admin.register(ViewingHistory)
class ViewingHistoryAdmin(ImportExportModelAdmin):
    list_display = ('user', 'video', 'watched_at')

