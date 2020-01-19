
#GEM MIXTURE GENERATOR


import numpy as np 
import os
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import ModelCheckpoint

from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import array_to_img
import matplotlib.pyplot as plt

curr_path=os.path.dirname(__file__)
#%% Data receive functions

def getData(pathd,shape):
    os.chdir(pathd)
    Alldatas=[]
    img_data=[]
    img_data=os.listdir(".")
    for image in img_data:
        _,extension = os.path.splitext(image)
        if(extension==".jpg" or extension==".jpeg" or extension==".png"):
            print(image)
            img=load_img(image)
            img=img.resize((shape[0],shape[1]))
            x=img_to_array(img)
            Alldatas.append(x)
    return Alldatas
SCALE=30 #RESIZE ALL IMAGES TO 30X30
all_img=getData(curr_path+"\ALL",(SCALE,SCALE))
all_img_test=getData(curr_path+"\ALLTEST",(SCALE,SCALE))

#%%

# EDIT DATASET AND RESHAPE
all_img=np.asarray(all_img,dtype="float")
all_img_test=np.asarray(all_img_test,dtype="float")

train=all_img/255-0.5
test=all_img_test/255-0.5

trainCount=train.shape[0]
testCount=test.shape[0]

train,test=train.flatten(),test.flatten()
trainShape=int(train.shape[0]/trainCount)
testShape=int(test.shape[0]/testCount)

train,test=train.reshape(trainCount,trainShape),test.reshape(testCount,testShape)
#%%

#CREATE AUTOENCODER
os.chdir(curr_path)
from keras.engine.input_layer import Input 


checkpoint = ModelCheckpoint(curr_path+"\bestWeights.hdf5", monitor='loss', verbose=1, save_best_only=True, mode='min')
callbacklists=[checkpoint]
model = Sequential()

featureSize=15
model.add(Dense(input_dim=train.shape[1],output_dim=train.shape[1],init='uniform'))
model.add(Dense(256, kernel_initializer='uniform'))

model.add(Dense(featureSize, kernel_initializer='uniform',activation="sigmoid")) #SIGMOID TO EASILY GENERATE IMAGES IN WIDE RANGE

model.add(Dense(256, kernel_initializer='uniform'))
model.add(Dense(train.shape[1],init='uniform'))

print(model.summary())
model.compile(loss="mean_squared_error",optimizer="adamax")
model.load_weights(curr_path+"/best.hdf5") #Load weights, if you want to train from zero, delete that line

    
model.fit(train,
          train,
          epochs = 300,
          batch_size = 1024,
          validation_data = (test,test),
         # callbacks=callbacklists, #SET ACTIVE IF YOU WANT TO SAVE WEIGHTS
          verbose=1)

#%% Check difference between test images

check=test[3]
decoded=model.predict(check.reshape((1,)+check.shape))
decoded=(decoded+0.5)
matrix=decoded.reshape(SCALE,SCALE,3)

#Show real image and compressed image from autoencoder
plt.figure(figsize=(30,30))
plt.subplot(20,20,1)
plt.imshow(array_to_img(((check+0.5)).reshape(SCALE,SCALE,3)))
plt.subplot(20,20,2)
plt.imshow(array_to_img(matrix))

#%% Get generator model FROM AUTOENCODER
from keras.models import Model
GEM_input=Input(model.layers[3].input_shape[1:])
GEM_model=GEM_input
for layer in model.layers[3:]:
    GEM_model= layer(GEM_model)
GEM_model = Model(inputs=GEM_input, outputs=GEM_model)
#%% SET SEED FOR RANDOM NUMBER GENERATOR
np.random.seed(seed=42)
#%% Generate and show new images
os.chdir(curr_path+ "\Generated")
plt.figure(figsize=(10,10))
for i in range(0,40):
    plt.subplot(20,20,i+1)
    random_features=np.random.randn(1,featureSize) # GENERATE RANDOM NUMBERS BETWEEN 0 AND 1 BECAUSE WE USED SIGMOID
    new_Img=GEM_model.predict(random_features)
    new_Img=(new_Img+0.5)
    matrix=new_Img.reshape(SCALE,SCALE,3)
    Gimage=array_to_img(matrix)
    plt.imshow(Gimage)
    plt.axis("off")
plt.tight_layout(pad=0.1)

#%%
#Plot Loss
plt.figure(figsize=(10,10))

plt.plot(model.history.history['loss'])
plt.plot(model.history.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()
