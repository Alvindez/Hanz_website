from django.shortcuts import render

# Create your views here.

def gallery(request):
    return render(request, 'Artwork/gallery.html')

def viewphoto(request, pk):
    return render(request, 'Artwork/photo.html')

def addphoto(request):
    return render(request, 'Artwork/add.html')


