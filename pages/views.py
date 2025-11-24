from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView): # new
    template_name = 'pages/home.html'

class ContactPageView(TemplateView): # new
    template_name = 'pages/contact.html'

class AboutPageView(TemplateView): # new
    template_name = 'pages/about.html'


class HelpPageView(TemplateView): # new
    template_name = 'pages/help.html'


class ServicePageView(TemplateView): # new
    template_name = 'pages/services.html'


class TermAndConditionPageView(TemplateView): # new
    template_name = 'pages/term_and_condition.html'