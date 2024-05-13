import base64

from django.core.files.base import ContentFile
from django.utils import timezone
from django.db.models import Sum
from rest_framework import serializers

from api.organizations.serializers import GetOrganizationSerializer
from api.users.serializers import GetUserSerializer
from api.tasks import task_send_email_message
from collects.models import Collect


class Base64ImageField(serializers.ImageField):
    """Сериализатор для картики."""
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
        return super().to_internal_value(data)


class GetCollectSerializer(serializers.ModelSerializer):
    """Модель Collect."""
    collected_amount = serializers.SerializerMethodField()
    author = GetUserSerializer()
    organization = GetOrganizationSerializer()
    check_peoples = serializers.SerializerMethodField()

    class Meta:
        fields = "__all__"
        model = Collect

    def get_collected_amount(self, obj):
        return obj.payments.aggregate(
            Sum('invest_amount')
        ).get('invest_amount__sum')

    def get_check_peoples(self, obj):
        return obj.payments.values('user').distinct().count()


class CreateCollectSerializer(serializers.ModelSerializer):
    """Создание/обновление Collect."""
    image = Base64ImageField(required=True, allow_null=False)

    class Meta:
        model = Collect
        exclude = ("create_date")
        read_only_fields = ("author", "create_date", "collect")

    def validate_close_date(self, value):
        if value and value <= timezone.now():
            raise serializers.ValidationError(
                'Дата завершения сбора не может быть меньше даты создания.'
            )
        return value

    def create(self, validated_data):
        collect = Collect.objects.create(**validated_data)
        task_send_email_message(
                subject="Денежный сбор создан.",
                message="Денежный сбор успешно создан.",
                email=[self.context["request"].user.email],
        )
        return collect
