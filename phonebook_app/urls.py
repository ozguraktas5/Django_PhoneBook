from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home),
    path("allpersons/", views.all_persons),
    path("kisiekle/", views.kisi_ekle),
    path("kategoriekle/", views.kategori_ekle),
    path("lokasyonekle/", views.lokasyon_ekle),
    path('editperson/<int:person_id>/', views.edit_person, name='edit_person'),
    path('deleteperson/<int:person_id>/', views.delete_person, name='delete_person'),
    path("upload/", views.upload, name="upload_image"),
        
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
