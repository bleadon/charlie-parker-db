from django.urls import path, re_path
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('search/', views.SearchPageView.as_view(), name='search'),
    path('search_results/', views.SearchResultsView.as_view(), name='search_results'),
    re_path(r'^version_detail/(?P<pk>\d+)/$', views.VersionDetailView.as_view(), name="version_detail"),
]
