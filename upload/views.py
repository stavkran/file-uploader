from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def upload(request) :
    if request.method == 'POST':
        file = request.FILES['file']
        with open('./upload/uploaded_files/' + file.name, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
    return render(request, 'index.html')
