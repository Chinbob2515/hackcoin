from django.db import models

# Create your models here.

from .hash import HashMixin

class Peer(models.Model):

	invisible = models.BooleanField(default=False)

	ip = models.GenericIPAddressField()


class Node(HashMixin):

	initial = models.BooleanField(default=False)

	time = models.DateTimeField(auto_now=True)

	predecessor = models.ForeignKey(
		'Node',
		on_delete=models.PROTECT,
		null=True, blank=True
	)

	validator = True

	hash_fields = ['initial', 'time', 'predecessor_id']

	def save(self, *args, **kwargs):

		super().save(*args, **kwargs)



class Transaction(HashMixin):

	time = models.DateTimeField()

	owner = models.ForeignKey(
		'Node',
		on_delete=models.PROTECT,
		related_name='transactions'
	)

	hash_fields = ['time', 'owner']
