minuman = [
    ['kopi',5000],
    ['susu',6000],
    ['teh',4000],
    ['air',3000]
]

for minum,harga in minuman:
    print (f'nama:{minum}',f'harga:{harga}')

for urutan , nomor in enumerate(minuman) :
    print(urutan+1 , nomor)
    # print(type(urutan)) 

# minuman = {
#     'kopi':[['kecil',5000],['besar',6000]],
#     'susu':[['kecil',6000],['besar',7000]],
#     'teh':[['kecil',4000],['besar',5000]]
# }

# for nama in minuman['kopi']:
#     print(nama ,'kopi')

