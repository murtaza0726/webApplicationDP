from django.shortcuts import render
import urllib.request,json

# Create your views here.

def home(request):
    return render(request, 'index.html')

def group(request):
    return render(request, 'group.html')

def about(request):
    return render(request, 'about.html')

def dome(request):
    url = 'https://mydbdeployment.herokuapp.com/api/client/v0.1/api/health'
    res = urllib.request.urlopen(url)
    data = json.loads(res.read())

    labels=[]
    chartdata=[]
    for City in data:
        labels.append(City['City'])
        chartdata.append(City['ObesityLevels_percent'])
    return render(request, 'dome.html', {'data':data, 'labels':labels, 'chartdata':chartdata})