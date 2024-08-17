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
    def save(self, **kwargs):
        self.is_valid(raise_exception=True)
        user = HikeUser.objects.filter(email=self.validated_data.get('email'))

        if user.exists():
            return user.first()
        else:
            new_user = HikeUser.objects.create(
                email=self.validated_data.get('email'),
                phone=self.validated_data.get('phone'),
                fam=self.validated_data.get('fam'),
                name=self.validated_data.get('name'),
                otc=self.validated_data.get('otc'),
            )
            return new_user

    class Meta:
        model = HikeUser
        fields = ['email', 'phone', 'fam', 'name', 'otc']


class PerevalSerializer(serializers.ModelSerializer):
    # add_time = serializers.DateTimeField(format='%d-%m-%Y %H:%M:%S', read_only=True)
    user = HikeUserSerializer()
    coords = CoordsSerializer(allow_null=True)
    level = LevelSerializer(allow_null=True)
    images = ImageSerializer(many=True)

    # status = serializers.CharField(read_only=True)

    class Meta:
        model = Pereval
        fields = ['id', 'beauty_title', 'title', 'other_titles', 'connect',
                  'add_time', 'status', 'user', 'coords', 'level', 'images']
        read_only_fields = ['status', 'add_time']

    def create(self, validated_data, **kwargs):
        user = validated_data.pop('user')
        coords = validated_data.pop('coords')
        level = validated_data.pop('level')
        images = validated_data.pop('images')
        user, created = HikeUser.objects.get_or_create(**user)
        coords = Coords.objects.create(**coords)
        level = Level.objects.create(**level)
        pereval = Pereval.objects.create(**validated_data, user=user, coords=coords, level=level, status='new')

        for img in images:
            image = img.pop('image')
            title = img.pop('title')
            Image.objects.create(image=image, pereval=pereval, title=title)
        return pereval
