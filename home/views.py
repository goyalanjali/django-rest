from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import TodoSerializer
from .models import Todo
from rest_framework.views import APIView
from rest_framework import status, viewsets
from rest_framework.decorators import action
from .serializer import TimingTodoSerializer
from .models import TimingTodo

# Create your views here.

@api_view()
def get_appi(request):
    return Response({'name': 'anjali', 'status': 'han'})


@api_view(['POST'])
def post_todo(request):
    try:
        data = request.data
        serializer = TodoSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            print(data)
            return Response(
                {
                    'status' : True,
                    'message' : 'Success Data',
                    'data' : serializer.data
                }
            )

        return Response(
                {
                    'status' : False,
                    'message' : 'Invalid Data',
                    'data' : serializer.data
                }
            )    

       
        

    except Exception as e:
        print(e)
        return Response(
                {
                    'status' : False,
                    'message' : 'Something went wrong'
                }
            )       


@api_view(['PATCH'])
def patch_todo(request):
    try:
        data = request.data  
        if not data.get('uid'):
            return Response(
                {
                    'status' : False,
                    'message' : 'uid required',
                    'data' : {}
                }
            )

        obj = Todo.objects.get(uid = data.get('uid'))    
        serializer = TodoSerializer(obj, data = data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'status' : True,
                    'message' : 'Success Data',
                    'data' : serializer.data
                }
            )

        return Response(
                {
                    'status' : False,
                    'message' : 'Invalid data',
                    'data' : serializer.errors
                }
            )

    except Exception as e:
        print(e)
        return Response(
                {
                    'status' : False,
                    'message' : 'Invalid uid',
                    'data' : {}
                }
            )       


#All the methods inside one class instead of creating different classes
class TodoView(APIView):
   def get(self, request):
      return Response({'name': 'anjali', 'status': 'han'})


   def post(self, request):
    try:
        data = request.data
        serializer = TodoSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            print(data)
            return Response(
                {
                    'status' : True,
                    'message' : 'Success Data',
                    'data' : serializer.data
                }
            )

        return Response(
                {
                    'status' : False,
                    'message' : 'Invalid Data',
                    'data' : serializer.data
                }
            )    

       
        

    except Exception as e:
        print(e)
        return Response(
                {
                    'status' : False,
                    'message' : 'Something went wrong'
                }
            ) 

            
   def patch(self, request):
      try:
        data = request.data  
        if not data.get('uid'):
            return Response(
                {
                    'status' : False,
                    'message' : 'uid required',
                    'data' : {}
                }
            )

        obj = Todo.objects.get(uid = data.get('uid'))    
        serializer = TodoSerializer(obj, data = data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'status' : True,
                    'message' : 'Success Data',
                    'data' : serializer.data
                }
            )

        return Response(
                {
                    'status' : False,
                    'message' : 'Invalid data',
                    'data' : serializer.errors
                }
            )

      except Exception as e:
        print(e)
        return Response(
                {
                    'status' : False,
                    'message' : 'Invalid uid',
                    'data' : {}
                }
            )       

          
  


# with APIView we get only few methods, but with viewset we can create customized methods as well in same class
class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    @action(detail=False, methods=['post'])
    def add_date_to_todo(self, request):
        try:
            data = request.data
            serializer = TimingTodoSerializer(data = data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                {
                    'status' : True,
                    'message' : 'Success Data',
                    'data' : serializer.data
                }
            )

            return Response(
                {
                    'status' : False,
                    'message' : 'Invalid data',
                    'data' : serializer.errors
                }
            )

        except Exception as e:
            print(e)
            return Response(
                    {
                        'status' : False,
                        'message' : 'Invalid uid',
                        'data' : {}
                    }
                )      


    @action(detail=False, methods=['get'])
    def get_timing(self, request): 
        objs = TimingTodo.objects.all()
        serializer = TimingTodoSerializer(objs, many = True)     
        return Response(
                {
                    'status' : True,
                    'message' : 'Timing Todo Fetched',
                    'data' : serializer.data
                }
            )     




