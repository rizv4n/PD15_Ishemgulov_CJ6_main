from rest_framework import serializers

from ads.models import Comment


class CommentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = 'id', 'text'


class CommentCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'

    def create(self, validate_data):
        comment = super().create(validate_data)
        comment.author = self.context['request'].user
        comment.save()

        return comment


class CommentDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'


class CommentDeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'


class CommentUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['text']
