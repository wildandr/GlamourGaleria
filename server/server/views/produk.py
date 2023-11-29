# views/produk.py

from pyramid.view import view_config
from ..models import Produk

@view_config(route_name='produk_list', renderer='json')
def produk_list(request):
    query = request.dbsession.query(Produk)
    return list(query)

@view_config(route_name='produk_create', renderer='json', request_method='POST')
def produk_create(request):
    # Implementasi pembuatan produk
    pass

@view_config(route_name='produk_view', renderer='json')
def produk_view(request):
    # Implementasi tampilan detail produk
    pass

@view_config(route_name='produk_update', renderer='json', request_method='POST')
def produk_update(request):
    # Implementasi pembaruan produk
    pass

@view_config(route_name='produk_delete', renderer='json', request_method='DELETE')
def produk_delete(request):
    # Implementasi penghapusan produk
    pass

# Ulangi proses serupa untuk Pemesanan, Pengguna, Pengiriman, Pembayaran
