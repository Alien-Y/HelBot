import json 
import random
import pickle
import numpy as np
import keras
from sklearn.preprocessing import LabelEncoder


# load dataset
with open("static/AI/intents.json", encoding="utf8") as file:
    data = json.load(file)

# load tokenizer object
with open('static/AI/tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

# load label encoder object
with open('static/AI/label_encoder.pickle', 'rb') as enc:
    lbl_encoder = pickle.load(enc)

# load pretrained model
model = keras.models.load_model('static/AI/model')

# parameters
max_len = 20


def response(question):

    result = model.predict(keras.utils.data_utils.pad_sequences(tokenizer.texts_to_sequences([question]),
                                            truncating='post', maxlen=max_len))
    
    tag = lbl_encoder.inverse_transform([np.argmax(result)])
        
    for i in data['intents']:
        if i['tag'] == tag:
            return np.random.choice(i['responses'])