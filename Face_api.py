from flask import Flask, request, jsonify
from Model import detect_and_plot
import base64
import logging
#pip install -r requirements.txt

app = Flask(__name__)

#defining logger file
logger = logging.getLogger(__name__)
#defines the the lowest-severity log message a logger will handle
logger.setLevel(logging.INFO)
#defines the format of our log messages
formatter = logging.Formatter('%(asctime)s :: %(module)s :: %(levelname)s :: %(message)s')
#define the file to which the logger will log
file_handler = logging.FileHandler('logger.log')
#setting up the format for the logger file
file_handler.setFormatter(formatter)
#adding FileHandler object to logger which would help us send logging output to disk file
logger.addHandler(file_handler)


def base64_to_image(base64_str):
    path_to_save = "imageToSave.jpg"
    with open(path_to_save, "wb") as fh:
        fh.write(base64.decodebytes(base64_str.encode('utf-8')))
    return path_to_save

@app.route('/face_detector', methods=['POST']) # for calling the API
def face_api():
    if (request.method=='POST'):
        try:
            # getting json request data
            img_b64_str = request.json['img']
            # loging info
            logger.info("The request has been received !!")
            img_path = base64_to_image(img_b64_str)

            result = detect_and_plot(img_path)
            logger.info("The output is :  {}".format(result))
            return jsonify(result)
        except Exception as e:
            logger.info("The output is :  {}".format(str(e)))
            return jsonify({"Status":"Error"})


@app.route('/',methods = ['POST'])
def Hello():
    return jsonify("Success")


if __name__ == '__main__':
    app.run(host = "localhost", port = 5002, debug=True)