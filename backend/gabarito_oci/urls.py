from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

from cadastro.views import upload_gabarito_view

urlpatterns = [
    # Rota do Admin
    path('admin/', admin.site.urls),
    
    # Rotas de Autenticação
    path('', auth_views.LoginView.as_view(template_name='gabarito_oci/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    
    # --- ROTAS DOS APLICATIVOS (usando include) ---
    path('home/', include('home.urls')), 
    path('cadastro/', include('cadastro.urls')), 
    
    # --- ROTA DA NOVA API ---
    path('api/upload/', upload_gabarito_view, name='api_upload'),
]