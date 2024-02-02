import secrets

generated_key = secrets.token_urlsafe(16)
generated_key_hex = secrets.token_urlsafe(16)

print(generated_key)
print(generated_key_hex)
#
# 1 - os.urandom(64).encode('hex')  # from os module
# 2 - uuid.uuid4()  # from uuid module
# 3 - get_random_string(length=32)  # from django.utils.crypto
# 4 - secrets.token_hex(64)  # from secrets >= python 3.6