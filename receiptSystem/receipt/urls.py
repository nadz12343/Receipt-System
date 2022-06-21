from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("another", views.another, name = "another"),
    path("second", views.second, name = "second"),
    path("api/retreive_receipts", views.retrieve_json_data, name = "retrive_all_receipts"),
    path("api/update_receipt/<int:id>", views.update_receipt, name = "update_receipt"),
    path("api/delete_receipt/<int:id>", views.delete_receipt, name = "delete_receipt"),
    path("api/add_receipt", views.add_receipt, name = "add_receipt"),
    path("api/download_receipts", views.download_receipts, name = "download_receipts"),
]