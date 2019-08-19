from django.shortcuts import render
from djano.config.auth.froms import UserCreationForm

# Create your views here.


def register(request):
	form = UserCreationForm()
	return render(request, 'users/register.html', {'form':form})