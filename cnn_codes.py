from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from  keras.models import Sequential
model = Sequential()

model.add(Convolution2D(filters=32, kernel_size=(3,3), activation='relu',input_shape=(64, 64, 3)))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Convolution2D(filters=16, kernel_size=(3,3), activation='relu',input_shape=(64, 64, 3)))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Flatten())

model.add(Dense(units=32, activation='relu'))
model.add(Dense(units=16, activation='relu'))
model.add(Dense(units=1, activation='sigmoid'))
model.summary()

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

from keras_preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)
test_datagen = ImageDataGenerator(rescale=1./255)
training_set = train_datagen.flow_from_directory(
        '/ml_task/dataset/train_set/',
        target_size=(64, 64),
        batch_size=32,
        class_mode='binary')
test_set = test_datagen.flow_from_directory(
        '/ml_task/dataset/test_set/',
        target_size=(64, 64),
        batch_size=32,
        class_mode='binary')

model.fit(
        training_set,
        steps_per_epoch=1311,
        epochs=3,
        validation_data=test_set,
        validation_steps=10)

model.save('cnn_code.h5')

scores = model.evaluate(test_set,verbose=1)
print('loss',scores[0])
print('acc',scores[1])
acc=scores[1]*100
accuracyfile = open("/ml_task/accuracy.txt", "w")
accuracyfile.write(str(acc))
accuracyfile.close()