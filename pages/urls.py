from django.urls import path

from .views import HomePageView, AboutUsPageView, ServicesPageView, SpecialtiesPageView, DentistsPageView, \
    ClinicsPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about-us/", AboutUsPageView.as_view(), name="about-us"),
    path("services/", ServicesPageView.as_view(), name="services"),
    path("specialties/", SpecialtiesPageView.as_view(), name="specialties"),
    path("dentists/", DentistsPageView.as_view(), name="dentists"),
    path("clinics/", ClinicsPageView.as_view(), name="clinics"),
]
