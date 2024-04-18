from django.urls import path
from customer.views import CustomerSignup,Customerlogin

urlpatterns = [
   
    path("",CustomerSignup.as_view()),
    path("login/",Customerlogin.as_view(),name="log-in"),

    #  path("signup/",signup),

]