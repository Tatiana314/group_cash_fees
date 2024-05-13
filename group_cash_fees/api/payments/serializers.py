from rest_framework import serializers

from api.users.serializers import GetUserSerializer
from api.tasks import task_send_email_message
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
        read_only_fields = ("user", "create_date", "collect")
        model = Payment

    def create(self, validated_data):
        payment = Payment.objects.create(**validated_data)
        task_send_email_message(
                subject="Платеж создан.",
                message="Платеж успешно создан.",
                email=[self.context["request"].user.email],
        )
        return payment
