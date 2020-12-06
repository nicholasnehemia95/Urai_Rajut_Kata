# Fungsi urai = 

# print(urai('Code'))
# print(urai('Python'))
# print(urai('Purwadhika'))

# # Output:
# CCoCodCode
# PPyPytPythPythoPython
# PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika

def urai(kata):
    katabaru=''
    iteration=0 #Ketika iterasi mencapai jumlah huruf dalam kata, maka berhenti
    while iteration!=len(kata):
        katabaru=katabaru+kata[0:iteration+1] #Concate dilakukan untuk range pertama huruf 1, terus 1 dan 2, kemudian 1,2,3 dst hingga huruf habis
        iteration+=1
    return katabaru
print('='*20)    
print('Fungsi Urai')
print('='*20)
print(urai('Code'))
print(urai('Python'))
print(urai('Purwadhika'))
print('='*20)
print('='*20)
print('Fungsi Rajut')
print('='*20)


def rajut(kata2):
    hilang=1 
    hurufkatautama=0
    jumlahhuruftotal=len(kata2)
    while jumlahhuruftotal!=0:
        jumlahhuruftotal=jumlahhuruftotal-hilang
        hilang+=1 ## Jumlah huruf akan dikurang 1, 2, 3 ,4 hingga huruf habis, dan nilai terahkir akan menjadi batas untuk slicing
        hurufkatautama+=1 ## Jumlah huruf dalam kata utama
        # print('sisa huruf adalah ',jumlahhuruftotal)
        # print('jumlah huruf utama adalah ',hurufkatautama)
    katautama=kata2[len(kata2)-hurufkatautama::1]
    # print(katautama)
    return katautama
print(rajut('CCoCodCode'))
print(rajut('PPyPytPythPythoPython'))
print(rajut('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'))
print('='*20)

# while hitunghuruf!=0:
#     hitunghuruf-=jumlahhuruf
#     jumlahhuruf+=1
#     jumlahhuruf+=1
# print(jumlahhuruf)






    

