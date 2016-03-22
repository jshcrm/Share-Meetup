from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.contrib.auth.decorators import login_required
from .forms import UserForm

# Create your views here.
def home(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def create_account(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/login')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = UserForm()

        return render(request, 'UserForm.html', {'form': form})

@login_required(redirect_field_name='share', login_url='/login')
def share(request):
    template = loader.get_template('share.html')
    return HttpResponse(template.render())



