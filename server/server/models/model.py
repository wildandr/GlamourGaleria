# models.py

from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime,
    Float
)
from sqlalchemy.orm import relationship
from .meta import Base

class Produk(Base):
    __tablename__ = 'produk'
    id = Column(Integer, primary_key=True)
    nama = Column(String(255), nullable=False)
    harga = Column(Float, nullable=False)
    deskripsi = Column(String(1000))

# Ulangi proses serupa untuk Pemesanan, Pengguna, Pengiriman, Pembayaran
