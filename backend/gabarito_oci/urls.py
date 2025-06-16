from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include



urlpatterns = [
    # Rota do Admin
    path('admin/', admin.site.urls),
    
    # Rotas de Autenticação
    path('', auth_views.LoginView.as_view(template_name='gabarito_oci/login.html'), name='login'),
    
    
    path('home/', include('home.urls')), 
    path('cadastro/', include('cadastro.urls')), 
    path('aluno/', include('alunos.urls')),  
]