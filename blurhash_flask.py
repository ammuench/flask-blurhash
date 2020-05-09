import blurhash
from flask import Flask, request
app = Flask(__name__)


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    print(filename)
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['POST'])
def blurhashUpload():
    try:
        if "image" not in request.files:
            return {
                "message": 'No image sent in payload'
            }, 400

        image_file = request.files['image']

        if not allowed_file(image_file.filename):
            return {
                "message": "A invalid file was supplied as an image.  Only .png, .jpg, .jpeg, and .gif are allowed"
            }, 403

        xComp = 3
        yComp = 3
        try:
            xComp = int(request.form['x'], 10)
            yComp = int(request.form['y'], 10)
        except:
            defaultValues = True
        finally:
            if (xComp > 9 or yComp > 9):
                xComp = xComp if xComp < 9 else 9
                yComp = yComp if yComp < 9 else 9
                hash = blurhash.encode(
                    image_file, x_components=xComp, y_components=yComp)
                return {
                    "message": f"Hash Successfully Generated for {image_file.filename} with coordinates X{xComp} Y{yComp}",
                    "warning": "Coordinate value over 9 was given, it was reduced to 9",
                    "blurhash": hash
                }, 200
            else:
                hash = blurhash.encode(
                    image_file, x_components=xComp, y_components=yComp)
                if defaultValues:
                    return {
                        "message": f"Hash Successfully Generated for '{image_file.filename}' with coordinates X{xComp} Y{yComp}",
                        "warning": "Default values of 3 were used for X and/or Y, as values were not provided",
                        "blurhash": hash
                    }, 200
                else:
                    return {
                        "message": f"Hash Successfully Generated for '{image_file.filename}' with coordinates X{xComp} Y{yComp}",
                        "blurhash": hash
                    }, 200
    except Exception as err:
        return {
            "message": "A server error occurred",
            "error": str(err)
        }, 500

if __name__ == "__main__":
    app.run(host='0.0.0.0')
