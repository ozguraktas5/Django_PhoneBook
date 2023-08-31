from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Person, Category, Location
from .forms import PersonForm, CategoryForm, LocationForm

def home(request):
    return render(request, "phonebook/home.html")
def all_persons(request):
    persons = Person.objects.all()
    return render(request, 'phonebook/all_persons.html', {'persons': persons})

def kisi_ekle(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("all_persons")
    else:
        form = PersonForm()
    return render(request, "phonebook/kisi_ekle.html", {"form": form})


def kategori_ekle(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("all_persons")
    else:
        form = CategoryForm()
    return render(request, "phonebook/kategori_ekle.html", {"form": form})


def lokasyon_ekle(request):
    if request.method == "POST":
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("all_persons")
    else:
        form = LocationForm()
    return render(request, "phonebook/lokasyon_ekle.html", {"form": form})


def edit_person(request, person_id):
    person = get_object_or_404(Person, id=person_id)
    if request.method == "POST":
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect("all_persons.html")
    else:
        form = PersonForm(instance=person)
    return render(
        request, "phonebook/edit_person.html", {"form": form, "person": person}
    )


def delete_person(request, person_id):
    person = get_object_or_404(Person, id=person_id)
    person.delete()
    return redirect("all_persons")

def upload(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            model = UploadImage(image=request.FILES["image"])
            model.save()
            return render(request, "books/success.html")
    else:
        form = UploadForm()
    return render(request, "books/upload.html", {"form": form})

def some_view(request):
    categories = Category.objects.all()
    return render(request, "sidebar.html", {"categories": categories})
