from django.db import models


class Note(models.Model):
    title = models.CharField(blank=True, max_length=50)
    text = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title[:30]

# sample data
# [
#     {id: 1, title: "Hello!", text: "Hello!"},
#     {id: 2, title: "My first note", text: "Something"},
#     {id: 3, title: "My second note", text: "Something"},
#     {id: 4, title: "My third note", text: "Something"},
#     {id: 5, title: "My fourth note", text: "Something"}
# ]
