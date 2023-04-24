from django.contrib import admin
from api.models import Note


class NoteAdmin(admin.ModelAdmin):
    pass


admin.site.register(Note, NoteAdmin)
