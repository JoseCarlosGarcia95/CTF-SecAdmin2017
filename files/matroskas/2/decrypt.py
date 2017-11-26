from Crypto.PublicKey import RSA
key = RSA.construct((long(5005224750131308657205203400806246001441303080404156831031), long(65537), long(2998231735365593714459952013416540859296752416118818243649)))

allcontent = file('flag.encrypted', 'r')

all = ''
while True:
       data = allcontent.read(96)
       if not data:
           break
       dec_data = key.decrypt(data)
       all += dec_data

print all
