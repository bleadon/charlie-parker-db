from django.contrib import admin
from . models import Session, Key, SongForm, Song, Version
# Register your models here.

# admin.site.register(Song)
# admin.site.register(Track)
class SessionAdmin(admin.ModelAdmin):
    search_fields = ['title', 'date', 'location', 'personnel', 'album_releases']

class VersionAdmin(admin.ModelAdmin):
    search_fields = ['version_title', 'notes', 'session__title', 'session__location']

admin.site.register(Session, SessionAdmin)
admin.site.register(Key)
admin.site.register(SongForm)
admin.site.register(Song)
admin.site.register(Version, VersionAdmin)
