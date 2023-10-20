from django.urls import path,include
from . import views
#import obtain_auth_token view
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    # path('', views.index, name='home'),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token),
]
