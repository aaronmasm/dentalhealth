from django.views.generic import TemplateView

# Create your views here.


class HomePageView(TemplateView):
    template_name = "pages/home.html"


class AboutUsPageView(TemplateView):
    template_name = "pages/about-us.html"


class ServicesPageView(TemplateView):
    template_name = "pages/services.html"


class SpecialtiesPageView(TemplateView):
    template_name = "pages/specialties.html"


class DentistsPageView(TemplateView):
    template_name = "pages/dentists.html"


class ClinicsPageView(TemplateView):
    template_name = "pages/clinics.html"
