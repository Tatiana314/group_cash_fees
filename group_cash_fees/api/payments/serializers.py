from django.core.mail import send_mail
from rest_framework import serializers

from api.users.serializers import GetUserSerializer
from payments.models import Payment


class GetPaymentSerializer(serializers.ModelSerializer):
    """Чтение Payment."""
    invest_amount = serializers.SerializerMethodField()
    user = GetUserSerializer()

    class Meta:
        fields = (
            "user",
            "comment",
            "create_date",
            "invest_amount",
        )
        model = Payment

    def get_invest_amount(self, obj):
        if obj.public:
            return obj.invest_amount


class CreatePaymentSerializer(serializers.ModelSerializer):
    """Создание Payment."""
    class Meta:
        exclude = ("create_date",)
        read_only_fields = ("author", "create_date")
        model = Payment

    def create(self, validated_data):
        payment = Payment.objects.create(**validated_data)
        send_mail(
                subject="Платеж создан.",
                message="Платеж успешно создан.",
                from_email="sredawork@gmail.com",
                recipient_list=[self.context["request"].user.email],
                fail_silently=True
        )
        return payment
