# Gender prediction using Deep Learning

# Importing all the dependencies

from tensorflow import keras
from keras.preprocessing.image import ImageDataGenerator as imgen
from keras.models import Sequential, Model
from keras.layers import Conv2D,MaxPooling2D,Dropout,Flatten,Dense,Input

from sklearn.model_selection import train_test_split

# Importing saved functions
from Utilities import *


# Getting the Data
data = getData()

# Splitting the pixels

data["pixels"] = data["pixels"].apply(toPixels)

# Reshaping the pixels

Images = reshapetoImage(data)

# Splitting into train and test data
x_train,x_test , y_train,y_test = train_test_split(Images, np.array(data["gender"]), random_state = 42, test_size = 0.15)
x_train,x_val, y_train,y_val = train_test_split(x_train,y_train, random_state = 21, test_size = 0.15)

# Image Data Generator
trainGen = imgen(rescale=1./255,
                 zoom_range=0.2,
                 shear_range=0.2,
                 horizontal_flip=True
                 )
valGen = imgen(rescale=1./255,
                 zoom_range=0.2,
                 shear_range=0.2,
                 horizontal_flip=True
               )
testGen = imgen(rescale=1./255)

trainds = trainGen.flow(x_train,y_train,
                   batch_size = 32
                   )

valds = valGen.flow(x_val,y_val,
               batch_size = 32
               )

testds = testGen.flow(x_test,y_test,
                      batch_size=32,
                      shuffle=False)

# MODEL BUILDING
print("Building model . . .")
"""
# Sequential Model
model = Sequential([
    Conv2D(32,(3,3), activation = "relu", input_shape = (48,48,1)),
    MaxPooling2D(2,2),

    Conv2D(32,(3,3), activation = "relu"),
    MaxPooling2D(2,2),

    Dropout(0.3),

    Conv2D(64,(3,3), activation = "relu"),
    MaxPooling2D(2,2),

    #Conv2D(128,(3,3), activation = "relu"),
    #MaxPooling2D(2,2),

    Flatten(),

    #Dense(256,activation = 'relu'),
    #Dropout(0.5),

    Dense(64,activation = 'relu'),
    Dropout(0.5),


    Dense(1,activation='sigmoid')
])
"""

# Functional Model
image_input = Input(shape=(48,48,1))

l1 = Conv2D(32,(3,3),activation='relu')(image_input)
l2 = MaxPooling2D((2,2))(l1)
l3 = Conv2D(32,(3,3),activation='relu')(l2)
l4 = MaxPooling2D((2,2))(l3)

l5 = Dropout(0.4)(l4)

l6 = Conv2D(64,(3,3),activation='relu')(l5)
l7 = MaxPooling2D((2,2))(l6)
l9 = Conv2D(128,(3,3),activation='relu')(l7)
l10 = MaxPooling2D((2,2))(l9)

l11 = Flatten()(l10)
l12 = Dense(256,activation='relu')(l11)

image_output = Dense(1,activation='sigmoid')(l12)

model = Model(inputs = image_input, outputs = image_output)



print(model.summary())
print("Model Built!!")

# Compile the model
print("Compiling. . . ")
model.compile(optimizer='adam',loss = "binary_crossentropy",metrics=['accuracy'])
print("Model Compiled!!")

# Defining callbacks
my_calls = [keras.callbacks.EarlyStopping(monitor='val_accuracy',patience=3),
            keras.callbacks.ModelCheckpoint("Model_gender.h5",verbose=1,save_best_only=True)]

# Train
print("Starting Training . . . .")
hist = model.fit(trainds,epochs=30,validation_data=valds,callbacks=my_calls)
print("Training Finished!!")

# Test
print("Satrting Testing . . .")
print("Model score is : ")
model.evaluate(testds,verbose=1)



























