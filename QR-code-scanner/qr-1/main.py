import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image

qr = pyqrcode.create("Lets go!")
qr.png("code.png",scale=8)