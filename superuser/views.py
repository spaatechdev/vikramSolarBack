from django.shortcuts import render
from vikramSolarBack.decorators import login_required

import environ
env = environ.Env()
environ.Env.read_env()

context = {}
context['project_name'] = env("PROJECT_NAME")
context['client_name'] = env("CLIENT_NAME")

# Create your views here.
@login_required
def dashboard(request):
    return render(request, 'portal/dashboard.html', context)