from flask import Flask,jsonify,request
import joblib
from keras.models import load_model

app = Flask(__name__)

@app.route("/", methods=['POST','GET'])
def index():
    
    print("A")
    if(request.method == 'POST'):
        data = request.get_json()
        open = float(data["area"])
        print(open)
        #lin_reg = joblib.load("./stock_prediction.pkl")
        
        model_final = keras.models.load_model('./model.h5')
        return jsonify(model_final.predict([[open]]))
    else:
        return  jsonify({"about":"Hello World"})

if __name__ == '__main__':
    app.run(debug=True)
    
    

#from flask import Flask,jsonify,request
#import joblib
#app = Flask(__name__)
#
#@app.route("/", methods=['POST','GET'])
#def index():
#    if(request.method == 'POST'):
#        data = request.get_json()
#        open = float(data["area"])
#        lin_reg = joblib.load("./stock_prediction.pkl")
#        return jsonify(lin_reg.predict([[open]]))
#    else:
#        return  jsonify({"about":"Hello World"})
#
#if __name__ == '__main__':
#    app.run(debug=True)