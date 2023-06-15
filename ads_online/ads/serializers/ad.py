from rest_framework import serializers

from ads.models import Ad


class AdListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ad
        fields = 'id', 'title'


class AdCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ad
        fields = '__all__'

    def create(self, validate_data):
        ad = super().create(validate_data)
        ad.author = self.context['request'].user
        ad.save()

        return ad


class AdDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ad
        fields = '__all__'


class AdDeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ad
        fields = '__all__'


class AdUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ad
        fields = ['title', 'price', 'description']
