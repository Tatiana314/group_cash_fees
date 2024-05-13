from django.contrib import admin

from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'type', 'collect', 'invest_amount', 'create_date',
        'comment', 'public'
    )
