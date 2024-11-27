from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
    d = {'Name': 'Firoz','age': 5 ,'list': ['Md','Firoz','Islam'],'day': datetime.datetime.now(),'courses' : [
        {
            'id' : 1,
            'name' : 'Python',
            'fees' : 5000
        },
        {
            'id' : 2,
            'name' : 'Django',
            'fees' : 10000
        },
        {
            'id' : 3,
            'name' : 'C',
            'fees' : 1000
        },
    ]}
    return render(request,'home.html',d)