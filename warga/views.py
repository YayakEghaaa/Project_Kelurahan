from django.views.generic import ListView, DetailView
from .models import Warga
from .models import Warga, Pengaduan

class WargaListView(ListView):
    model         = Warga
    template_name = 'warga/warga_list.html' 

class WargaDetailView(DetailView):
    model         = Warga
    template_name = 'warga/warga_detail.html'
    
class PengaduanListView(ListView):
    model               = Pengaduan
    template_name       = 'Warga/pengaduan_list.html'
    context_object_name = 'daftar_pengaduan'