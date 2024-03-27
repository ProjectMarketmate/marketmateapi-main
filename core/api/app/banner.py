from rest_framework import serializers
from core.models import OfferBanner
from rest_framework import generics


class OfferBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfferBanner
        fields = '__all__'

class OfferBannerListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = OfferBannerSerializer
    queryset = OfferBanner.objects.all()
    

class OfferBannerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OfferBannerSerializer
    queryset = OfferBanner.objects.all()


