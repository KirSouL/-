from django.contrib import admin
from certification.models import Certification, BranchOffice


@admin.register(BranchOffice)
class BranchOfficeAdmin(admin.ModelAdmin):
    list_display = (
        'branch_office',
        'department',
        'position',
        'kvd',
    )
    list_filter = (
        'branch_office',
        'department',
        'kvd',
    )
    search_fields = (
        'branch_office',
        'kvd',
    )


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = (
        'office',
        'first_name',
        'patronymic',
        'last_name',
        'birth_date',
        'method',
        'type_certification',
        'objects_ntd',
        'technical_devices',
        'start_date',
        'end_date',
    )
    list_filter = (
        'office',
        'method',
        'type_certification',
    )
    search_fields = (
        'office',
        'first_name',
        'patronymic',
        'last_name',
        'method',
        'type_certification',
    )

