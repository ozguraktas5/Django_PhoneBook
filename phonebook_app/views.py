from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Person, Category, Location, UploadImage
from .forms import PersonForm, CategoryForm, LocationForm, UploadForm


def home(request):
    categories = Category.objects.all()
    return render(request, "phonebook/home.html", {"categories": categories})


def all_persons(request):
    persons = Person.objects.all()
    return render(request, "phonebook/all_persons.html", {"persons": persons})


def kisi_ekle(request):
    if request.method == "POST":
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/allpersons")
    else:
        form = PersonForm()
    return render(request, "phonebook/kisi_ekle.html", {"form": form})


def kategori_ekle(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("kategorilistesi")
    else:
        form = CategoryForm()
    return render(request, "phonebook/kategori_ekle.html", {"form": form})


def kategori_listesi(request):
    categories = Category.objects.all()
    return render(
        request, "phonebook/kategori_listesi.html", {"categories": categories}
    )


def kategori_duzenle(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect("kategorilistesi")
    else:
        form = CategoryForm(instance=category)
    return render(request, "phonebook/kategori_duzenle.html", {"form": form})


def kategori_sil(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    category.delete()
    return redirect("kategorilistesi")


def lokasyon_ekle(request, person_id):
    person = Person.objects.get(id=person_id)

    if request.method == "POST":
        form = LocationForm(request.POST)
        if form.is_valid():
            location = form.save()
            person.location = location
            person.save()
            return redirect("allpersons")

    form = LocationForm()
    return render(
        request, "phonebook/lokasyon_ekle.html", {"form": form, "person": person}
    )


def edit_person(request, person_id):
    person = get_object_or_404(Person, id=person_id)
    if request.method == "POST":
        form = PersonForm(request.POST, request.FILES, instance=person)
        if form.is_valid():
            form.save()
            return redirect("allpersons")
    else:
        form = PersonForm(instance=person)
    return render(request, "phonebook/edit_person.html", {"form": form})


def delete_person(request, person_id):
    person = get_object_or_404(Person, id=person_id)
    person.delete()
    return redirect("allpersons")


def upload(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            model = UploadImage(image=request.FILES["image"])
            model.save()
            return render(request, "phonebook/success.html")
    else:
        form = UploadForm()
    return render(request, "phonebook/upload.html", {"form": form})


def some_view(request):
    categories = Category.objects.all()
    context = {"categories": categories}
    return render(request, "../templates/sidebar.html", context)

def search_results(request):
    query = request.GET.get('q')
    results = Person.objects.filter(first_name__icontains=query) | Person.objects.filter(last_name__icontains=query)
    return render(request, 'phonebook/search_results.html', {'results': results, 'query': query})
