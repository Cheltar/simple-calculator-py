bahasa = input("Select language(ind/eng):").lower()

if bahasa == "ind":
  print("Simple Calaculator")
  print("Pilih Operator")
  print("tambahan menggunakan +")
  print("kurangan menggunakan -")
  print("kalian menggunakan *")
  print("pembagian menggunakan /")
  select = input("Pilih Operator : ")
  a = int(input("Masukan Angka Pertama :"))
  b = int(input("Masukan Angka Kedua :"))


if bahasa == "eng":
  print("Simple Calculator")
  print("Select Operator")
  print("addition use +")
  print("subtraction use -")
  print("multiplication use *")
  print("division use /")
  select = input("Select Operator : ")
  a = int(input("Input First Number :"))
  b = int(input("Input Second Number :"))

def tambahan():
  if select == "+":
    hsil = a + b
    print(hsil)
    
def kurangan():
  if select == "-":
    hsil = a - b
    print(hsil)

def kalian():
  if select == "*":
    hsil = a * b
    print(hsil)

def bagian():
  if select == "/":
    hsil = a / b
    print(hsil)

tambahan()
kurangan()
kalian()
bagian()
