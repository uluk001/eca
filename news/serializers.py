from rest_framework import serializers
from news.models import News, NewImages

class NewsSerializer(serializers.ModelSerializer):
    content = serializers.SerializerMethodField()
    content_ru = serializers.SerializerMethodField()
    content_en = serializers.SerializerMethodField()


    class Meta:
        model = News
        fields = '__all__'


    def get_content(self, obj):
        return str(obj.content.html)
    
    def get_content_ru(self, obj):
        return str(obj.content_ru.html)
    
    def get_content_en(self, obj):
        return str(obj.content_en.html)


class NewImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewImages
        fields = ('image',)

