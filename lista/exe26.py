"""26. Faça um programa que imprima a tabuada de multiplicação de 1 a 9;"""

for i in range(1, 10):
    print(f"Tabuada do {i}");
    for x in range(1, 11):
        print(f"{i} x {x} = {i*x}");
    print();