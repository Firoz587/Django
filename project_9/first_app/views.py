from django.shortcuts import render

# Create your views here
def home(request):
    responce = render(request,'home.html')
    responce.set_cookie('name','Firoz')
    return responce

def get_cookies(request):
    name = request.COOKIES.get('name')
    print(request.COOKIES)
    return render(request,'get_cookie.html',{'name': name})

def delete_cookie(request):
    responce = render(request,'delete.html')
    responce.delete_cookie('name')
    return responce

def set_session(request):
    data = {
        'name' : 'Firoz',
        'age' : 20,
        'language' : 'Bangla'
    }
    request.session.update(data)
    return render(request,'home.html')

def get_session(request):
    name = request.session.get('name' , 'Guest')
    age = request.session.get('age')
    return render(request,'get_session.html',{'name': name, 'age': age})

def delete_session(request):
    request.session.flush()
    return render(request,'delete.html')