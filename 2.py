# Membalik posisi elemen list

def balikposisi(z):
    x = []
    for i in range (len(z) - 1, -1, -1):
        y = z[i]
        x.append(y)
    return x

print(balikposisi([1,2,3,4]))
print(balikposisi(['A', 'B', 'C', 'D', 'E', 'F', 'G']))
print(balikposisi(['Messi', 'Suarez', 'Coutinho', 'Dembele', 'Rakitic']))