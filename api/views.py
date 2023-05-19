from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from api.models import Note
from api.serializers import NoteSerializer
from rest_framework.authtoken.models import Token


class NoteAPIList(generics.ListCreateAPIView):
    def get_queryset(self):
        return Note.objects.filter(user=self.request.user.id)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    # permission_classes = (IsAuthenticated, )


class NoteAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    # permission_classes = (IsAuthenticated, )
