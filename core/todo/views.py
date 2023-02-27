from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Todo
# Create your views here.


class TodoView(APIView):

    def get(self, request):
        # creating coustomize get method here
        response = {'status': 500, 'message': 'Something went wrong'}
        # response['status'] = 500
        # response['message'] = 'Something went wrong'
        try:
            todo_objs = Todo.objects.all()
            payload = []
            for todo_obj in todo_objs:
                payload.append({
                    'todo_name': todo_obj.todo_name,
                    'todo_description': todo_obj.todo_description,
                    'is_completed': todo_obj.is_completed,
                })
            response = {'status': 200, 'message': 'Completed', 'data': payload}

        except Exception as e:
            print(f'An exception occurred: {e}')
        return Response(response)

    def post(self, request):
        response = {'status': 500, 'message': 'Failed'}
        try:
            data = request.data
            todo_name = data.get('todo_name')
            todo_description = data.get('todo_description')
            if todo_name is None or todo_description is None:
                response = {
                    'message': 'todo_name and todo_description are required'}
                raise Exception('todo_name')
            Todo.objects.create(todo_name=todo_name,
                                todo_description=todo_description)
            response = {'status': 200, 'message': 'Success'}

        except Exception as e:
            print(f'An exception occurred {e}')
        return Response(response)

    def put(self, request):
        pass

    def delete(self, request):
        pass
