from django.urls import path

from .controller import AprendizListCreateView, AprendizDetailView

urlpatterns = [
    path("", AprendizListCreateView.as_view(), name="aprendiz-list-create"),
    path("<int:id>/", AprendizDetailView.as_view(), name="aprendiz-detail"),
]
