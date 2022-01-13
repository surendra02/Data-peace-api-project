from rest_framework.pagination import LimitOffsetPagination
class MyLimiPagination(LimitOffsetPagination):
    default_limit = 5
