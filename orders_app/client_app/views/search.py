from django.views.generic import View
from django.shortcuts import render
from store_app.models import Product, ProductsStore
from django.core.paginator import Paginator

class Search(View):
    def get(self, request):
        #try:
        context = self.create_context(request)
        return render(request, 'client_app/search.html', context)
        # except:
        #     print("Error in search")
        #     return render(request, 'client_app/search.html')


    def create_context(self, request):
        results_search = self.get_results(request.GET['q'], 'product')
        page_display = self.get_paginator_results(results_search, request.GET.get('page', 1))

        context = {
            'results': page_display,
            'title': 'Search results for ' + request.GET['q'],
            'search': True,
            'last_search': request.GET['q']
        }

        return context

    def get_results(self, query_search, type):
        if type == 'product':
                results = Product.objects.filter(name__icontains=query_search)
                return ProductsStore.objects.filter(product__in=results).order_by('product__name')
        elif type == 'category':
            pass

    
    def get_paginator_results(self, results, page_number):
        print(page_number)
        if results is not None:
            paginator = Paginator(results, 4)
            page_display = paginator.get_page(page_number)
            return page_display
        return results
