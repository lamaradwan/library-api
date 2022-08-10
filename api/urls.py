from django.urls import path

from .views import QuoteListView, QuoteDetailView

urlpatterns = [
    path('', QuoteListView.as_view(), name = 'things_list'),
    path('<int:pk>/', QuoteDetailView.as_view(), name = 'things_detail'),
]