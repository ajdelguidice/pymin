with open(img, "rb") as image:
    f = image.read()
    b = bytearray(f)
    print(b)
