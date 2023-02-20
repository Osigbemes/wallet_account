from rest_framework import serializers

from .models import UserAccount

class CreateUserAccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = UserAccount
        fields = ('first_name', 'last_name', 'email')
        extra_kwargs = {'accountPassword': {'write_only':True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)
        instance.is_active=True
        instance.save()
        return instance