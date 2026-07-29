from tensorflow.keras.preprocessing.image import ImageDataGenerator

def create_generators(train_dir, test_dir):
    datagen=ImageDataGenerator(
        rescale=1./255,
        validation_split=0.2
    )
    test_datagen=ImageDataGenerator(rescale=1./255)

    train_generator=datagen.flow_from_directory(
        train_dir,
        batch_size=32,
        target_size=(64, 64),
        class_mode='categorical',
        subset='training',
        shuffle=True
    )
    validation_generator=datagen.flow_from_directory(
        train_dir,
        batch_size=32,
        target_size=(64,64),
        class_mode='categorical',
        subset='validation',
        shuffle=False
    )
    testing_generator=test_datagen.flow_from_directory(
        test_dir,
        batch_size=32,
        class_mode='categorical',
        target_size=(64,64),
        shuffle=False
    )

    return train_generator, validation_generator, testing_generator