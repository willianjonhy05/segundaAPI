from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import User, Todo
from .serialiezer import MyTokenObtainPairSerielizer, RegisterSerielizer, TodoSerielizer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerielizer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = RegisterSerielizer


@api_view(["GET"])
def getRoutes(request):
    routes = ["/loginapi/token/", "/loginapi/register/", "/loginapi/token/refresh/"]
    return Response(routes)

@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def testEndPoint(request):
    if request.method == "GET":
        data = f"Parabéns {request.user}, sua API respondeu a sua solicitação GET"
        return Response({"response": data}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        text = "Hello buddy"
        data = f"Parabéns {request.user}, sua API respondeu ao seu POST request com o texto: {text}"
        return Response({"response": data}, status=status.HTTP_200_OK)
    return Response({}, status.HTTP_400_BAD_REQUEST)


class TodoListView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerielizer

    def get_queryset(self):    
        user_id = self.kwargs['user_id']
        user = User.objects.get(id=user_id)
        todo = Todo.objects.filter(user=user)
        return todo


class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerielizer

    def get_object(self):
        user_id = self.kwargs["user_id"]
        todo_id = self.kwargs["todo_id"]

        user = User.objects.get(id=user_id)
        todo = Todo.objects.get(id=todo_id, user=user)
        return todo



class TodoMarkAsCompleted(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerielizer


    def get_object(self):
        user_id = self.kwargs["user_id"]
        todo_id = self.kwargs["todo_id"]

        user = User.objects.get(id=user_id)
        todo = Todo.objects.get(id=todo_id, user=user)

        todo.completed = True
        todo.save()
        return todo

def index(request):
    return HttpResponse('')