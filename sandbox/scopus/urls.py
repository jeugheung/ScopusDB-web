from django.urls import path
from .views import *

urlpatterns = [
    path('', about),
    path('about', about),
    path('overview/summary', overviewSummary),
    path('overview/rankings', overviewRankings),
    path('overview/collaboration', overviewCollaboration),
    path('overview/published', overviewPublished),
    path('overview/viewed', overviewViewed),
    path('overview/cited', overviewCited),
    path('news', news),
    path('researchers', researchers),
    path('benchmarking', benchmarking),
]