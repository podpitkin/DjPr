from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect

from catalog.forms import ProductForm
from catalog.models import Product


class CatalogListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'
    paginate_by = 12

    def get_queryset(self):
        return Product.objects.all().order_by('category', 'name')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:prod_list')

    def form_valid(self, form):
        product = form.save(commit=False)
        product.owner = self.request.user
        product.save()
        return redirect(self.success_url)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'

    def test_func(self):
        product = self.get_object()
        return product.owner == self.request.user

    def get_success_url(self):
        return reverse_lazy('catalog:prod_detail', kwargs={'pk': self.object.pk})


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:prod_list')

    def test_func(self):
        product = self.get_object()
        return product.owner == self.request.user or self.request.user.has_perm('catalog.delete_product')


class ProductUnpublishView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'catalog.can_unpublish_product'

    def post(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=kwargs['pk'])
        product.is_published = False
        product.save()
        return redirect('catalog:prod_detail', pk=product.pk)