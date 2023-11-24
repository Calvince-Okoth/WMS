from django.shortcuts import render

def home(request):
    # Your home view logic here
    return render(request, 'index.html')
def request(request):
    # Your company view logic here
    return render(request, 'Request.html')
def sign(request):
    # Your company view logic here
    return render(request, 'sign.html')


