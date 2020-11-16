from django.db import models

from barang import models as barang_models

class Keranjang(models.Model):
  barang = models.ForeignKey(barang_models.Barang, on_delete=models.CASCADE, related_name='keranjang')
  qty = models.IntegerField(default=1)

  def __str__(self):
    return self.barang.nama

  def total(self):
    return self.barang.harga * self.qty

