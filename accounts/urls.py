from accounts.views.signin import Signin
from accounts.views.signup import Signup
from accounts.views.user import GetUser

from django.urls import path

urlpatterns = [
    path('signin', Signin.as_view(),name='accounts',),
    path('signup', Signup.as_view(),name='accounts',),
    path('user',GetUser.as_view(),name='accounts',)
    # path('veiculo/<int:pk>/', Veiculo.as_view(), name='veiculo'),
]
