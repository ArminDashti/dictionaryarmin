from django.shortcuts import render, redirect
from .forms import insert_word_form
from .models import words
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages

def insword(request):
    if (request.method == 'POST'):
        iwf = insert_word_form(request.POST)
        if iwf.is_valid():
            iwf.save(commit=True)
            return redirect('/dictionary-armin/insword/')
    if (request.method == 'GET'):
        iwf = insert_word_form()
        return render(request, 'dictionary_armin/insword.html', {'insert_word_form': iwf})

def randomword(request):
    if (request.method == 'GET'):
        get_word =  words.objects.raw('select * from dictionary_armin_words offset random() * (select count(*) from dictionary_armin_words) limit 1 ;')
        return render(request, 'dictionary_armin/randomword.html', {'word': get_word[0].english_word, 'defn':get_word[0].english_meaning})

def dict_table(request):
    pass

    
