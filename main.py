from PIL import Image
from flask import Flask,jsonify,request
from classifier import getPrediction

app=Flask(__name__)
@app.route("/predictDigit",methods=["POST"])
def predictData():
    image=request.files.get("digit")
    pred=getPrediction(image)
    return jsonify({
        "prediction":pred
    })

if __name__=="__main__":
    app.run()


