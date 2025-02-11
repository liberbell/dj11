from django.shortcuts import render
from .forms import CreateUserForm
from django.shortcuts import redirect


# Create your views here.
def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect("")
        
    context = {"form": form}

    return render(request, "account/registration/register.html", context=context)