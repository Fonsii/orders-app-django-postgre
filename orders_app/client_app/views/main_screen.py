from django.views.generic import View
from django.shortcuts import render


class MainScreen(View):

    def get(self, request):
        return render(request, 'client_app/index.html', {})
