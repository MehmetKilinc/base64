import base64
cumle = input("cumle yada kelime :\n")
cumle = cumle.encode("utf-8")
sifreleme = base64.b64encode(cumle)
sifreleme = sifreleme.decode("utf-8")
print(sifreleme)


sifreleme = sifreleme.encode("utf-8")
asil = base64.b64decode(sifreleme)
asil = asil.decode("utf-8")
print(asil)


