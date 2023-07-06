from django.contrib import admin

from api.models import Note


class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'updated', 'user')


admin.site.register(Note, NoteAdmin)
