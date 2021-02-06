from django.contrib.admin.apps import AdminConfig


class CryackerAdminConfig(AdminConfig):
    default_site = 'cryacker.admin.CryackerAdminSite'
