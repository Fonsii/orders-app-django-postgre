from django.views.generic import View
from django.shortcuts import render, redirect
from store_app.models import Product, ProductsStore, Store
from django.core.paginator import Paginator

class ProductsListView(View):
    def get(self, request):
        if request.user.is_staff:
            if not Store.objects.filter(store=request.user).exists():
                self.create_store(request)
            context = self.create_context(request)
            return render(request, 'store_app/products_list.html', context)
        else:
            return redirect('index')

    
    def create_context(self, request):
        store = Store.objects.get(store=request.user)
        products_store_relation = ProductsStore.objects.filter(store=store)
        products = Product.objects.filter(id__in=products_store_relation.values('product')).order_by('name')

        results = self.get_paginator_results(products, request.GET.get('page'))
        
        context = {
            'results': results,
            'title': 'My Products',
            'my_products': True
        }

        return context
    

    def create_store(self, request):
        store = Store(store=request.user, location='N/A')
        store.save()


    def get_paginator_results(self, results, page_number):
        if results is not None:
            if page_number is None:
                page_number = 1

            paginator = Paginator(results, 4)
            page_display = paginator.get_page(page_number)
            return page_display
        return results

