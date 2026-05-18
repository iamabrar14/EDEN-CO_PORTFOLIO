from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("portfolio.urls")),
]

# Error handlers for consistent HTTP response codes.
handler404 = "portfolio.views.handler404"
handler500 = "portfolio.views.handler500"
