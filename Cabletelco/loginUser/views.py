from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class Index(LoginRequiredMixin, TemplateView):
    """
    funcion principal del aplicativo
    """

    template_name = 'index.html'
