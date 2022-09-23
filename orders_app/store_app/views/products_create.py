from django.views.generic import View
from django.shortcuts import render, redirect
from store_app.models import Product, ProductsStore, Store
from store_app.forms import ProductForm


class ProductsCreateView(View):
    def get(self, request):
        if request.user.is_staff:
            if not Store.objects.filter(store=request.user).exists():
                self.create_store(request)
            context = self.create_context(request)
            return render(request, 'store_app/products_create.html', context)
        else:
            return redirect('index')

    
    def post(self, request):
        if request.user.is_staff:
            if not Store.objects.filter(store=request.user).exists():
                self.create_store(request)
            
            form = ProductForm(request.POST)
            if form.is_valid():
                form.save()
                added_product = Product.objects.get(ref=form.cleaned_data['ref'], name=form.cleaned_data['name'], description=form.cleaned_data['description'])

                store = Store.objects.get(store=request.user)
                ProductsStore.objects.create(store=store, product=added_product)
            return redirect('index')
        else:
            return redirect('index')

    
    def create_context(self, request):
        form = ProductForm()
        
        context = {
            'product_form': form,
            'title': 'Add product',
            'my_products': True
        }

        return context
    

    def create_store(self, request):
        store = Store(store=request.user, location='N/A')
        store.save()
