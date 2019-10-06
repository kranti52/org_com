from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from ..managers import MapManager
from ..managers import SystemObjectManager
from ..models import Map


class MapSerializer(serializers.ModelSerializer):
    first_object_id = serializers.IntegerField(required=True)
    second_object_id = serializers.IntegerField(required=True)

    def create(self, validated_data):
        validation_error = {}
        if validated_data['first_object_id'] == validated_data['second_object_id']:
            validation_error['non_field_errors'] = [" Mapping id's shouldn't be same. "]
        if not SystemObjectManager.check_if_systemobject_exists_by_id(
                validated_data['first_object_id']) and not validation_error:
            validation_error['first_id'] = [" First id object doesn't exists. "]
        if not SystemObjectManager.check_if_systemobject_exists_by_id(
                validated_data['second_object_id']) and not validation_error:
            validation_error['second_id'] = [" Second id object doesn't exists. "]
        if MapManager.check_if_mapping_exists_by_id(
                validated_data['first_object_id'], validated_data['second_object_id']) \
                and not validation_error:
            validation_error['non_field_errors'] = [
                "The fields first_object_id, second_object_id must make a unique set."]
        if validation_error:
            raise serializers.ValidationError(validation_error)

        map = Map.objects.create(**validated_data)
        return map

    class Meta:
        model = Map
        fields = ('first_object_id', 'second_object_id')
        validators = [
            UniqueTogetherValidator(
                queryset=Map.objects.all(),
                fields=['first_object_id', 'second_object_id']
            )
        ]
