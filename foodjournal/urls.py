# from inventory import views 
# from rest_framework import routers
from django.urls import path
from foodjournal import views
from django.urls import path, include


#Routers to provide an easy way of automatically determinging URL conf
# router = routers.SimpleRouter()
# router.register('users', UserViewSet)

#Wire API by using automatic URL routing
urlpatterns = [
    # path('admin/', admin.site.urls),    
    path('foodjournal/', views.food_journal_entry_list),
    path('foodjournal/<int:pk>/', views.food_journal_entry_detail),
    path('food/', views.food_log_item_list),
    path('food/<int:pk>', views.food_log_item_detail),
    path('user/', views.user_list),
    path('user/<int:pk>', views.user_detail),

]
