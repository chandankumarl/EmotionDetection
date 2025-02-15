from flask import Flask,render_template,request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route('/emotionDetector')
def emotion():
    text_to_analyze = request.args.get('textToAnalyze')
    emotions = emotion_detector(text_to_analyze)

    return "For the given statement, the system response is 'anger':{}, 'disgust': {},\
    'fear': {}, 'joy': {} and 'sadness': {}. The dominant emotion is {}.\
    ".format(emotions['anger'],emotions['disgust'],emotions['fear'],emotions['joy'],\
    emotions['sadness'],emotions['dominant_emotion'])
# print(emotion_detector("I hate working long hours"))

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True,port=5000)
