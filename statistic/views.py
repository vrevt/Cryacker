from django.http import HttpResponse
from django.views.generic import TemplateView

from statistic.models import Record


class StatisticList(TemplateView):
    template_name = "statistic/about.html"

