from typing import Any, Dict
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, View
from django.views.decorators.cache import cache_page
from django.http import HttpRequest, HttpResponse


from .models import Technology, Project, Experience, File
from .forms import ContactForm


class HomeView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs: None) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context['cv'] = get_object_or_404(File, name='cv').file.url
        context['technologies'] = Technology.objects.filter(visible=True).order_by('priority')
        context['projects'] = Project.objects.prefetch_related('images').order_by('priority')
        context['experiences'] = Experience.objects.all().order_by('-start')
        context['form'] = ContactForm()

        return context


class ProjectDetailView(TemplateView):
    template_name = 'pages/project_detail.html'

    def get_context_data(self, **kwargs: int) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context['project'] = get_object_or_404(Project, id=kwargs.get('id'))

        return context


class ContactView(View):
    template_name = 'home.html'

    def get(self, request: HttpRequest) -> HttpResponse:
        form = ContactForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request: HttpRequest) -> HttpResponse:
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, self.template_name, {'form': form})
