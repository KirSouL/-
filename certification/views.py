from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import CreateView, DetailView, ListView, DeleteView, UpdateView
from django.urls import reverse_lazy, reverse

from certification.models import Certification


class CertificationCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    pass
    # model = Certification
    # form_class = CedrtificateForm
    # success_url = reverse_lazy("catalog:product_list")
    # permission_required = "catalog.add_product"
    #
    # def form_valid(self, form):
    #     product = form.save()
    #     product.owner = self.request.user
    #     product.save()
    #     return super().form_valid(form)


class CertificationUpdateView(LoginRequiredMixin, UpdateView):
    pass
    # model = Product
    # success_url = reverse_lazy("catalog:product_list")
    #
    # def get_context_data(self, **kwargs):
    #     context_data = super().get_context_data(**kwargs)
    #     VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
    #     if self.request.method == 'POST':
    #         context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
    #     else:
    #         context_data['formset'] = VersionFormset(instance=self.object)
    #     return context_data
    #
    # def form_valid(self, form):
    #     formset = self.get_context_data()['formset']
    #     self.object = form.save()
    #     if formset.is_valid():
    #         formset.instance = self.object
    #         formset.save()
    #
    #     return super().form_valid(form)
    #
    # def get_form_class(self):
    #     user = self.request.user
    #     if (user.has_perm("catalog.set_info_product") and user.has_perm("catalog.set_category_product") and
    #             user.has_perm("catalog.set_published_status")):
    #         return ProductModeratorForm
    #     if user == self.object.owner:
    #         return ProductForm
    #     raise PermissionDenied


class CertificationListView(ListView):
    pass
    # model = Product
    #
    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context_data = super().get_context_data(**kwargs)
    #     for product in context_data["object_list"]:
    #         current_version = Version.objects.filter(product=product, is_version=True)
    #         product.current_version = current_version
    #     return context_data
    #
    # def form_valid(self, form):
    #     forms = self.get_context_data()['current_version']
    #     self.object = form.save()
    #     if forms.is_valid():
    #         forms.instance = self.object
    #         forms.save()
    #
    #     return super().form_valid(form)

    # def get_queryset(self):
    #     return get_products()


class CertificationDetailView(DetailView):
    pass
    # model = Certification


class CertificationDeleteView(LoginRequiredMixin, DeleteView):
    model = Certification
    success_url = reverse_lazy('certification:list_cert')
