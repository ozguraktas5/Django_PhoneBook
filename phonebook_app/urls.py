from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name="phone_index"),
    path("allpersons/", views.all_persons, name="allpersons"),
    path("kisiekle/", views.kisi_ekle, name="kisiekle"),
    path("kategoriekle/", views.kategori_ekle,name="kategoriekle"),
    path("kategorilistesi/", views.kategori_listesi, name="kategorilistesi"),
    path("kategoriduzenle/<int:category_id>/", views.kategori_duzenle, name='kategoriduzenle'),
    path("kategorisil/<int:category_id>/", views.kategori_sil, name="kategorisil"),
    path("lokasyonekle/<int:person_id>/", views.lokasyon_ekle, name="lokasyonekle"),
    path('editperson/<int:person_id>/', views.edit_person, name='edit_person'),
    path('deleteperson/<int:person_id>/', views.delete_person, name='delete_person'),
    path("upload/", views.upload, name="upload_image"),
    path("search/", views.search_results, name='search_results'),
    
        
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
