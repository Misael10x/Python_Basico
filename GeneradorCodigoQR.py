import qrcode

texto = input("Ingresa el texto o enlace para generar el QR: ")
nombre_archivo = "codigo_qr.png"

qr = qrcode.make(texto)
qr.save(nombre_archivo)

print(f"Código QR gua
