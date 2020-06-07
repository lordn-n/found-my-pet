from . import views
from django.urls import path

urlpatterns = [
    path('s<int:pet_id>', views.scan, name='QR scan'),

    path('report', views.create_report, name='Reports'),
    path('report/<int:report_id>', views.show_report, name='Found Report'),
]
