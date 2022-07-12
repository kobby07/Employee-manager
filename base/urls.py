from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name="home"),
    path('login', views.mylogin, name="login"),
    path('signup', views.signup, name="signup"),
    path('logout', views.log_out, name="logout"),
    path('create-employee', views.create_employee, name='create'),
    path('update-employee/<int:id>', views.update_employee, name='update'),
    path('import-data', views.import_data, name="import")
]
