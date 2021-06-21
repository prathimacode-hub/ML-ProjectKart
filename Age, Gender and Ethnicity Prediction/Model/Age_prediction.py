# Age prediction using Deep Learning

# Importing all the dependencies

from tensorflow import keras
from keras.preprocessing.image import ImageDataGenerator as imgen
from keras.models import Model
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

x_train,x_test , y_train,y_test = train_test_split(Images, np.array(data["age"]), random_state = 42, test_size = 0.15)
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
print("Building model. . . ")
"""
# Sequential Model
model = Sequential([
    Conv2D(32,(3,3),activation='relu',input_shape=(48,48,1)),
    MaxPooling2D((2,2)),

    Conv2D(32,(3,3),activation='relu'),
    MaxPooling2D((2,2)),

    Dropout(0.4),

    Conv2D(64,(3,3),activation='relu'),
    Conv2D(128,(3,3),activation='relu'),

    Flatten(),

    Dense(256,activation='relu'),

    Dense(1,activation='relu')
])
"""

# Functional Model
image_input = Input(shape=(48,48,1))

l1 = Conv2D(32,(3,3), activation="relu")(image_input)

l2 = Conv2D(32,(3,3), activation="relu")(l1)
l3 = MaxPooling2D(pool_size=(2, 2))(l2)

l4 = Dropout(0.30)(l3)

l5 = Conv2D(64,(3,3), activation="relu")(l4)
l6 = Conv2D(128,(3,3), activation="relu")(l5)

#l7 = BatchNormalization()(l6)

l8 = Flatten()(l6)
l9 = Dense(256, activation= "relu")(l8)

image_output = Dense(1)(l9)
model = Model(image_input, image_output)


print(model.summary())
print("Model Built..")

# Compile the model
print("Compiling the Model....")
model.compile(optimizer='adam',loss = 'mse', metrics=[keras.metrics.mean_absolute_error])
print("Model Compiled!")

# Defining callbacks
my_calls = [keras.callbacks.EarlyStopping(monitor='val_mean_absolute_error',patience=3),
            keras.callbacks.ModelCheckpoint("Model_age.h5",verbose=1,save_best_only=True)]


# Train
print("Starting training . . .  .")
hist = model.fit(trainds,epochs=32,validation_data=valds,callbacks=my_calls)
print("Training Finished!!")

# Test
print("Testing the Model . . .")
print("Model score is :",)
model.evaluate(testds,verbose=1)


















