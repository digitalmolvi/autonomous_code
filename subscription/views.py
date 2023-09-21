from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import login, authenticate
from .models import UserMembership, Subscription, Membership
from django.contrib.auth import get_user_model  # Import the User model

from .serializers import RegisterSerializer
from django.contrib.auth.hashers import make_password
User = get_user_model()  # Get the User model for the current project


def home(request):
    return render(request, 'index.html')


def index(request):
    user_membership = UserMembership.objects.get(user=request.user)
    subscriptions = Subscription.objects.filter(
        user_membership=user_membership).exists()
    if not subscriptions:
        return redirect('sub')
    else:
        subscription = Subscription.objects.filter(
            user_membership=user_membership).last()
        return render(request, 'home.html', {'sub': subscription})


def signin(request):
    return render(request, 'login.html')


def check_mail_ajax(request):
    if request.is_ajax():
        email = request.GET.get('email', None)
        check_email = User.objects.filter(email=email).exists()
        if check_email:
            response = {'error': 'Email already exists.'}
        else:
            response = {'success': 'Cool'}
        return JsonResponse(response)
    else:
        response = {'error': 'Error Email Checking.'}
        return JsonResponse(response)


class Register(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            obj = serializer.save()
            password = make_password(serializer.data['password'])
            User.objects.filter(email=serializer.data['email']).update(
                password=password)
            get_membership = Membership.objects.get(membership_type='Free')
            instance = UserMembership.objects.create(
                user=obj, membership=get_membership)
            return Response({'success': 'Registration successful.'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Login(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = User.objects.filter(email=email).first()
        if not user:
            return Response({'error': 'No account with such email'}, status=status.HTTP_400_BAD_REQUEST)

        if not user.check_password(password):
            return Response({'error': 'Password is not correct. Try again'}, status=status.HTTP_400_BAD_REQUEST)

        log_user = authenticate(email=email, password=password)
        if log_user is not None:
            login(request, log_user)
            return Response({'success': 'Login successful'})
        else:
            return Response({'error': 'Invalid email/password. Try again later.'}, status=status.HTTP_400_BAD_REQUEST)


def subscription(request):
    return render(request, 'index.html')
