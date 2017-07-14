
from rest_framework import serializers
from polls.models import Users, Company
from rest_framework.utils.representation import serializer_repr



class Companyserializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ('Name', 'Address')


class Usersserializer(serializers.ModelSerializer):
    company = Companyserializer()


    class Meta:
        model = Users
        fields = ('Name', 'Role', 'company')