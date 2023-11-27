import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze }}
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers = header)
    return response.text

def emotion_predictor(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze }}
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers = header)
    formatted_reponse = json.loads(response.text)
    
    if response.status_code == 200:
        #Emotion scores
        anger_score = formatted_reponse['emotionPredictions'][0]['emotion']['anger']
        disgust_score = formatted_reponse['emotionPredictions'][0]['emotion']['disgust']
        fear_score = formatted_reponse['emotionPredictions'][0]['emotion']['fear']
        joy_score = formatted_reponse['emotionPredictions'][0]['emotion']['joy']
        sadness_score = formatted_reponse['emotionPredictions'][0]['emotion']['sadness']

        emotion_dict = formatted_reponse['emotionPredictions'][0]['emotion']
        score = list(emotion_dict.values())
        emotion = list(emotion_dict.keys())
        dominant_emotion = emotion[score.index(max(score))]
    elif response.status_code == 500:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score =  None
        sadness_score = None
        dominant_emotion = None

    return {'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score, 'joy': joy_score, 'sadness': sadness_score, 'dominant_emotion': dominant_emotion}