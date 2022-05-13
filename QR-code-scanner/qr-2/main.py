import qrcode

img = qrcode.make("QR code generator")
img.save("code.png")