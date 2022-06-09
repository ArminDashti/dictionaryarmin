from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .form import nameform

def home_view(request):
    if request.method == 'POST':
        form = nameform(request.POST)
        if form.is_valid():
            vle = 'Good1'
            vle = form.fields['subject'].values()
            return HttpResponse(f'<b> {vle} </b>')
        else:
            return HttpResponseRedirect('<b> Error </b>')
    context ={}
    context['form']= nameform()
    return render(request, "wordform/home.html", context)