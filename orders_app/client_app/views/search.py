from django.views.generic import View
from django.shortcuts import render


class Search(View):

    def get(self, request):
        try:
            print(request.GET['q'])
        except:
            print("no search query")
        return render(request, 'client_app/search.html', {})
