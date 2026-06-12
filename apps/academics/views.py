from rest_framework import generics, permissions
from rest_framework import serializers
from .models import TermMark, Subject

# --- Serializers ---
class SubjectSerializer(serializers.ModelSerializer):
    name_display = serializers.CharField(source='get_name_display', read_only=True)

    class Meta:
        model = Subject
        fields = ['id', 'name', 'name_display']

class TermMarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = TermMark
        fields = ['id', 'subject', 'percentage', 'term', 'year']

    def validate_percentage(self, value):
        if value < 0 or value > 100:
            raise serializers.ValidationError("Percentage must fall between 0 and 100.")
        return value

    def create(self, validated_data):
        # Automatically tie mark data to the authenticated requesting student profile
        request = self.context.get('request')
        validated_data['profile'] = request.user.profile
        return super().create(validated_data)

# --- Views ---
class TermMarkListCreateView(generics.ListCreateAPIView):
    serializer_class = TermMarkSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Scope return values explicitly to the logged-in student profile context
        return TermMark.objects.filter(profile=self.request.user.profile).select_related('subject')