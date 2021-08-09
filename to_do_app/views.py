from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from . models import *
from . serializers import *
from django.core.paginator import Paginator #import Paginator


def movies(request):
	movies = Movie.objects.all() #queryset containing all movies we just created
	paginator = Paginator(movies, 3)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	return render(request=request, template_name="main/movies.html", context={'movies':page_obj})
# Create your views here.


@api_view(['GET'])
def task_ki_yadi(request):
    task_objs = task.objects.all()
    paginator = Paginator(task_objs, 3)
    print(paginator)
    page_number = request.data.get('page')
    print("********88",page_number)
    page_obj = paginator.get_page(page_number)
    print("*********4444444444",page_obj)
    serializer = taskSerializer(page_obj,many=True)
    print(serializer)
    return Response(serializer.data)



@api_view(['POST'])
def task_create(request):
    if request.method=="POST":

        serializer = taskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            # return Response(serializer.data)
            return Response({"status":200, "message":"your data got added","data":serializer.data})
        else:
            return Response({
                'status': 'Bad request',
                'message': serializer.errors,
            }, status=status.HTTP_400_BAD_REQUEST)
            # return Response({"errors":serializer.errors,
            #             "status":status.HTTP_400_BAD_REQUEST})

@api_view(['GET','PUT','PATCH','DELETE'])
def task_details(request,pk):
    try:
        task_obj = task.objects.get(pk=pk)
    except task.DoesNotExist:
        return Response({"data":"data doesnot exist for this id" },status=status.HTTP_400_BAD_REQUEST)

    if request.method =="GET":
        serializer = taskSerializer(task_obj)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer =taskSerializer(task_obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    elif request.method=="PATCH":
        serializer =taskSerializer(task_obj,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    elif request.method =="DELETE":
        task_obj.delete()
        return Response("data got deleetd")


class task_list(APIView):
    def get(self, request):
        task_obj = task.objects.all()
        serializer =taskSerializer(task_obj, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = taskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class task_detail(APIView):
    def get_object(self, pk):
        try:
            return task.objects.get(pk=pk)
        except task.DoesNotExist:
             raise Http404


    def get(self, request, pk ):
        task = self.get_object(pk)
        serializer = taskSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk):
        task= self.get_object(pk)
        serializer = taskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        task= self.get_object(pk)
        serializer = taskSerializer(task, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def delete(self, request, pk, format=None):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)