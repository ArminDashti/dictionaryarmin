from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import dict_from, login_form
from .models import dict as dm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.template.response import TemplateResponse
from django.template import Context, Template

@login_required(login_url='/wordic/login')
@permission_required('wordic.add_dict', raise_exception=True)
def index(request):
    if (request.method == 'POST'):
        form = dict_from(request.POST)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, "Word added")
            return render(request, 'wordic/index.html', {'form': form})
    else:
        form = dict_from()
        return render(request, 'wordic/index.html', {'form': form})

def login_page(request):
    if request.method == 'POST':
        from_login_form = login_form(request.POST)
        username1 = from_login_form['get_username'].value() #Get a field from. The fiels define in forms.py
        password1 = from_login_form['get_pass'].value()
        user = authenticate(username=username1, password=password1)
        if user is None:
            from_login_form_get = login_form() #Generate a form.
            messages.error(request, 'Your username or Password is incorrect. Please Try again.')
            return render(request, 'wordic/login.html', {'form': from_login_form_get}) #'form' is defined in HTML.
        else:
            login(request, user) #Save the login in current session.
            return redirect("/wordic/")

    if request.method == 'GET':
        login_form_ = login_form()
        return render(request, 'wordic/login.html', {'form': login_form_})

@login_required(login_url='/wordic/login')
def dict_table(request):
    if request.method == 'GET':
        query_results  = dm.objects.all()
        return render(request, 'wordic/dicttable.html', {'query_results': query_results }) #'query_results' is defined in HTML.


def cost(request):
    pt = "Nothing"
    t = TemplateResponse(request, 'wordic/cost.html', {})
    if request.method == 'POST':
        get_text = request.POST['a_text'] #'a_text' is defined in HTML.
        return render(request, 'wordic/cost.html', {'put_text': get_text })
    else:
        return render(request, 'wordic/cost.html', {'put_text': pt })
    

def test_temp(request):
    t = TemplateResponse(request, 'wordic/tt.html', {})
    t.render()
    return t.content