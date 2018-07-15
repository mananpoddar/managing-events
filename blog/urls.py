from django.conf.urls import url
from blog import views
app_name = "blog"

urlpatterns = [
    url(r'^formpage/', views.form_name_view, name='form_name'),
    url(r'^signup/', views.authentication_view, name='authentication_name'),
    url(r'^main_page/', views.main_page, name='main_page'),
    url(r'^logout/', views.user_logout, name='user_logout'),
    
    
    url(r'^user_login/', views.user_login, name='user_login'),
   
   
]
