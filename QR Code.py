import qrcode

qr = qrcode.QRCode(
	version=1,
	error_correction=qrcode.constants.ERROR_CORRECT_M,
	box_size=15,
	border=5
)
data = 'google.com'
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color='green',back_color = 'yellow')
img.save('myQR.png')
