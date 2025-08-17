from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json

from rest_framework_simplejwt.tokens import RefreshToken

from .models import Student, Organizer, Attendant

def index(request):
    return render(request,'login/index.html')

def get_token(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        username = data.get('username')
        password = data.get('password')
        role = data.get('role')
        gender = data.get('gender')
        age = data.get('age')

        if User.objects.filter(username=username).exists():
            return JsonResponse({'error': 'The ID have been used.'}, status=100)

        user = User.objects.create_user(username=username, password=password)

        if role == 'student':
            Student.objects.create(user=user, gender=gender, age=age)
        elif role == 'organizer':
            Organizer.objects.create(user=user)
        elif role == 'attendant':
            Attendant.objects.create(user=user)
        else:
            return JsonResponse({'error': 'invalid character'}, status=101)

        tokens = get_token(user)
        return JsonResponse({
            'message': 'Successful!',
            'id': user.id,
            'role': role,
            'tokens': tokens
        })

    return JsonResponse({'error': 'POST only'}, status=102)


@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            role = None
            if hasattr(user, 'student'):
                role = 'student'
            elif hasattr(user, 'organizer'):
                role = 'organizer'
            elif hasattr(user, 'attendant'):
                role = 'attendant'

            tokens = get_token(user)
            return JsonResponse({
                'message': 'Successful!',
                'id': user.id,
                'role': role,
                'tokens': tokens
            })
        else:
            return JsonResponse({'error': 'Wrong username or password.'}, status=103)

    return JsonResponse({'error': 'POST only'}, status=102)

#error 102 POST only , 103 Wrong username or password. , 101 invalid character , 100 The ID have been used.