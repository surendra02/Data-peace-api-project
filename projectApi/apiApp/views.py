from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from .mypagination import MyLimiPagination
from django_filters.rest_framework import DjangoFilterBackend


@api_view(['GET', 'POST'])
def saveOrAllData(request):
    """"This function is responsible to fetch all records with GET method and insert a record with POST method"""
    if request.method == "GET":
        data = Employee.objects.all()
        serializer = EmployeeSerializer(data, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(request.data)
        else:
            return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def singleData(request, eid):
    """This function is responsible to find a record(GET),update a record(PUT) and also delete a record(DELETE)"""
    try:
        record = Employee.objects.get(id=eid)
    except:
        return Response({'status': status.HTTP_404_NOT_FOUND, 'data': 'Record not found!!'})

    if request.method == "GET":
        serializer = EmployeeSerializer(record)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = EmployeeSerializer(record, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        record.delete()
        return Response("Record has been deleted!!")


# This class is responsible to search data by first_name,last_name with pagination and limits
class EmployeeList(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['first_name', 'last_name']
    pagination_class = MyLimiPagination
