from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from api.models import Note
from api.serializers import NoteSerializer


class NoteAPIList(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    # permission_classes = (IsAuthenticated, )


class NoteAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    # permission_classes = (IsAuthenticated, )
