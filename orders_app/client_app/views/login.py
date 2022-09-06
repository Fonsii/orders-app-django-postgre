from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

class Login(View):


    def get(self, request):
        if User.objects.filter(pk=request.user.id).exists():
            return redirect('index')
        else:
            return render(request, 'client_app/register.html', {})


    def post(self, request):
        print(request.user.id)
        username = request.POST.get('username')
        user = User.objects.get(pk=request.user.id)
        user.username = username
        user.save()
        return render(request, 'client_app/login.html', {})