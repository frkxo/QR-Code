import pyqrcode 
import png 
from pyqrcode import QRCode 
  
  
#qr olucak yazı ya da link
s = "GOTD"
  
#qr yeri
url = pyqrcode.create(s) 
  
# svg file
url.svg("qr_code.svg", scale = 8) 
  
# png file
url.png('qr_code.png', scale = 10) 
