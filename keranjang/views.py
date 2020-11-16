from django.shortcuts import render, redirect
from django.contrib import messages
from barang import models as barang_models
from . import models

def index(req):
  keranjangs = models.Keranjang.objects.all()
  total = 0
  for k in keranjangs:
    total += k.total()
  return render(req, 'keranjang/index.html', {
    'data': keranjangs,
    'total': total,
  })

def add(req, barang_id):
  barang = barang_models.Barang.objects.get(pk=barang_id)
  models.Keranjang.objects.create(
    barang=barang
  )
  messages.info(req, f'{barang.nama} berhasil dimasukkan ke keranjang.')
  return redirect('/')

def update(req, id):
  if req.POST:
    up = models.Keranjang.objects.filter(pk=id).update(qty=req.POST['qty'])
    return redirect('/keranjang')

  keranjang = models.Keranjang.objects.filter(pk=id).first()
  return render(req, 'keranjang/update.html', {
    'data': keranjang,
  })

def delete(req, id):
  up = models.Keranjang.objects.filter(pk=id).delete()
  return redirect('/keranjang')
