from django.urls import path
import route_planner.views


app_name = 'route_planner'


urlpatterns = [
    path('', route_planner.views.PlannerView.as_view(),
         name='planner'),
    path('<str:system>', route_planner.views.SystemView.as_view(),
         name='system'),
    path('report/', route_planner.views.ReportView.as_view(),
         name='report'),
]
