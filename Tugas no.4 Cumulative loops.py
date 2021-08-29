bil = input("Masukkan Angka: ")
bil=int(bil)

faktorial = 1

if bil < 0:
   print("Negative tidak punya faktorial")
elif bil == 0:
   print("Faktorial 0 yaitu 1")
else:
   for i in range(1,bil + 1):
       faktorial = factorial*i
   print("Faktorial dari",bil,"yaitu",faktorial)