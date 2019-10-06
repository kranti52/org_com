from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..utility import ENTITY_MAPPING


class InformationalSystemView(APIView):

    def get(self, request, entity_type):
        if not entity_type or entity_type not in ENTITY_MAPPING:
            return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        entities = ENTITY_MAPPING[entity_type]['manager'].filter_object_data(request.GET.copy())
        return Response(entities)

    def post(self, request, entity_type):
        if not entity_type or entity_type not in ENTITY_MAPPING:
            return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        serializer = ENTITY_MAPPING[entity_type]['serializer'](data=request.data)
        if serializer.is_valid():
            entity = serializer.save()
            if entity:
                return Response(entity.to_representation(), status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, entity_type, id=None):
        if not id or not entity_type or entity_type not in ENTITY_MAPPING:
            return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        entity = ENTITY_MAPPING[entity_type]['manager'].get_object_by_id(id)
        if not entity:
            return Response({'error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
        entity.delete()

        return Response({'success': True})

    def put(self, request, entity_type, id=None):
        if not id or not entity_type or entity_type not in ENTITY_MAPPING:
            return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        entity = ENTITY_MAPPING[entity_type]['manager'].get_object_by_id(id)
        if not entity:
            return Response({'error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ENTITY_MAPPING[entity_type]['serializer'](data=request.data, instance=entity)
        if serializer.is_valid():
            entity = serializer.save()
            if entity:
                return Response(entity.to_representation(), status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
