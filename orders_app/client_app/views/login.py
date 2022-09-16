from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
class Login(View):
    def get(self, request):
        if User.objects.filter(pk=request.user.id).exists():
            return redirect('index')
        else:
            return render(request, 'client_app/register.html', {})