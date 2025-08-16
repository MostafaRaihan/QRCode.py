import qrcode

# Data to encode
data = "https://www.youtube.com/"

# Create QR code
qr = qrcode.make(data)

# Save QR code as an image
qr.save("youtube_qr.png")

print("✅ QR Code generated successfully!")
