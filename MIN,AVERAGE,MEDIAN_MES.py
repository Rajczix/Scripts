import pandas
import time
import random
from django.contrib.admin.utils import flatten

try:
    f = open("czyt.ini")
    f.close()
    pah = "czyt.ini"
except IOError:
    print("Ini file not found, generating new one")
    f = open("czyt.ini", "w+")
    f.write("NEW;-100000;100000;200000;dane.csv;wynik.csv;AVERAGE;MIN;MEDIAN;10;1000;100000")
    f.close()
    pah = 'czyt.ini'

list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
list6 = []


def ini(pnh):
    cos = pandas.read_csv(r"%s" % pnh, delimiter=';', header=None)
    paha = flatten(cos.to_numpy().tolist())
    print('Odczyt pliku INI.')
    return paha


def tim():
    zat = time.time()
    return zat


def read_csv(ph):
    ndf = []
    result = pandas.read_csv(r'%s' % ph, delimiter=';', header=None)
    print('Odczyt danych')
    try:
        kappa = result.astype(int)
        print(type(kappa))
        ndf = kappa.to_numpy().tolist()
    except ValueError:
        print('str to int fail')
    return ndf


def sv_csv(ph):
    try:
        min1 = int(ph[1])
    except ValueError:
        print('1.Err, using default min=-1000')
        min1 = -1000
    try:
        max1 = int(ph[2])
    except ValueError:
        print('2.Err, using default  max=1000')
        max1 = 1000
    try:
        ile = int(ph[3])
    except ValueError:
        print('3.Err, using default ilosc=100000')
        ile = 100000
    while True:
        if min1 < max1 and ile > 0:
            los = []
            for i in range(ile):
                zeta = random.randint(min1, max1)
                los.append(zeta)
            dan = pandas.DataFrame(los)
            while True:
                z3 = ph[4]
                if z3[-4:] != '.csv':
                    print('wrong extension')
                else:
                    break
            dan.to_csv(r'%s' % z3, sep=';', header=None, index=False)
            return z3
            break
        else:
            print('wrong input, using defualt values min=-1000;max=1000;ile=100000')
            min1 = -1000
            max1 = 1000
            ile = 100000


def qck(dan):
    grt = []
    lrw = []
    if len(dan) <= 1:
        return dan
    else:
        sro = dan.pop()
    for x in dan:
        if x >= sro:
            grt.append(x)
        else:
            lrw.append(x)
    return qck(lrw) + sro + qck(grt)


def dane(ph):
    z = str(ph[0])
    try:
        z = z.upper()
    except ValueError:
        print('1.Ini error; defualt commend: OLD')
        z = 'OLD'
    while True:
        if z == 'NEW':
            a = sv_csv(ph)
            print("\n Data generated \n")
            asa = read_csv(a)
            print('\n Data prepared')
            return asa
            break
        elif z == 'OLD':
            fil = read_csv(ph[4])
            return fil
            break
        else:
            print('2.Ini error; defualt commend:  OLD')
            z = 'OLD'


def wyn(ph, list, list2, list3, list4, list5, list6):
    try:
        print('Saving results.')
        handler = str(ph[5])
    except ValueError or a[-4:] != '.csv':
        handler = 'results.csv'
    df = pandas.DataFrame([])
    df.to_csv(handler)
    f = open(r'%s' % handler, 'w')
    f.write("ALGORITHMS;NUMBER_OF_ELEMENTS;TIME\n")
    for i in range(len(list)):
        f.write("AVERAGE;{};{}\n".format(list[i], list2[i]))
    for i in range(len(list3)):
        f.write("MIN;{};{}\n".format(list3[i], list4[i]))
    for i in range(len(list5)):
        f.write("MEDIAN;{};{}\n".format(list5[i], list6[i]))
    print('Finished saving.')
    f.close()


inicja = ini(pah)
data = dane(inicja)
try:
    m1 = str(inicja[8])
    tan = m1.upper()
except ValueError:
    tan = 'MEDIAN'
try:
    m2 = str(inicja[7])
    tan2 = m2.upper()
except ValueError:
    tan2 = 'MIN'
try:
    m3 = str(inicja[6])
    tan3 = m3.upper()
except ValueError:
    tan3 = 'AVERAGE'
try:
    elem = int(inicja[9])
except ValueError or elem <= 0:
    print('Wrong input, using default value = 1')
    elem = 1
for i in range(elem):
    print('Iterations: {}' .format(i))
    n = 0
    if int(inicja[11]) <= len(data) and int(inicja[10]) > 0:
        n = random.randint(int(inicja[10]), int(inicja[11]))
    else:
        print('Wrong range using defualt values: low=1; high=number of elements')
        n = random.randint(1, len(data))
    merged = []
    if tan3 == 'AVERAGE':
        start = tim()
        dod = 0
        for i in flatten(data[:n]):
            abla = int(i)
            dod = dod + abla
        zmienna = (dod / n)
        end = tim()
        list1.append(n)
        list2.append(end - start)
    else:
        print('NO AVERAGE')
    if tan2 == 'MIN':
        start = tim()
        min1 = data[0]
        for x in range(len(data[0:n])):
            if data[x] < min1:
                min1 = data[x]
        end = tim()
        list3.append(n)
        list4.append(end - start)
    else:
        print('NO MIN')
    if tan == 'MEDIAN':
        start = tim()
        zet = qck(data[:n])
        merged = flatten(zet)
        if n % 2 == 0:
            mem = int(merged[int(n / 2)])
            me = int(merged[int(n / 2) + 1])
            a = (int(merged[int(n / 2)]) + int(merged[int(n / 2) + 1])) / 2
            merged.append(a)
        else:
            medic = int(round(n / 2))
            merged.append(merged[medic])
        end = tim()
        list5.append(n)
        list6.append(end - start)
    else:
        print("NO MEDIAN")
wyn(inicja, list1, list2, list3, list4, list5, list6)