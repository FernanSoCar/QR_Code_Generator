import os
import qrcode
import PySimpleGUI as sg

class QRCodeGenerator:
    def __init__(self):
        sg.theme('DarkBlue')
        layout = [
            [sg.Text('Link', font=('Helvetica', 15), size=(10, 1)),
             sg.Input(key='data', font=('Helvetica', 15), size=(20, 1))],
            [sg.Text('File Name', font=('Helvetica', 15), size=(10, 1)),
             sg.Input(key='filename', font=('Helvetica', 15), size=(20, 1))],
            [sg.Push(), sg.Button('Generate QR Code'), sg.Push()]
        ]

        self.window = sg.Window('QR Code Generator', layout, icon='qrcode.ico')

    def start(self):
        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Generate QR Code':
                data = values['data']
                filename = values['filename']
                if data and filename:
                    self.generate_qr_code(data, filename)
                else:
                    sg.popup('Please enter both data and file name!', title='Error')

    def generate_qr_code(self, data, filename):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color='black', back_color='white')

        
        if not filename.lower().endswith('.png'):
            filename += '.png'

        save_path = os.path.join(os.getcwd(), filename)
        img.save(save_path)
        sg.popup(f'QR Code saved as {save_path}', title='Success')


if __name__ == "__main__":
    app = QRCodeGenerator()
    app.start()
