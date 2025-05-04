from django.urls import path
from certification.apps import CertificationConfig
from certification.views import CertificationCreateView, CertificationListView, CertificationDetailView, \
    CertificationDeleteView, CertificationUpdateView

app_name = CertificationConfig

urlpatterns = [
    path('create_cert/', CertificationCreateView.as_view(), name='create_cert'),
    path('', CertificationListView.as_view(), name='list_cert'),
    path('detail_cert/<int:pk>', CertificationDetailView.as_view(), name='detail_cert'),
    path('delete_cert/<int:pk>', CertificationDeleteView.as_view(), name='delete_cert'),
    path('update_cert/<int:pk>', CertificationUpdateView.as_view(), name='update_cert'),
]
