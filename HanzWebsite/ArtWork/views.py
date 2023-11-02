from django.shortcuts import render
from .models import Category, Photo

# Create your views here.

def gallery(request):
    categories = Category.objects.all()
    photos = Photo.objects.all()

    context = {'categories': categories, 'photos': photos}
    return render(request, 'Artwork/gallery.html', context)

def viewphoto(request, pk):
    return render(request, 'Artwork/photo.html')

def addphoto(request):
    return render(request, 'Artwork/add.html')


