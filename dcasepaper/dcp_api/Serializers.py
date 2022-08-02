from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField
from .models import *
from rest_framework_bulk import (BulkListSerializer,BulkSerializerMixin)


class PatientProfileserializer(serializers.ModelSerializer):

    class Meta:
        model=PatientProfile
        fields='__all__'


#--------Patient Medical Profile model serializers----------
class PatientMedicalProfileSerializer(serializers.ModelSerializer):
    id= serializers.IntegerField(required=False)

    class Meta:
        model=PatientMedicalProfile
        fields=['id',
                'Patient',
                'P_Habbit',
                'P_LevelOfHygins',
                'P_CosmeticConcern',
                'P_MedicalHistory',
                ]
        read_only_fields=('Patient',)
#------End Patient Medical Profile Model Serializer-----------------


