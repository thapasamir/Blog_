from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('blog',views.BlogView.as_view()),
    path('blog/<int:pk>/',views.BlogView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
