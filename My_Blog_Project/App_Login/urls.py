from django.urls import path
from App_Login import views

app_name = 'App_Login'

urlpatterns=[
     path('sign_up/', views.sign_up, name='sign_up'),
     path('log_in/', views.log_in, name='log_in'),
     path('log_out/', views.log_out, name='log_out'),
     path('profile/', views.profile, name='profile'),
     path('user_change/', views.user_change, name='user_change'),
     path('password/', views.pass_change, name='pass_change'),
     path('add_pro_pic/', views.add_pro_pic, name='add_pro_pic'),
     path('change_pro_pic/', views.change_pro_pic, name='change_pro_pic'),
]
