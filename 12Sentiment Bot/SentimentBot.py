from textblob import TextBlob
from dataclasses import dataclass

@dataclass
class Mood:
    emoji: str
    sentiment: float
    
def get_mood(input_text: str,*,sensitivity: float)-> Mood:
    polarity_float= TextBlob(input_text).sensiment.polarity
    
    friendly_threshold: float = sensitivity
    hostile_threshold: float = sensitivity
    
    if polarity > friendly_threshold:
        return Mood('Good', polarity)
    elif polarity < hostile_threshold:
        return Mood('Angry', polarity)
    else:
        return Mood('Sad, polarity') 
    
def run_bot():
    print('Enter some text to get a sentiment analysis ')      
        
        