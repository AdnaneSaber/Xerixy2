from django.shortcuts import render
from .serializers import TaskSerializer
from .models import Task
from rest_framework.views import APIView
from rest_framework import status
from django.db import connection
from rest_framework.response import Response
import json


class TasksView(APIView):
    def get(self, request, id, *args, **kwargs):
        if not id:
            todos = Task.objects.all()
            serializer = TaskSerializer(todos, many=True)
        else:
            todos = Task.objects.filter(id=id)
            serializer = TaskSerializer(todos, many=True)
        return Response(serializer.data)

    def delete(self, request, id, *args, **kwargs):
        todos = Task.objects.filter(id=id).delete()
        return Response(status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = TaskSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id, *args, **kwargs):
        if id:
            body = json.loads(request.body)
            newState = body['done']
            if str(newState).lower() == 'false':
                newState = False
            elif str(newState).lower() == 'true':
                newState = True
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            with connection.cursor() as cursor:
                cursor.execute(f"""
                    update tasks_task set done = {newState} where id = {id} """)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


def index(request):
    return render(request, "build/index.html", {})
