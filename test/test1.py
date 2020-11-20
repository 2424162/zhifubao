hah = {1:1}
cc = hah
hah.update({2:2})
print(cc)

lala = 9
hh = lala
lala = lala+1
print(hh)

caca = [1,2,3]
hha = caca
caca.append(4)
print(hha)
import time
time1 = time.time()
for i in range(10000000):
    pass
time2 = time.time()
print(time2-time1)
