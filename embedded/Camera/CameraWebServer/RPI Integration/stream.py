import cv2
from flask import Flask, send_file

app = Flask(__name__)

# Raspberry Pi camera settings
camera = cv2.VideoCapture(0)
camera.set(3, 640) # width
camera.set(4, 480) # height

def get_frame():
    success, frame = camera.read()
    if success:
        ret, buffer = cv2.imencode('.jpg', frame)
        return buffer.tobytes()
    else:
        return None

@app.route('/getFrames')
def get_frames():
    frame = get_frame()
    if frame:
        return send_file(
            frame,
            mimetype='image/jpeg',
            as_attachment=False,
            cache_timeout=0
        )
    else:
        return "Failed to get frame", 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)