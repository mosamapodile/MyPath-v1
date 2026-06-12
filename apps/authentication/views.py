from rest_framework import generics, permissions
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .models import StudentProfile
from rest_framework import serializers

User = get_user_model()

# --- Serializers ---
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

class StudentProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = StudentProfile
        fields = ['id', 'user', 'grade', 'province', 'xp_points', 'level']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        password = user_data.pop('password')
        
        # Create standard User instance securely
        user = User.objects.create_user(**user_data, password=password)
        
        # Instantiate matching Student Profile
        profile = StudentProfile.objects.create(user=user, **validated_data)
        return profile

# --- Views ---
class StudentRegisterView(generics.CreateAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer
    permission_classes = [permissions.AllowAny]

class StudentProfileView(generics.RetrieveAPIView):
    serializer_class = StudentProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # Dynamically yield profile matching current bearer token context
        return self.request.user.profile