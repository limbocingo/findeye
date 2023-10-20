from django.shortcuts import render, redirect
from django.http.request import HttpRequest
from django.views import View

from user.models import User


class Login(View):
    def get(self, request: HttpRequest):
        if request.COOKIES.get('sid'):
            return redirect('/api/admin/panel/')

        return render(request, 'login.html')

    def post(self, request: HttpRequest):
        username = request.POST.get('username')
        password = request.POST.get('password')

        if request.COOKIES.get('sid'):
            return redirect('/api/admin/panel/')

        try:
            user = User.objects.get(username=username)

            if not user.check_password(password):
                return render(request, 'login.html', {'error': True})
            
        except User.DoesNotExist:
            return render(request, 'login.html', {'error': True})

        response = redirect('/api/admin/panel/') 
        response.set_cookie('sid', user.sid)

        return response

class Panel(View):
    def get(self, request: HttpRequest):
        try:
            User.objects.get(sid=request.COOKIES.get('sid'))
        except User.DoesNotExist:
            return redirect('/api/admin/login/')

        return render(request, 'panel.html')
