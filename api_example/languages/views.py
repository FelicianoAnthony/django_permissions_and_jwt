from django.shortcuts import render
from rest_framework import viewsets#, permissions 
from .models import Language, Programmer, Paradigm 
from .serializers import LanguageSerializer, ParadigmSerializer, ProgrammerSerializer

# automatically handles basic http requests rather than defining everything explicity
# inherit modelsviewset 
# covers case for all objects or specific objects 
class LanguageView(viewsets.ModelViewSet):
	queryset = Language.objects.all()
	serializer_class = LanguageSerializer
	#permission_classes = (permissions.IsAuthenticatedOrReadOnly,) # only want logged in users to edit or add 


class ParadigmView(viewsets.ModelViewSet):
	queryset = Paradigm.objects.all()
	serializer_class = ParadigmSerializer



class ProgrammerView(viewsets.ModelViewSet):
	queryset = Programmer.objects.all()
	serializer_class = ProgrammerSerializer

