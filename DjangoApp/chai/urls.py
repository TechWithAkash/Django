from django.urls import path
from . import views

# locahost:8000/chai
# localhost:8000/chai/order

urlpatterns = [
    path('',views.all_chai,name='all_chai'),
    # path('order/',views.order,name='all_home'),
    path('<int:chai_id>',views.chai_detail,name='chai_detail'),
    path('chai_stores/',views.chai_store_view,name='chain_stores'),
    

]
