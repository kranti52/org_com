from .managers import IssueManager
from .managers import MapManager
from .managers import MetricManager
from .managers import ProductManager
from .models import Issue
from .models import Map
from .models import Metric
from .models import Product
from .serializers import IssueSerializer
from .serializers import MapSerializer
from .serializers import MetricSerializer
from .serializers import ProductSerializer

ENTITY_MAPPING = {
    'product': {
        'model': Product,
        'manager': ProductManager,
        'serializer': ProductSerializer
    },
    'issue': {
        'model': Issue,
        'manager': IssueManager,
        'serializer': IssueSerializer
    },
    'metric': {
        'model': Metric,
        'manager': MetricManager,
        'serializer': MetricSerializer
    },
    'map': {
        'model': Map,
        'manager': MapManager,
        'serializer': MapSerializer
    },
}
