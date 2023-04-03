import qrcode 
import pyttsx3 as pt
import PySimpleGUI as sg

layout = [
    
[sg.Input('', key = 'INPUT_1')],
[sg.Button('Create', key = 'create_QRcode')],
[sg.Image('MyQrcode.png')]
    
]

window = sg.Window('QR Code Generator', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'create_QRcode':
        input_1 = values['INPUT_1']
        image = qrcode.QRCode(
            version = None, 
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            border=5, 
            box_size=9
        )
        image.add_data(input_1)
        image.make(fit = True)
        FILL_COLOR = (200, 18, 52)
        BACK_COLOR = (10, 45, 30)
        img = image.make_image(fill_color = 'blue', back_color = 'cyan')
        img.save('Fati_Qrcode.png')
        
window.read()

