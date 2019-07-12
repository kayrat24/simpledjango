from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError
from my_app.models import GetFormData


def index(request):
    if request.method == 'POST':
        try:
            name=request.POST["name"]            
            email=request.POST["email"]
            message=request.POST["message"]
            print(name, email, message)

        except MultiValueDictKeyError:
            name = False
            email = False
            message = False

        
        else:

            GetFormData.objects.create(
                name=name, email=email, message=message,
            )

    return render(request, 'index.html', {})
# Create your views here.
