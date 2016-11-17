

# from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import RegistryUserForm
from ElearningSystem.user import models as models_input
from ElearningSystem.models.user_service import UserService
class UserView():

    def __init__(self):
        pass

    def index(request):
        print('x')
        return render(request, 'user/index.html', {'title':'registry'})

    def post_registry(request):
        if request.method == 'POST':
            form = RegistryUserForm(request.POST)
            if form.is_valid():
                username = form.data.get('username')
                account_name = form.data.get('account_name')
                password = form.data.get('password')
                email = form.data.get('email')
                user_service = UserService()
                user_service.addUser(username,password,account_name,email)
                user_service.closeSession()
                return render(request,'user/registry.html',{'info':'Successfully'})
        else:
            form = RegistryUserForm()
        return render(request,'user/post_registry.html',{'form':form})