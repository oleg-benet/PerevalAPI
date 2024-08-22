from .models import Coords, Level, Pereval, Image, HikeUser
from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = ['latitude', 'longitude', 'height']


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ['winter', 'summer', 'autumn', 'spring']


class ImageSerializer(serializers.ModelSerializer):
    image = serializers.URLField()

    class Meta:
        model = Image
        fields = ['image', 'title']


class HikeUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = HikeUser
        fields = ['email', 'phone', 'fam', 'name', 'otc']


class PerevalSerializer(WritableNestedModelSerializer):
    add_time = serializers.DateTimeField(format='%d-%m-%Y %H:%M:%S', read_only=True)
    user = HikeUserSerializer()
    coords = CoordsSerializer(allow_null=True)
    level = LevelSerializer(allow_null=True)
    images = ImageSerializer(many=True)

    class Meta:
        model = Pereval
        fields = ['id', 'beauty_title', 'title', 'other_titles', 'connect',
                  'add_time', 'user', 'coords', 'status', 'level', 'images']
        read_only_fields = ['status', 'add_time']


    def validate(self, data):
        if self.instance:
            db_user = self.instance.user
            data_user = data.get('user')
            if (db_user.email != data_user['email'] or
                db_user.phone != data_user['phone'] or
                db_user.fam != data_user['fam'] or
                db_user.name != data_user['name'] or
                db_user.otc != data_user['otc']):
                raise serializers.ValidationError({'Отклонено': 'Нельзя изменять данные пользователя!'})
        return data
