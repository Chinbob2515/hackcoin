from django.contrib import admin

# Register your models here.

from .models import Peer, Node, Transaction

admin.site.register(Peer)
admin.site.register(Node)
admin.site.register(Transaction)
