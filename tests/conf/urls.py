from django.urls import include, path


urlpatterns = [path("", include("tests.books.urls"))]
