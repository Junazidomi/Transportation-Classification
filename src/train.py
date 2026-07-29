import os

def calculate_class_weights(train_nonvehicle, train_vehicle):

    count_nonvehicle = len(os.listdir(train_nonvehicle))
    count_vehicle = len(os.listdir(train_vehicle))
    

    total =  count_nonvehicle + count_vehicle 

    weight_0 = (1 / count_nonvehicle) * (total / 2)
    weight_1 = (1 / count_vehicle) * (total / 2)

    class_weights = {
        0: weight_0,
        1: weight_1
    }

    return class_weights


def train_model(model, train_generator, validation_generator,
                train_nonvehicle, train_vehicle):

    class_weights = calculate_class_weights(train_nonvehicle, train_vehicle)

    history = model.fit(
        train_generator,
        epochs=10,
        validation_data=validation_generator,
        class_weight=class_weights
    )

    return history