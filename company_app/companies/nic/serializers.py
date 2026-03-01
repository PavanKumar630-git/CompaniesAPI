from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)


class LoginResponseSerializer(serializers.Serializer):
    status = serializers.BooleanField()
    access_token = serializers.CharField()
    refresh_token = serializers.CharField()
    username = serializers.CharField()