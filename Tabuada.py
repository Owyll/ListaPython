numero = int(input("Tabuada de qual numero?"))
print(f"--- Tabuada do {numero} ---")
for i in range(1, 11):
    res = numero * i
    print(f"{numero} x {i} = {res}")

