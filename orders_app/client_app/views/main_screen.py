from django.views.generic import View
from django.shortcuts import render
class MainScreen(View):
    def get(self, request):
        context = self.create_context()
        return render(request, 'client_app/index.html', context)

    
    def create_context(self):
        return {
            'title': 'Main Screen',
            'home': True
        }