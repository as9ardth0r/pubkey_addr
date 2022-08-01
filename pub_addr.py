import hashlib
import base58

starting_x = 0x0
starting_x = 0x0000d9521578a6e83f8b5b8e943437693cf5ef61031a2b45f4f528b3ed59b9504a00            
p = 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f
beta  = 0x7ae96a2b657c07106e64479eac3434e99cf0497512f58995c1396c28719501ee
beta2 = 0x851695d49a83f8ef919bb86153cbcb16630fb68aed0a766a3ec693d68e6afa40

def hash160(hex_str):
    sha = hashlib.sha256()
    rip = hashlib.new('ripemd160')
    sha.update(hex_str)
    rip.update( sha.digest() )
    return rip.hexdigest()  # .hexdigest() is hex ASCII

def oncurve(x,y):
  x = (x*x*x+7) % p
  y = (y*y) % p
  return x==y
 
while starting_x < p:
    x = starting_x
    ysquared = ((x*x*x+7) % p)     
    y1 = pow(ysquared, (p+1)//4, p)
    y2 = (y1 * -1) % p
    if (y1**2) % p == (x**3 + 7) % p:
        a = (f'02{hex(x)[2:].zfill(64)}')#{hex(y1)[2:].zfill(64)} for pub uncompress
        g = (f'04{hex(x)[2:].zfill(64)}{hex(y1)[2:].zfill(64)}')
        h = (f'04{hex(x)[2:].zfill(64)}{hex(y2)[2:].zfill(64)}')
        b = (f'03{hex(x)[2:].zfill(64)}')#{hex(y2)[2:].zfill(64)} for pub uncompress
        pubkey = a
        pubkey1 = g
        pubkey2 = h
        pubkey3 = b
        compress_pubkey = False
        if (compress_pubkey):
            if (ord(bytearray.fromhex(pubkey[-2:])) % 2 == 0):
                pubkey_compressed = '02'
            else:
                pubkey_compressed = '03'
            pubkey_compressed += pubkey[2:66]
            hex_str = bytearray.fromhex(pubkey_compressed)
        else:
            hex_str = bytearray.fromhex(pubkey)
            
        if (compress_pubkey):
            if (ord(bytearray.fromhex(pubkey1[-2:])) % 2 == 0):
                pubkey_compressed = '02'
            else:
                pubkey_compressed = '03'
            pubkey_compressed += pubkey1[2:66]
            hex_str1 = bytearray.fromhex(pubkey_compressed)
        else:
            hex_str1 = bytearray.fromhex(pubkey1)
            
        if (compress_pubkey):
            if (ord(bytearray.fromhex(pubkey2[-2:])) % 2 == 0):
                pubkey_compressed = '02'
            else:
                pubkey_compressed = '03'
            pubkey_compressed += pubkey2[2:66]
            hex_str2 = bytearray.fromhex(pubkey_compressed)
        else:
            hex_str2 = bytearray.fromhex(pubkey2)
            
        if (compress_pubkey):
            if (ord(bytearray.fromhex(pubkey3[-2:])) % 2 == 0):
                pubkey_compressed = '02'
            else:
                pubkey_compressed = '03'
            pubkey_compressed += pubkey3[2:66]
            hex_str3 = bytearray.fromhex(pubkey_compressed)
        else:
            hex_str3 = bytearray.fromhex(pubkey3)

        key_hash = '00' + hash160(hex_str)
        key_hash1 = '00' + hash160(hex_str1)
        key_hash2 = '00' + hash160(hex_str2)
        key_hash3 = '00' + hash160(hex_str3)

        sha = hashlib.sha256()
        sha1 = hashlib.sha256()
        sha2 = hashlib.sha256()
        sha3 = hashlib.sha256()
        sha.update( bytearray.fromhex(key_hash) )
        sha1.update( bytearray.fromhex(key_hash1) )
        sha2.update( bytearray.fromhex(key_hash2) )
        sha3.update( bytearray.fromhex(key_hash3) )
        checksum = sha.digest()
        checksum1 = sha1.digest()
        checksum2 = sha2.digest()
        checksum3 = sha3.digest()
        sha = hashlib.sha256()
        sha1 = hashlib.sha256()
        sha2 = hashlib.sha256()
        sha3 = hashlib.sha256()
        sha.update(checksum)
        sha1.update(checksum1)
        sha2.update(checksum2)
        sha3.update(checksum3)
        checksum = sha.hexdigest()[0:8]
        checksum1 = sha1.hexdigest()[0:8]
        checksum2 = sha2.hexdigest()[0:8]
        checksum3 = sha3.hexdigest()[0:8]
        i = base58.b58encode( bytes(bytearray.fromhex(key_hash + checksum)) ).decode('utf-8')
        j = base58.b58encode( bytes(bytearray.fromhex(key_hash1 + checksum1)) ).decode('utf-8')
        k = base58.b58encode( bytes(bytearray.fromhex(key_hash2 + checksum2)) ).decode('utf-8')
        l = base58.b58encode( bytes(bytearray.fromhex(key_hash3 + checksum3)) ).decode('utf-8')
        if i.startswith('1Feex'):
            print (i, a )
        if j.startswith('1Feex'):
            print (j, g )
        if k.startswith('1Feex'):
            print (k, h )
        if l.startswith('1Feex'):
            print (l, b )
    starting_x += 1

# 1FeexV6b4bbQJmfCgEunRt6D9xAPth8oGk 03d9521578a6e83f8b5b8e943437693cf5ef61031a2b45f4f528b3ed59b9 504a00
# 1Feex7K6wxppNeiKdFgVd8XGzYTjsFkSXt 03d9521578a6e83f8b5b8e943437693cf5ef61031a2b45f4f528b3ed59b9 632d35