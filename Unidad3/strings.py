try:
    fruta = "BaNana"
    fruta[0]  = "b"  # las cadenas son inmutables
    print(fruta[:].lower())
except TypeError as e:
    print(f"Error: {e}")

print(fruta[:].upper())
# Va  a solictar un nombre cualquiero
# y va indicar si eso es un palinfromema o no

