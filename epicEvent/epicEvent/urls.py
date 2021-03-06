"""epicEvent URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from authentication.urls import authentication_url_paterns
from customer.urls import customers_url_paterns
from contrat.urls import contrats_url_paterns
from event.urls import events_url_paterns
from django.urls import path


urlpatterns = authentication_url_paterns + \
                customers_url_paterns + \
                events_url_paterns + \
                contrats_url_paterns + \
                [path("sentry-error/", lambda request: 1/0)]
