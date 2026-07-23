from django.urls import path

from library.views.dashboard_views import DashboardAPIView

urlpatterns = [
    path("", DashboardAPIView.as_view(), name="dashboard"),
]