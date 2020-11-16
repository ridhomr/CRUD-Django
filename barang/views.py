from django.shortcuts import render, redirect
from django.forms.models import model_to_dict
from django.http import HttpResponse
import json

from . import models

def index(req):
  barangs = models.Barang.objects.all()
  context = {
    'data': barangs,
  }

  if req.headers['Accept'] == 'application/json':
    data = [model_to_dict(barang) for barang in barangs]
    context['data'] = data
    return HttpResponse(json.dumps(context))

  return render(req, 'barang/index.html', context)

def create(req):
  if req.POST:
    barang = models.Barang.objects.create(
      nama=req.POST['nama'],
      harga=req.POST['harga']
    )
    return HttpResponse(json.dumps({
      'data': model_to_dict(barang),
    }))

  return render(req, 'barang/create.html')

def update(req, id):
  if req.POST:
    models.Barang.objects.filter(pk=id).update(
      nama=req.POST['nama'],
      harga=req.POST['harga']
    )
    return redirect('/barang')

  barang = models.Barang.objects.filter(pk=id).first()
  return render(req, 'barang/update.html', {
    'data': barang,
  })

def delete(req, id):
  models.Barang.objects.filter(pk=id).delete()
  return redirect('/barang')
