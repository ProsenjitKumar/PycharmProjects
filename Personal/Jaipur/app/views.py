from django.contrib import messages
from django.shortcuts import render


def home(request):
    return render(request, 'app/index.html')


def result(request):
    if request.method == 'POST':
        search = request.POST['search']
        if search:
            return render(request, 'app/result.html')
        else:
            messages.warning(request, "No Result Found")
    return render(request, 'app/result.html')



