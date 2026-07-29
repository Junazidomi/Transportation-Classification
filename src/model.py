from tensorflow.keras import Model, layers
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.optimizers import RMSprop,Adam
from tensorflow.keras.layers import InputLayer,Conv2D, MaxPool2D, Dense, Flatten,Dropout, BatchNormalization


def create_model():

    model=Sequential()

    model.add(Conv2D(32,(3,3), activation='relu', input_shape=(64, 64,3)))
    model.add(MaxPool2D(2,2))
    model.add(Dropout(0.25))

    model.add(Conv2D(64, (3,3), activation='relu'))
    model.add(MaxPool2D(2,2))
    model.add(Dropout(0.25))

    model.add(Conv2D(128, (3,3), activation='relu'))
    model.add(MaxPool2D(2,2))
    model.add(Dropout(0.5))

    model.add(Flatten())

    model.add(Dense(64, activation='relu'))
    model.add(Dropout(0.5))
    
    model.add(Dense(2, activation='softmax'))

    model.compile(
        optimizer=Adam(),
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )
    return model