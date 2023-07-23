from collections import OrderedDict
from rest_framework import serializers

from .models import (Department, Employee,)


# Here I give this class the name of TheAmazingField you can name it whatever you want

class TheAmazingField(serializers.PrimaryKeyRelatedField):

    def __init__(self,serializer, many=False,*args,**kwargs) -> None:
        super().__init__(*args,**kwargs)
        self.serializer = serializer
        self.many=many

    # When read data we need all the serialized object not only the Id
    def to_representation(self,value):
        return self.serializer(instance=value, many=self.many).data

    """
    I use a small but not mandatory trick to help you reduce typing:
    make sure the queryset of the serialized model is automatically
    inherited. I am very lazy
    """
    def get_queryset(self):
        if self.queryset:
            return self.queryset
        return self.serializer.Meta.model.objects.all()

    """
    Get choices is used by the DRF autodoc and expects to_representation()
    to return an ID, which causes everything to crash.
    We rewrite the trick to use item.pk instead of to_representation()
    """
    def get_choices(self, cutoff=None):
        queryset = self.get_queryset()
        if queryset is None:
            return {}

        if cutoff is not None:
            queryset = queryset[:cutoff]

        return OrderedDict([
            (
                item.pk,
                self.display_value(item)
            )
            for item in queryset
        ])

        """
        DRF skips certain validations when there is only the id,
        and as this is not the case here, everything crashes. We disable this.
        """
    def use_pk_only_optimization(self):
        return False

class DepartmentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Department
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    department = TheAmazingField(serializer=DepartmentSerializer)
    class Meta:
        model = Employee
        fields = '__all__'