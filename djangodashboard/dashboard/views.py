from django.shortcuts import render
from .models import Header
from .serializers import HeaderSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
def dashboard(request):
    return render(request,'dashboard/index.html')

# class HeaderViewSet(viewsets.ModelViewSet):
#     serializer_class= HeaderSerializer
#     queryset = Header.objects.all()


@api_view(['GET'])
def header_list(request):
    header = Header.objects.all()
    serializer = HeaderSerializer(header, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_header(request):
    serializer = HeaderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT', 'PATCH'])
def update_header(request, pk):
    header = Header.objects.get(pk=pk)
    serializer = HeaderSerializer(instance=header, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_header(request, pk):
    header = Header.objects.get(pk=pk)
    header.delete()
    return Response(status=204)


