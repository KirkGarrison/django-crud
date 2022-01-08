from django.urls import path
from .views import SnackListView
from .views import AboutPageView
from .views import SnackDetailView
from .views import SnackCreateView
from .views import SnackDeleteView
from .views import SnackUpdateView

urlpatterns = [
    path('', SnackListView.as_view(), name='snack_list'),
    path('<int:pk>/', SnackDetailView.as_view(), name='snack_detail'),
    path('create/', SnackCreateView.as_view(), name='snack_create'),
    path('<int:pk>/delete/', SnackDeleteView.as_view(), name='snack_delete'),
    path('<int:pk>/update/', SnackUpdateView.as_view(), name='snack_update'),
    path('about/', AboutPageView.as_view(), name='about')
]