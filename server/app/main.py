from flask import Flask, Response, render_template
import cv2

app = Flask(__name__)
video = cv2.VideoCapture(0)

@app.route('/')
def index():
    return render_template("index.html")

def gen(video):

    while True:
        success, image = video.read()
        if not success:
            break
        else:
            ret, jpeg = cv2.imencode('.jpg', image)
            frame = jpeg.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame +b'\r\n\r\n')
def genC(video):
    while True:
        success, image = video.read()
        if not success:
            break
        else:
            imageC = cv2.Canny(image, 150, 450, edges=None)
            retC, jpegC = cv2.imencode('.jpg', imageC)
            jpegC = cv2.resize(jpegC,dsize=0.5)
            frameC = jpegC.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frameC +b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    global video
    return Response(gen(video),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feedC')
def video_feedC():
    global video
    return Response(genC(video),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)