from curses.ascii import HT
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
import datetime
import csv
import json
from .models import Receipt
# Create your views here.

def index(request):
    print("index")
    receipts = Receipt.objects.all()
    template = loader.get_template("receipts/receipts.html")
    context = {
        "receipts": receipts
    }
    return HttpResponse(template.render(context, request))

def another(request):
    return HttpResponse("this is another webpage")


def second(request):
    return HttpResponse("blah blah")


def retrieve_json_data(request):
    print("in the function")

    receipt_arr = []

    for receipt in Receipt.objects.all():
        receipt_arr.append(receipt.get_receipt())

    return JsonResponse(receipt_arr, safe = False)

def update_receipt(request, id):
    if request.method == "PUT":
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        receipt = Receipt.objects.get(pk = id)
        receipt.name = data["name"]; receipt.cost = data["cost"]; receipt.location = data["location"]
        receipt.save()
        return JsonResponse(receipt.get_receipt())
    return HttpResponse("coudlnt update")

def delete_receipt(request, id):
    if request.method == "DELETE":
        receipt = Receipt.objects.get(pk = id)
        receipt.delete()
        return JsonResponse({})

def add_receipt(request):
    if request.method == "POST":
        date = datetime.datetime.now()
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        receipt = Receipt(name = data["name"], cost = data["cost"], location = data["location"], creation_date = date)
        receipt.save()
        return JsonResponse(receipt.get_receipt())

def download_receipts(request):
    response = HttpResponse(
        content_type = 'text/csv',
        headers = {'Content-Disposition': 'attachment; filename="receipts.csv"'},
    )

    writer = csv.writer(response)
    writer.writerow(["ID", "NAME", "COST", "LOCATION", "CREATION DATE"])
    for receipt in Receipt.objects.all():
        writer.writerow(receipt.get_receipt_arr())
    
    return response