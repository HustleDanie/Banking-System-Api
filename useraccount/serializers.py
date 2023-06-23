from rest_framework import serializers
from allbanks.models import Bank
from useraccount.models import(
    CustomUser,
    UserTransactions
)
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

    
class NewAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'bank',
            'first_name',
            'last_name',
            'other_name',
            'password',
            'email',
            'image',
            'gender',
            'phone',
            'address'
        ]
    
        extra_kwargs ={
            'password':{
                'write_only': True
            },
            'email':{
                'write_only': True
            },
            'image':{
                'write_only':True
            },
            'password':{
                'min_length': 8,
                'write_only': True
            }
        }
    def create(self, validated_data):
        user= CustomUser.objects.create_user(**validated_data)
        acc_number = validated_data["phone"][1:11]
        user.acc_number = acc_number
        user.save()
        return user
    def to_representation(self, instance):
        data= super().to_representation(instance)
        data["Your account number:"]= instance.acc_number
        data["info"]= f"Thank you for creating account with us{instance.first_name} {instance.last_name} {instance.other_name}"
        return data
    
class LogInSerializer(TokenObtainPairSerializer):
    ...

class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "image", "other_name", 'email']

        extra_kwargs = {
            "image": {
                "required" : False
                }
        }   
        
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
    

class GetBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['account_balance']
    
class AllUserTransactionsSerializer(serializers.ModelSerializer):
    receiver_account_number = serializers.CharField(max_length=10, required=True)
    transaction = serializers.CharField(max_length=10, required=True)
    class Meta:
        model = UserTransactions
        fields=["bank","amount","receiver_account_number","transaction"]

    def validate(self, data):
        receiver_acc_no = CustomUser.objects.filter(acc_number=data["receiver_account_number"])
        bank = Bank.objects.filter(id=data['bank'].id)

        if receiver_acc_no.exists() and bank.exists():
            return data
        
        else:
            raise serializers.ValidationError({
                "error-message":f"Pls recheck the account or bank provided."
            })
        
    def create(self, validated_data):

        if validated_data["transaction"] == "save":
            sender = CustomUser.objects.get(id=self.context['request'].user.id)
            receiver = CustomUser.objects.get(acc_number=validated_data['receiver_account_number'])

            if sender.acc_number == validated_data['receiver_account_number']:
                print('reached here')
                sender.account_balance+= validated_data['amount']
                sender.save()
                print('***', sender.account_balance)
            else:
                receiver.account_balance+= validated_data['amount']
                receiver.save()
            UserTransactions.objects.create(

                                            amount=validated_data["amount"],
                                            sender= self.context['request'].user,
                                            receiver_account_number=validated_data['receiver_account_number'],
                                            bank=validated_data['bank'],
                                            transaction=validated_data["transaction"]
                                     )
            return validated_data
        elif validated_data["transaction"]=="withdraw":
            sender= CustomUser.objects.get(id=self.context['request'].user.id)

            if sender.account_balance < validated_data["amount"]:
                raise serializers.ValidationError({
                    "info": "INSUFFICIENT FUNDS"})
            else:
                sender.account_balance -= validated_data['amount']
                sender.save()
                validated_data["amount_left"]=f"You have {sender.account_balance}left"
                UserTransactions.objects.create(
                                             amount=validated_data["amount"],
                                             sender=self.context['request'].user,
                                             receiver_account_number=validated_data["receiver_account_number"],
                                             bank= validated_data["bank"],
                                             transaction = validated_data["transaction"]
                               )
        return validated_data

class AllMadeTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTransactions
        fields = ["amount","bank","receiver_account_number","transaction"]

