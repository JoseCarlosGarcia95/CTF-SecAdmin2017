from Crypto.PublicKey import RSA
import os

# List all files to be decompressed.
files = sorted(os.listdir('encrypted'))

# Initialize RSA with our keys.
key = RSA.construct((long(300907363049052383020612454787728712853), long(65537), long(60473486407969069934647032749346055777)))

# Decrypt every file.
all_data = ''

for file in files:
       with open('encrypted/{}'.format(file), 'r') as f:
              raw_data = f.read()
              unencrypted_data = key.decrypt(raw_data)
              
              # Because we see junk data.
              clear_data = unencrypted_data[10:]
              all_data += clear_data


print all_data
