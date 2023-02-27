from rest_framework.serializers import ModelSerializer
from news.models import News, NewImages

class NewsSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

class NewsSerializerEn(ModelSerializer):
    class Meta:
        model = News
        fields = ('title', 'content', 'main_image')


class NewImagesSerializer(ModelSerializer):
    class Meta:
        model = NewImages
        fields = ('image',)