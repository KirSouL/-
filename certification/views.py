from django.shortcuts import render
from django.forms import inlineformset_factory
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import CreateView, DetailView, ListView, DeleteView, UpdateView
from django.urls import reverse_lazy, reverse

from certification.forms import CertificationForm, TechForm
from certification.models import Certification


class CertificationCreateView(CreateView):
    model = Certification
    form_class = CertificationForm
    success_url = reverse_lazy('certification:certification_list')
    # permission_required = "catalog.add_product"

    def form_valid(self, form):
        product = form.save()
        product.owner = self.request.user
        product.save()
        return super().form_valid(form)


class CertificationUpdateView(UpdateView):
    model = Certification
    form_class = CertificationForm
    success_url = reverse_lazy('certification:certification_list')

    def tech(request):
        if request.method == 'POST':
                form = TechForm(request.POST)
                if form.is_valid():
                    technical_devices = form.cleaned_data.get('technical_devices')

        else:
            form = TechForm

            return render('certification_detail.html', {'detail_certification': form})

    # def get_context_data(self, **kwargs):
    #     context_data = super().get_context_data(**kwargs)
    #     VersionFormset = inlineformset_factory(Certification, extra=1)
    #     if self.request.method == 'POST':
    #         context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
    #     else:
    #         context_data['formset'] = VersionFormset(instance=self.object)
    #     return context_data

    # def tech(request, pk):
    #     ins = Certification.objects.get(pk=pk)
    #
    #     form = TechForm(instance=ins)
    #     if request.method == 'POST':
    #         form = form(request.POST, instance=ins)
    #         if form.is_valid():
    #             form.save()

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)

    # def get_form_class(self):
    #     user = self.request.user
    #     if (user.has_perm("catalog.set_info_product") and user.has_perm("catalog.set_category_product") and
    #             user.has_perm("catalog.set_published_status")):
    #         return ProductModeratorForm
    #     if user == self.object.owner:
    #         return ProductForm
    #     raise PermissionDenied


class CertificationListView(ListView):
    model = Certification

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        return context_data


class CertificationDetailView(DetailView):
    model = Certification


class CertificationDeleteView(DeleteView):
    model = Certification
    success_url = reverse_lazy('certification:certification_list')


# def countries_view(request):
#     if request.method == 'POST':
#         form = CountryForm(request.POST)
#         if form.is_valid():
#             countries = form.cleaned_data.get('countries')
#             # do something with your results
#     else:
#         form = CountryForm
#
#     return render_to_response('render_country.html', {'form': form},
#                               context_instance=RequestContext(request))

# #model.py
# class ClassName(models.Model):
#     field_name = models.CharField(max_length=100)
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         if self.field_name:
#             self.field_name= eval(self.field_name)
#
#
#
# #form.py
# CHOICES = [('pi', 'PI'), ('ci', 'CI')]
#
# class ClassNameForm(forms.ModelForm):
#     field_name = forms.MultipleChoiceField(choices=CHOICES)
#
#     class Meta:
#         model = ClassName
#         fields = ['field_name',]
#
# #view.py
# def viewfunction(request, pk):
#     ins = ClassName.objects.get(pk=pk)
#
#     form = ClassNameForm(instance=ins)
#     if request.method == 'POST':
#         form = form (request.POST, instance=ins)
#         if form.is_valid():
#             form.save()
#             ...