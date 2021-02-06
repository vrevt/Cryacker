from django.contrib import admin
from django.utils.translation import ugettext as _


class CryackerAdminSite(admin.AdminSite):
    site_header = _("Cryacker Administration")
    site_title = _("Cryacker Administration")
    index_title = _("Welcome to Cryacker Administration")
    site_url = '/dashboard/'
    enable_nav_sidebar = False
