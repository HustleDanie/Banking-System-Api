from rest_framework import serializers
from useraccount.models import(
    Bank
)
class NewBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ['bank', 'bank_address']


    def create(self, validated_data):
        return super().create(validated_data)
    
    