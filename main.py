#pip install qrcode
#pip install pillow

import qrcode

# Data to encode
data = "https://www.youtube.com/"

# Create QR code
qr = qrcode.make(data)

# Save the QR code as an image
qr.save("youtube_qr.png")

print('Qr Code making Process Completed')

