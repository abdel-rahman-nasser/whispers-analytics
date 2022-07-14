import colorama
from colorama import Fore, Style, Back
import json
import numpy as np
import pickle
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense, Embedding, GlobalAveragePooling1D
from keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder

colorama.init()


class Chatbot:
    def __init__(
        self,
        chatbot_name='new_chatbot',
        vocab_size=1000,
        embedding_dim=16,
        max_len=20,
        oov_token="<OOV>",
        epochs=500,
        intents=[]
    ):
        self.chatbot_name = chatbot_name
        self.vocab_size = vocab_size
        self.embedding_dim = embedding_dim
        self.max_len = max_len
        self.oov_token = oov_token
        self.epochs = epochs
        self.intents = intents

        self.model = None
        self.tokenizer = None
        self.lbl_encoder = None

    def create_new_bot(self):
        training_sentences = []
        training_labels = []
        labels = []
        responses = []

        for intent in self.intents:
            for pattern in intent['patterns']:
                training_sentences.append(pattern)
                training_labels.append(intent['tag'])
            responses.append(intent['responses'])

            if intent['tag'] not in labels:
                labels.append(intent['tag'])

        num_classes = len(labels)

        lbl_encoder = LabelEncoder()
        lbl_encoder.fit(training_labels)
        training_labels = lbl_encoder.transform(training_labels)

        tokenizer = Tokenizer(
            num_words=self.vocab_size,
            oov_token=self.oov_token
        )
        tokenizer.fit_on_texts(training_sentences)
        word_index = tokenizer.word_index
        sequences = tokenizer.texts_to_sequences(training_sentences)
        padded_sequences = pad_sequences(
            sequences, truncating='post', maxlen=self.max_len)

        model = Sequential()

        model.add(Embedding(self.vocab_size, self.embedding_dim,
                  input_length=self.max_len))
        model.add(GlobalAveragePooling1D())
        model.add(Dense(16, activation='relu'))
        model.add(Dense(16, activation='relu'))
        model.add(Dense(num_classes, activation='softmax'))

        model.compile(loss='sparse_categorical_crossentropy',
                      optimizer='adam', metrics=['accuracy'])

        history = model.fit(padded_sequences, np.array(
            training_labels), epochs=self.epochs)

        model.save('./saved-chatbots/'+self.chatbot_name)
        # to save the fitted tokenizer
        with open('tokenizer.pickle', 'wb') as handle:
            pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)

        # to save the fitted label encoder
        with open('label_encoder.pickle', 'wb') as ecn_file:
            pickle.dump(lbl_encoder, ecn_file,
                        protocol=pickle.HIGHEST_PROTOCOL)

    # Load the bot and run it
    # def load_and_start_chatbot(self):
    #     # with open("intents.json") as file:
    #     #     data = json.load(file)

    #     # load trained model
    #     model = keras.models.load_model('./saved-chatbots/'+self.chatbot_name)

    #     # load tokenizer object
    #     with open('tokenizer.pickle', 'rb') as handle:
    #         tokenizer = pickle.load(handle)

    #     # load label encoder object
    #     with open('label_encoder.pickle', 'rb') as enc:
    #         lbl_encoder = pickle.load(enc)

    #     # parameters
    #     max_len = 20

    #     while True:
    #         print(Fore.LIGHTBLUE_EX + "User: " + Style.RESET_ALL, end="")
    #         inp = input()
    #         if inp.lower() == "quit":
    #             break

    #         result = model.predict(
    #             keras.preprocessing.sequence.pad_sequences(
    #                 tokenizer.texts_to_sequences([inp]),
    #                 truncating='post',
    #                 maxlen=max_len
    #             )
    #         )
    #         tag = lbl_encoder.inverse_transform([np.argmax(result)])

    #         for i in self.intents:
    #             if i['tag'] == tag:
    #                 print(Fore.GREEN + "ChatBot:" + Style.RESET_ALL,
    #                       np.random.choice(i['responses']))

    #         # print(Fore.GREEN + "ChatBot:" + Style.RESET_ALL,random.choice(responses))

    #     print(Fore.YELLOW +
    #           "Start messaging with the bot (type quit to stop)!" + Style.RESET_ALL)

    # Load the bot and run it

    def load_chatbot(self, chatbot_name):
        # with open("intents.json") as file:
        #     data = json.load(file)

        # load trained model
        model = keras.models.load_model('./saved-chatbots/'+chatbot_name)

        # load tokenizer object
        with open('tokenizer.pickle', 'rb') as handle:
            tokenizer = pickle.load(handle)

        # load label encoder object
        with open('label_encoder.pickle', 'rb') as enc:
            lbl_encoder = pickle.load(enc)

        self.model = model
        self.tokenizer = tokenizer
        self.lbl_encoder = lbl_encoder

    def get_response(self, user_input):
        max_len = 20
        inp = user_input

        result = self.model.predict(
            keras.preprocessing.sequence.pad_sequences(
                self.tokenizer.texts_to_sequences([inp]),
                truncating='post',
                maxlen=max_len
            )
        )
        tag = self.lbl_encoder.inverse_transform([np.argmax(result)])

        for i in self.intents:
            if i['tag'] == tag:
                pick = np.random.choice(i['responses'])
                return pick

        return "Sorry, I don't understand you"

    def load_and_get_response(chatbot_name, user_input, intents):
        # with open("intents.json") as file:
        #     data = json.load(file)

        # load trained model
        model = keras.models.load_model('./saved-chatbots/'+chatbot_name)

        # load tokenizer object
        with open('tokenizer.pickle', 'rb') as handle:
            tokenizer = pickle.load(handle)

        # load label encoder object
        with open('label_encoder.pickle', 'rb') as enc:
            lbl_encoder = pickle.load(enc)

        max_len = 20
        inp = user_input

        result = model.predict(
            keras.preprocessing.sequence.pad_sequences(
                tokenizer.texts_to_sequences([inp]),
                truncating='post',
                maxlen=max_len
            )
        )
        tag = lbl_encoder.inverse_transform([np.argmax(result)])

        for i in intents:
            if i['tag'] == tag:
                pick = np.random.choice(i['responses'])
                return pick

        return "Sorry, I don't understand you"

# bot = Chatbot('bot_company')
# bot.create_new_bot()
# bot.load_and_start_chatbot()
