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

	# defines whether or not this block is a valid part of the block chain
	constituent = models.BooleanField(default=False)

	def save(self, *args, **kwargs):

		super().save(*args, **kwargs)



class Transaction(HashMixin):

	class TransactionType(models.IntegerChoices):
		MINED = (0, 'Mined')
		TRANSFER = (1, 'Transfer')

	type = models.IntegerField(
		choices = TransactionType.choices
	)

	block_order = models.IntegerField(null=True, blank=True)

	owner = models.ForeignKey(
		'Node',
		on_delete=models.PROTECT,
		related_name='transactions'
	)

	# the only person that needs to sign this is the person who is transferring the money
	signed_one = models.CharField(max_length=512, null=True, blank=True)

	# public keys identifying the actors
	source = models.CharField(max_length=256, null=True, blank=True)
	desination = models.CharField(max_length=256)

	value = models.FloatField()

	hash_fields = ['block_order', 'owner_id', 'value']


def get_wallet_value(public_key):

	out  = Transaction.objects.filter(owner__constituent=True, source=public_key)
	into = Transaction.objects.filter(owner__constituent=True, destination=public_key)

	total = 0
	for transaction in out:
		total -= transaction.value
	for transaction in into:
		total += transaction.value

	return total
