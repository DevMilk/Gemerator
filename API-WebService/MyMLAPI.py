 
import flask 
import numpy as np 
from random import randint
from numpy.random import randn 
np.random.seed(randint(1,3000))


import os
import tensorflow as tf 
from tensorflow.keras.preprocessing.image import array_to_img
import matplotlib  
from matplotlib import cm
matplotlib.use('Agg')

from matplotlib import pyplot as plt

 
from tensorflow.keras.models import load_model, save_model, Model 
from tensorflow.keras import Input 


#%% Generate and show new images
 
import PIL as pil
import io 
import base64
import urllib
from matplotlib import gridspec 

print("Importlar tamam")
app = flask.Flask(__name__)
print("flask name tamam")
featureSize=15
SCALE= 30
MODEL_BUCKET = os.environ['MODEL_BUCKET']
MODEL_FILENAME = os.environ['MODEL_FILENAME']
GEM_model = None
GEM_GAN_model = None
print("fonksiyonlar tanımlanacak") 

def pltToPng():
    fig = plt.gcf()
    plt.close()
    buf = io.BytesIO()
    fig.savefig(buf, format='png' ,transparent=True)
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    return uri 


def getGenerator(modelPath):
    global GEM_model
    print("GET GENERATOR'A GIRILDI, yol: {}, Dosya Mevcut Mu?: {}".format(modelPath,os.path.isfile(modelPath)))
    try:
        print("Model Loading")
        model = load_model(modelPath,compile=False)
        print("Model Loaded")
    except Exception as e:
        print("MODEL YUKLENEMIYOR: ", e)    
    print("Input katmani hazirlaniyor")    
    GEM_input=Input(shape=(featureSize,))
    print("Input katmani hazirlandi")  
    GEM_model=GEM_input

    for layer in model.layers[3:]:
         GEM_model= layer(GEM_model)
    print("layerlar tamamlandi, modele donusturuluyor.")     
    GEM_model = Model(inputs=GEM_input, outputs=GEM_model)
    print("Gem_Model tamamlandi.")
     #%% SET SEED FOR RANDOM NUMBER GENERATOR
 

print("get generator'a girilecek")
# initialize our Flask application and the Keras model
getGenerator(os.path.join("Model","gemmodelv2.h5"))
GEM_GAN_model = load_model(os.path.join("Model","generator_modelY.h5"),compile=False)
print("APP RUN ") 

@app.route("/generate" ,methods =["GET", "POST" ])
def generateGems():
    global GEM_model
    print("Uretime girildi.")
    if(GEM_model==None):
        print("yUkleniyor")
        getGenerator(os.path.join("Model","gemmodelv2.h5"))
        print("yUklendi.") 
    data = {"success": False}
    matrix = []
    Gimage = 0
    print("plt figure olusturuluyor")
    plt.figure(figsize=(5,5))
    gs = gridspec.GridSpec(10, 8, width_ratios=[1, 1, 1,1,1,1,1,1],
         wspace=0.0, hspace=0.0, top=0.95, bottom=0.05, left=0.17, right=0.845) 
    for i in range(0,5):
        for j in range (0,8):
            plt.subplot(gs[i,j])
             
            random_features=np.random.uniform(0,1,featureSize) # GENERATE RANDOM NUMBERS BETWEEN 0 AND 1 BECAUSE WE USED SIGMOID
            random_features = random_features.reshape( (1,featureSize))
             
            print("Product: ",i*8+j) 
            new_Img=GEM_model.predict(random_features)
             
            matrix.append( new_Img.reshape(SCALE,SCALE,3))
             
            filterr = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
            im = pil.Image.fromarray(np.uint8(np.asarray(matrix[i*8+j])*255))   
            mx = im.filter(pil.ImageFilter.EDGE_ENHANCE )     
            plt.imshow(mx)
            plt.axis("off")
    plt.tight_layout( pad=0.0001) 
    print("Data Hazırlanıyor")
    data["Images"]= pltToPng()
    data["success"] = True
    print("Data hazırlandı")
    return flask.jsonify(data)

def generate_latent_points(latent_dim, n_samples):
	# generate points in the latent space
	x_input = randn(latent_dim * n_samples)
	# reshape into a batch of inputs for the network
	x_input = x_input.reshape(n_samples, latent_dim)
	return x_input

@app.route("/GANgenerate" ,methods =["GET", "POST" ])
def generateGemsGAN():
    global GEM_GAN_model
    print("Uretime girildi.")
    if(GEM_GAN_model==None):
        print("yUkleniyor")
        try:
            print("Model Loading")
            GEM_GAN_model = load_model(os.path.join("generator_modelY.h5"),compile=False)
            print("Model Loaded")
        except Exception as e:
            print("MODEL YUKLENEMIYOR: ", e)
            return 0
    data = {"success": False}
    matrix = []
    Gimage = 0
    print("plt figure olusturuluyor")
    plt.figure(figsize=(5,5))
    gs = gridspec.GridSpec(10, 8, width_ratios=[1, 1, 1,1,1,1,1,1],
         wspace=0.0, hspace=0.0, top=0.95, bottom=0.05, left=0.17, right=0.845) 
    for i in range(0,5):
        for j in range (0,8):
            plt.subplot(gs[i,j])
             
            random_features=generate_latent_points(100, 1)
             
            print("Product: ",i*8+j) 
            new_Img=GEM_GAN_model.predict(random_features)
             
            matrix.append( new_Img.reshape(32,32,3))
            plt.imshow(matrix[i*8+j])
            plt.axis("off")
    plt.tight_layout( pad=0.0001) 
    print("Data Hazırlanıyor")
    data["Images"]= pltToPng()
    data["success"] = True
    print("Data hazırlandı")
    return flask.jsonify(data)
#app.run(debug=True)    
if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0') 
    