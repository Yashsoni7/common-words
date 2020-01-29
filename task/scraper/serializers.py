from rest_framework import serializers
from .models import common_word

class common_words_serializer(serializers.ModelSerializer):
    class Meta:
        model = common_word
        fields = ['word','freq','url']