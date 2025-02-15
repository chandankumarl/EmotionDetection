import json
import requests

def emotion_detector(text_to_analyze):
    'The function takes text as an input to analyze the emotion and return emotion object'

    url='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    my_obj= { "raw_document": { "text": text_to_analyze } }
    
    # Make request
    response = requests.post(url, json = my_obj, headers=header)
    
    formatted_response=json.loads(response.text)

    anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
    disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
    fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
    joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
    sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']

    emotions = {
        'anger' : anger_score,
        'disgust' : disgust_score,
        "fear" : fear_score,
        "joy" : joy_score,
        'sadness' : sadness_score
    }
    emotions['dominant_emotion']=max(emotions,key=emotions.get)
    
    return emotions

