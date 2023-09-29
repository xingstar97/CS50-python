x, y, z = input("Expression: ").split(" ")

x = int(x)
z = int(z)

if y == "+":
    print(f"{x+z: .1f}")
if y == "-":
    print(f"{x-z: .1f}")
if y == "*":
    print(f"{x*z: .1f}")
if y == "/":
    print(f"{x/z: .1f}")

