def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')

def includeme(config):
    config.add_route('produk_list', '/produk')
    config.add_route('produk_create', '/produk/create')
    config.add_route('produk_view', '/produk/{id}')
    config.add_route('produk_update', '/produk/{id}/update')
    config.add_route('produk_delete', '/produk/{id}/delete')

    # Ulangi untuk Pemesanan, Pengguna, Pengiriman, Pembayaran
