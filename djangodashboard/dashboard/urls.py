from django.urls import path
from dashboard import views
from rest_framework.routers import DefaultRouter
# from dashboard.views import HeaderViewSet

urlpatterns = [
    path('',views.dashboard),
    # path('headerlist/', views.header_list),
    # path('header/create/',views.create_header),
    # path('header/update/<int:pk>/',views.update_header),
    # path('header/delete/<int:pk>',views.delete_header),

]
# router = DefaultRouter()
# router.register(r'header',views.HeaderViewSet, basename='header')
# urlpatterns = router.urls