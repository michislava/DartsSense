import cv2
from flask import Flask, Response

app = Flask(__name__)

# Raspberry Pi camera settings
camera = cv2.VideoCapture(0)
camera.set(3, 640) # width
camera.set(4, 480) # height

def generate_frames():
    while True:
        # Capture frame-by-frame
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/getFrames')
def get_frames():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)