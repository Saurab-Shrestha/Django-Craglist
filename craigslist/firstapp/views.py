import requests
from bs4 import BeautifulSoup
from django.shortcuts import redirect, render
from requests.compat import quote_plus
from .import models
from .models import Todo
from .import forms

BASE_CRAIGSLIST_URL = 'https://losangeles.craigslist.org/search/?query={}'
BASE_IMAGE_URL = 'https://images.craigslist.org/{}_300x300.jpg'
# Create your views here.

def home(request):
    return render(request, 'home.html')

def new_search(request):
    search =  request.POST.get('search')
    models.Search.objects.create(search = search)
    final_url = BASE_CRAIGSLIST_URL.format(quote_plus(str(search)))
    response =requests.get(final_url)
    data = response.text
    soup= BeautifulSoup(data,features='html.parser')
    post_listings = soup.find_all('li',{'class':'result-row'})
    final_postings = []
    for post in post_listings:
        post_title = post.find(class_='result-title').text
        post_url = post.find('a').get('href')
        if post.find(class_='result-price'):
            post_price = post.find(class_='result-price').text
        else:
            post_price = 'N/A'
        
        if post.find(class_='result-image').get('data-ids'):
            post_image_id = post.find(class_='result-image').get('data-ids').split(',')[0].split(':')[1]
            post_image_url = BASE_IMAGE_URL.format(post_image_id)
            print(post_image_url)
        else:
            post_image_url = 'https://craigslist.org/images/peace.jpg'
        final_postings.append((post_title,post_url,post_price,post_image_url))

    stuff_for_frontend = {
        'search':search,
        'final_postings':final_postings,
    }
    return render(request,'firstapp/new_search.html',stuff_for_frontend)


def weather(request):
    return render(request,'weather.html')

def calorie_meter(request):
    return render(request, 'caloriemeter.html')


""" Text-to-html """
def text_to_html(request):
    form = forms.EditorForm()
    return render(request, 'text_to_html.html', {'form':form})


""" Todo List """
def todo(request):
    form =  forms.TodoForm()

    if request.method == "POST":
        #get the posted form
        form = forms.TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')

    todos = Todo.objects.all() 
    return render(request, "todo.html",{"todo_form": form,"todos": todos})

def update_todo(request,pk):
    todo = Todo.objects.get(id=pk)
    form = forms.TodoForm(instance=todo)

    if request.method == "POST":
        form  = forms.TodoForm(request.POST, instance = todo)
        if form.is_valid():
            form.save()
            return redirect("todo")
        
    return render(request, "update_todo.html",{"todo_edit_form":form})


def delete_todo(request,pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect("todo")