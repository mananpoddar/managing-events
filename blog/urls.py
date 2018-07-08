from django.conf.urls import url
from blog import views
app_name = "blog"

urlpatterns = [
    url(r'^formpage/', views.form_name_view, name='form_name'),
    url(r'^users/', views.authentication_view, name='authentication_name'),
    url(r'^main_page/', views.main_page, name='main_page'),

    
    
    url(r'^user_login/', views.user_login, name='user_login'),
   
   
]
