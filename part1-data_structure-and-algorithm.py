## Part 1 - Data Structure and Algorithm
# Problem 1 - Remove Duplicates
def angka_unik(list_angka):
    seen = {}
    
    unique_index = 0
    for angka in list_angka:
        if angka not in seen:
            seen[angka] = True
            list_angka[unique_index] = angka
            unique_index += 1

    list_angka = list_angka[:unique_index]
    jumlah_angka_unik = unique_index
    return list_angka, jumlah_angka_unik

list_angka = list(map(int, input("Masukkan list angka (pisahkan dengan spasi): ").split()))

output, jumlah_angka_unik = angka_unik(list_angka)

print("Angka unik:", output)
print("Jumlah angka unik:", jumlah_angka_unik)


# Problem 2 - Bilangan Prima ke X
def is_prime(angka):
    if angka <= 1:
        return False
    if angka == 2:
        return True
    if angka % 2 == 0:
        return False
    for i in range(3, int(angka**0.5) + 1, 2):
        if angka % i == 0:
            return False
    return True

def prime_x(n):
    count = 0
    angka = 2
    while True:
        if is_prime(angka):
            count += 1
            if count == n:
                return angka
        angka += 1

n = int(input("Masukkan urutan bilangan prima: "))

output = prime_x(n)
print(f"Bilangan prima ke-{n} adalah {output}")


# Problem 3 -  Fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

n = int(input("Masukkan nomor Fibonacci yang diinginkan: "))

output = fibonacci(n)
print(f"Nomor Fibonacci ke-{n} adalah {output}")


# Problem 4 - Prima Segi Empat
def is_prime(angka):
    if angka <= 1:
        return False
    if angka == 2:
        return True
    if angka % 2 == 0:
        return False
    for i in range(3, int(angka**0.5) + 1, 2):
        if angka % i == 0:
            return False
    return True

def next_prime(start):
    angka = start + 1
    while True:
        if is_prime(angka):
            return angka
        angka += 1

def generate_prime_segiempat(tinggi, lebar, start):
    prima_list = []
    current = start
    
    while len(prima_list) < tinggi * lebar:
        current = next_prime(current)
        prima_list.append(current)
    
    segiempat = []
    index = 0
    for _ in range(tinggi):
        row = prima_list[index:index + lebar]
        segiempat.append(row)
        index += lebar
    
    return segiempat

def print_segiempat(segiempat):
    for row in segiempat:
        print(' '.join(map(str, row)))

tinggi = int(input("Masukkan tinggi segiempat: "))
lebar = int(input("Masukkan lebar segiempat: "))
start = int(input("Masukkan angka mulai: "))

segiempat = generate_prime_segiempat(tinggi, lebar, start)
print_segiempat(segiempat)


# Problem 5 - Total Maksimum Dari Deret Bilangan
def jumlah_subarray_max(nums):
    max_current = max_global = nums[0]

    for num in nums[1:]:
        max_current = max(num, max_current + num)
        if max_current > max_global:
            max_global = max_current

    return max_global

input1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
input2 = [-2, -5, 6, -2, -3, 1, 5, -6]

print(f"Output dari input1: {jumlah_subarray_max(input1)}")  # Output: 6
print(f"Output dari input2: {jumlah_subarray_max(input2)}")  # Output: 7





