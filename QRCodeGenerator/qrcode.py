import pyqrcode

def qr_code():
    s='your first Qr code'
    d=pyqrcode.create(s)
    d.png('my_img.png',scale=6)
    print('code executed properly')

if __name__ == '__main__':
    qr_code()


# # Import QRCode from pyqrcode
# import pyqrcode
# import png
# from pyqrcode import QRCode
#
# # String which represents the QR code
# s = "www.geeksforgeeks.org"
#
# # Generate QR code
# url = pyqrcode.create(s)
#
# # Create and save the svg file naming "myqr.svg"
# url.svg("myqr.svg", scale=8)
#
# # Create and save the png file naming "myqr.png"
# url.png('myqr.png', scale=6)