from django.urls import path

from tests.books.views import view


urlpatterns = [path(route="", view=view, name="simple-view")]
