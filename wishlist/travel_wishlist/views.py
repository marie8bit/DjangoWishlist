from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.conf.urls import url
from .models import Place
from .forms import NewPlaceForm
# Create your views here.

def place_list(request):
    if request.method=='POST':
        form = NewPlaceForm(request.POST)
        place = form.save()
        if form.is_valid():
            place.save()
            return redirect('place_list')
    places = Place.objects.order_by('name')
    form = NewPlaceForm()
    return render(request, 'travel_wishlist/wishlist.html', {'places':places, 'form': form})



def place_detail(request, pk):
    place = get_object_or_404(Place, pk=pk)
    if (place.visited):
        return render(request, 'travel_wishlist/place_detail.html', {'place': place})
    else:

        return redirect('place_list')


def place_edit(request, pk):
    place = get_object_or_404(Place, pk=pk)
    if request.method == "POST":
        form = NewPlaceForm(request.POST, instance=place)
        if form.is_valid():
            place = form.save(commit=False)

            place.save()
            return redirect('place_detail', pk=place.pk)
    else:
        form = NewPlaceForm(instance=place)
    return render(request, 'travel_wishlist/place_edit.html', {'form': form})
