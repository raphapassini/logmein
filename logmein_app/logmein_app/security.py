from Crypto.Cipher import AES
import base64
from django.conf import settings

# the block size for the cipher object; must be 16, 24, or 32 for AES
BLOCK_SIZE = 32

# the character used for padding--with a block cipher such as AES, the value
# you encrypt must be a multiple of BLOCK_SIZE in length.  This character is
# used to ensure that your value is always a multiple of BLOCK_SIZE
PADDING = '{'

# generate a random secret key
secret = settings.SECRET_KEY[:16]

# create a cipher object using the random secret
cipher = AES.new(secret)

# one-liner to sufficiently pad the text to be encrypted
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING

# one-liners to encrypt/encode and decrypt/decode a string
# encrypt with AES, encode with base64
EncodeAES = lambda s: base64.b64encode(cipher.encrypt(pad(s)))
DecodeAES = lambda e: cipher.decrypt(base64.b64decode(e)).rstrip(PADDING)


def encode_aes_using_secret(secret, s):
    cipher = AES.new(secret)
    return base64.b64encode(cipher.encrypt(pad(s)))


