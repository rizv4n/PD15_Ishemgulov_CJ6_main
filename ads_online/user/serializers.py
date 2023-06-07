from rest_framework import serializers

from ads_online.user.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validate_data):
        user = super().create(validate_data)

        user.set_password(user.password)
        user.save()

        return user
