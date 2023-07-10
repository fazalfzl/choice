
import cv2
import numpy as np
from PyQt5.QtCore import QThread, pyqtSignal
from efficientnet.keras import preprocess_input
from keras.saving.saving_api import load_model

from common_support.utils import load_labels, Config





class RecognitionThread(QThread):
    recognitionFinished = pyqtSignal(list)


    def __init__(self):
        super().__init__()

    def run(self):
        # Start the webcam
        try:
            config = Config()
            model_fpath = config.get('model_fpath')

            model = load_model(model_fpath)


            cap = cv2.VideoCapture(0)

            labels = load_labels()
            while True:
                # Capture frame-by-frame
                ret, frame = cap.read()

                if ret:
                    # Our operations on the frame come here
                    img = cv2.resize(frame, (224, 224))

                    cv2.imwrite('captured_image.jpg', img)

                    # Convert the image to a numpy array
                    img_array = np.array(img)

                    # Expand the dimensions of the image, because the model expects batches of images
                    img_array = np.expand_dims(img_array, axis=0)

                    # Preprocess the input
                    img_array = preprocess_input(img_array)

                    # Run model prediction on the image
                    predictions = model.predict(img_array, verbose=0)

                    # Get the top 3 prediction labels and their corresponding probabilities
                    top_3_indices = np.argsort(predictions[0])[::-1][:4]
                    top_3_labels = [labels[i] for i in top_3_indices]
                    top_3_probs = predictions[0][top_3_indices]

                    self.recognitionFinished.emit(top_3_labels)

            # When everything is done, release the capture and destroy windows
            cap.release()
            cv2.destroyAllWindows()
        except Exception as e:
            print(e)
