import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, f1_score
from sklearn.model_selection import GridSearchCV
from sentence_transformers import SentenceTransformer
import pickle

import nltk

def ensure_nltk_resources():
    try:
        nltk.data.find('corpora/stopwords')
    except LookupError:
        nltk.download('stopwords')
    try:
        nltk.data.find('corpora/wordnet')
    except LookupError:
        nltk.download('wordnet')

# Call the function to ensure resources are available
ensure_nltk_resources()

class LegalCaseClassifier:
    def __init__(self, model_name='nlpaueb/legal-bert-base-uncased', test_size=0.2, random_state=42):
        self.model_name = model_name
        self.test_size = test_size
        self.random_state = random_state
        self.label_encoder = LabelEncoder()
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))
        self.sentence_model = SentenceTransformer(self.model_name)
        self.classifier = None


    def clean_legal_text(self, text):
        ''' Clean legal specific text patterns. '''
        text = re.sub(r'\b(vs?|versus)\b', 'versus', text)       # normalize 'vs' to versus
        text = re.sub(r'\d+\s*u\.s\.\s*\d+', 'us_citation', text) # replace U.S. citations
        text = re.sub(r'section\s*\d+[a-z]*', 'section_ref', text)
        return text
    



    def preprocess_text(self, text):
        ''' Preprocess the input text by cleaning, tokenizing, removing stopwords, and lemmatizing'''

        try:
            if not isinstance(text, str):
                raise ValueError(f"Expected string, got {type(text)}")

            # Basic cleaning
            text = text.lower()    # lowercase
            text = re.sub(r'\n', ' ', text)   # remove newlines
            text = re.sub(r'[^a-z\s]', '', text)  # keep only letters
            text = re.sub(r'\s+', ' ', text).strip() # remove extra spaces
            # Word Tokenization
            tokens = word_tokenize(text)  # tokenize

            #stopword removal
            legal_keep_words = {
        'shall', 'must', 'should', 'shouldn', "shouldn't",
        'can', 'couldn', "couldn't", 'may', 'mightn', "mightn't",
        'will', 'won', "won't", 'wouldn', "wouldn't",
        'not', 'no', 'nor', 'without',
        'if', 'unless', 'until', 'when', 'while', 'before', 'after',
        'here', 'there', 'where', 'within', 'between', 'under', 'upon',
        'own', 'whose'
    }
            words_to_be_removed = self.stop_words - legal_keep_words
            tokens = [word for word in tokens if word not in list(words_to_be_removed)]

            # Lemmatization
            tokens = [self.lemmatizer.lemmatize(word) for word in tokens]

            # remove short tokens
            tokens = [word for word in tokens if len(word) > 2]

            # clean legal specific patterns
            tokens = [self.clean_legal_text(word) for word in tokens]

            # Join tokens back to string
            text_joined = ' '.join(tokens)

            return text_joined
        except Exception as e:
            print(f"Error processing text: {e}")
            return ""

    def encode_texts(self, texts):
        ''' Encode texts using the SentenceTransformer model - Legal BERT'''
        try:
            embeddings = self.sentence_model.encode(texts, show_progress_bar=True)
            return embeddings
        except Exception as e:
            print(f"Error encoding texts: {e}")
            return np.array([])
        
    def get_predictions(self, texts):

        ''' Get predictions for new cases. '''
        try:
            if texts.strip() != "":
                processed_texts = self.preprocess_text(texts)
                embeddings = self.encode_texts([processed_texts])

                # load the model
                with open(r'C:\SJSU\Fall 2025\DATA 245 Machine Learning\00001 Assignments\Homework 2.1\Legal Case Classification\Model\legal_case_classifier.pkl', 'rb') as f:
                    self.classifier = pickle.load(f)

                predictions = self.classifier.predict(embeddings)
                return predictions
            else:
                return "Input text is empty"

        except Exception as e:
            print(f"Error in getting predictions: {e}")
            return []
    
    def testing_model(self):
        ''' Test the model with a sample input'''
        try:
            sample_case ="""
is plain that, where an order is set aside, and a matter is remitted to the Tribunal for reconsideration, there is nothing on which any issue estoppel can be founded: Morales v Minister for Immigration and Multicultural Affairs [1998] FCA 334 ; (1998) 82 FCR 374 ; Minister for Immigration and Multicultural Affairs v Wang (2003) 215 CLR 518. It is perhaps understandable, in the light of the history of the proceedings from the decision of the delegate all the way to the High Court, but very unfortunate, that counsel for the appellants should have sought to argue issue estoppel.

"""       
            case_outcome = self.get_predictions(sample_case)
            print("Predicted Outcome is: ", case_outcome)
          
        except Exception as e:
            print(f"Error testing model: {e}")

if __name__ == "__main__":
    classifier = LegalCaseClassifier()
    classifier.testing_model()
