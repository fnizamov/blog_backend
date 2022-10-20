from django.urls import path
from .views import (
    RecoveryPasswordView,
    RegistrationView,
    AccountActivationView,
    ChangePasswordView,
    RecoveryPasswordView,
    SetRecoveredPasswordView
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='registration'),
    path('activate/<str:activation_code>/', AccountActivationView.as_view(), name='activation'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),
    path('recovery-password/', RecoveryPasswordView.as_view(), name='recovery_password'),
    path('set-recovered-password/', SetRecoveredPasswordView.as_view(), name='set_recovered_password'),
]