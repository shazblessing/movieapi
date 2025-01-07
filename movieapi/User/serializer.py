from django.contrib.auth.models import User
from rest_framework import serializers


# The `UserSerializer` class serializes user data including followers and following relationships,
# with methods to retrieve followers and following lists and create a new user instance.
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]

    def create(self, validated_data):

        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )

        return user
