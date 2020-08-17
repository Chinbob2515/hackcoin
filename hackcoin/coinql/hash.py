from django.db import models

# defining a hash mixin for use in the blockchain objects

import hashlib

class HashMixin(models.Model):

	def hash_string(self, str):

		hashGen = hashlib.sha512()
		hashGen.update(str.encode("utf-8"))

		return hashGen.hexdigest()

	def __hash__(self, **kwargs):

		if "hash_fields" in kwargs:
			fields = kwargs["hash_fields"]
		else:
			fields = self.hash_fields

		repr = ""

		for field in fields:
			val = str(self.__dict__[field])
			repr += val

		val = self.hash_string(repr)
		print("__hash__", repr, val, int(val, 16))
		return int(val, 16)

	data_hash = models.CharField(max_length=256, null=True, blank=True)
	validator = False
	nonce = models.IntegerField(default=0, blank=True)
	verification = models.CharField(max_length=256, null=True, blank=True)
	valid = models.BooleanField(default=False)

	def save(self, *args, **kwargs):

		self.data_hash = self.__hash__()

		if self.validator:
			self.verification = self.__hash__(hash_fields=["data_hash", "nonce"])
			self.valid = int(self.verification) < 2**511 #170803185

		super().save(*args, **kwargs)

	class Meta:
		abstract = True
