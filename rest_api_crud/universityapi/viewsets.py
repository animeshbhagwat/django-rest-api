from rest_framework import viewsets, filters
from . import models
from . import serializers

class UniversityViewset(viewsets.ModelViewSet):
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    queryset = models.Univeristy.objects.all()
    serializer_class = serializers.UniversitySerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        country_code = str(self.request.query_params.get('country_code', ''))
        
        if country_code:
            return queryset.filter(alpha_two_code=country_code)
        
        return queryset
