from simplecrypt import encrypt, decrypt
from base64 import b64encode, b64decode

from dashboard.base.base import Base


class Encrypt_Decrypt(Base):

	def encrypt_for_db(key, value):
		return b64encode(encrypt(key, value)).decode('utf-8')

	def decrypt_for_db(key, value):
		return b64decode(decrypt(key, value)).decode('utf-8')
