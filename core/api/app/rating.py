# from rest_framework import serializers
# from core.models import Rating
# from rest_framework import generics

# class RatingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Rating
#         fields = '__all__'

# class RatingCreateAPIView(generics.CreateAPIView):
#     serializer_class = RatingSerializer

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
#         product = serializer.validated_data['product']
#         product.update_average_rating()
