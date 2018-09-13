from rest_framework import serializers

from institutions.models import Institution, InstitutionType
from common.serializers import  AbstractFieldsMixin

class InstitutionTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = InstitutionType
        fields = '__all__'


class InstitutionTypeInlineSerializer(serializers.ModelSerializer):

    class Meta:
        model = InstitutionType
        fields = ('id', 'name','levels')

class InstitutionSerializer(AbstractFieldsMixin, serializers.ModelSerializer):


    def create(self, validated_data):
        institution = super(InstitutionSerializer, self).create(validated_data)

        if institution.type == 'High School':
            for i in range(4):
                ClassLevel.objects.create()

        user = self.context['request'].user
        user.institution = institution
        user.is_admin = True
        user.save()

        institution.save()

        return institution

    def update(self, institution, validated_data):
        institution = super(InstitutionSerializer, self).update(institution, validated_data)
        institution.created_by.institution = institution
        institution.save()

        return institution

    class Meta:
        model = Institution
        fields = '__all__'


class InstitutionInlineSerializer(AbstractFieldsMixin, serializers.ModelSerializer):
    type = InstitutionTypeInlineSerializer(read_only=True)
    class Meta:
        model = Institution
        fields = ('id', 'created_by','type', 'name', 'website', 'motto', 'logo', 'domain')



