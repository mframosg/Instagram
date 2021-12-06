"""Users views"""

from django.contrib.auth import login, authenticate
from django.shortcuts import render

def login_view(request):
    """Login view"""
    return render(request, 'login.html')