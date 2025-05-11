from django.urls import path
from certification.apps import CertificationConfig
from certification.views import CertificationCreateView, CertificationListView, CertificationDetailView, \
    CertificationDeleteView, CertificationUpdateView

app_name = CertificationConfig.name

urlpatterns = [
    path('create_certification/', CertificationCreateView.as_view(), name='create_certification'),
    path('', CertificationListView.as_view(), name='certification_list'),
    path('detail_certification/<int:pk>', CertificationDetailView.as_view(), name='detail_certification'),
    path('delete_certification/<int:pk>', CertificationDeleteView.as_view(), name='delete_certification'),
    path('update_certification/<int:pk>', CertificationUpdateView.as_view(), name='update_certification'),
]
