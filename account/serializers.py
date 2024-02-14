# from rest_framework import serializers
# from account.models import Student, CustomUser

# class CustomUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ['email', 'first_name', 'last_name', 'role', 'mobile']

# class StudentCreateSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField(write_only=True)
#     first_name = serializers.CharField(write_only=True)
#     last_name = serializers.CharField(write_only=True)
#     role = serializers.CharField(write_only=True)
#     mobile = serializers.CharField(write_only=True)
#     password = serializers.CharField(write_only=True, style={'input_type': 'password'})

#     class Meta:
#         model = Student
#         fields = ['id', 'email', 'first_name', 'last_name', 'role', 'mobile', 'password', 'batch_year', 'branch', 'admission_no']
    
#     def create(self, validated_data):
#         data = {
#             'email': validated_data.pop('email'),
#             'first_name': validated_data.pop('first_name'),
#             'last_name': validated_data.pop('last_name'),
#             'role': validated_data.pop('role'),
#             'mobile': validated_data.pop('mobile'),
#         }

#         user = CustomUser.objects.create(**data)
#         user.set_password(validated_data.pop('password'))  # Set the password securely
#         user.save()

#         student = Student.objects.create(user=user, **validated_data)
        
#         return student



# class StudentSerializer(serializers.ModelSerializer):
#     user = CustomUserSerializer()

#     class Meta:
#         model = Student
#         fields = "__all__"
