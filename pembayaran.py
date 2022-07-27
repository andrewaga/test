minuman = [
    ['kopi',5000],
    ['susu',6000],
    ['teh',4000],
    ['air',3000]
]
v=0
while v< len(minuman):
    for index,minum in enumerate(minuman):
        print (f'no.{index+1} nama:{minum[0]}',f'harga:{minum[1]}')

    eceran= input('pilih no?')
    ecer= int(eceran)-1

    hargamenu=minuman[ecer][1]

    total= input('berapa?')
    tot=int(total)
    totalan=hargamenu*tot

    print(f'totalny {totalan}')
    # v=v+1
    bayar=input('bayar')
    bayaran=int(bayar)
    kembalian= bayaran - totalan
    if bayaran <=totalan :
        print('uang kurang')
    else :
        print(f'kembalian:{kembalian}')

    if input('apa ingin mngulang lagi?')=='t':
        break
# for urutan , nomor in enumerate(minuman) :
#     print(urutan+1 , nomor)
    # print(type(urutan)) 

# minuman = {
#     'kopi':[['kecil',5000],['besar',6000]],
#     'susu':[['kecil',6000],['besar',7000]],
#     'teh':[['kecil',4000],['besar',5000]]
# }

# for nama in minuman['kopi']:
#     print(nama ,'kopi')

