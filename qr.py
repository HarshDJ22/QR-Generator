import qrcode 
qr=qrcode.QRCode(
    version = 15 ,
    box_size = 10 ,
    border = 5 ,    
)

data = "https://www.justdial.com/Mumbai/Krishna-Tailors-Opp-M-K-School-Borivali-West/022PXX22-XX22-130212114327-D6H5_BZDET"
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black" , back_color="white")
img.save('text.png')