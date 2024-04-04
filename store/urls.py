
from django.urls import path
from app import views
from django.contrib import admin


urlpatterns = [
        path('admin/', admin.site.urls),
        path("", views.LandingPage.as_view(), name="landing"),
    path("posting-vehicle", views.PostVehicle.as_view(), name="post-vehicle"),
    path("car-page/<id>/", views.VehicleSale.as_view(), name="car-page"),
    path("buy-vehicle", views.BuyingVehicle.as_view(), name="buy-vehicle"),
    path("receipt", views.VehicleReceipt.as_view(), name="receipt"),
    path("receipt-page/<id>/", views.ViewingReceipt.as_view(), name="view-receipt"),
     path('index',views.index,name='index'),
    path('prediction',views.prediction,name='prediction'),
]



