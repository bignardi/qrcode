from flask import Flask, request, jsonify, send_file
#from app.controllers.qr_controller import QRController

from app.controllers import qr_controller

qr_ctr = qr_controller.QRController()

app = Flask(__name__)
qr_controller = qr_ctr

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    data = request.json.get('data')
    qr_img_path = qr_controller.generate_qr(data)

    return send_file(qr_img_path, mimetype='image/png')

if __name__ == '__main__':
    app.run()