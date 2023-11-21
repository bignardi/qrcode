from flask import request, send_file

from app import app
from app.controllers import qr_controller

qr_ctr = qr_controller.QRController()
qr_controller = qr_ctr

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    data = request.json.get('data')
    qr_img_path = qr_controller.generate_qr(data)

    return send_file(qr_img_path, mimetype='image/png')