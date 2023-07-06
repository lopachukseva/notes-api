from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from api.models import Note
from api.serializers import NoteSerializer


class NoteAPIList(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user.id)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class NoteAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user.id)
