from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..managers import SystemObjectManager
from ..utility import ENTITY_MAPPING


class MapView(APIView):
    def get(self, request):
        if not request.GET.get('id') or not request.GET.get('id').isdigit():
            return Response({'error': 'Valid id is required'}, status=status.HTTP_400_BAD_REQUEST)
        if not SystemObjectManager.check_if_systemobject_exists_by_id(int(request.GET['id'])):
            return Response({'error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
        entities = ENTITY_MAPPING['map']['manager'].get_object_mapping_by_id(int(request.GET['id']))
        return Response(entities)

    def post(self, request):
        serializer = ENTITY_MAPPING['map']['serializer'](data=request.data)
        if serializer.is_valid():
            entity = serializer.save()
            if entity:
                return Response(entity.to_representation(), status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
