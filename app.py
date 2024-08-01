from flask import Flask, request, jsonify
from gramformer import Gramformer
import torch

app=Flask(__name__)

gf=Gramformer(models=1,use_gpu=torch.cuda.is_available())

@app.route('/correct',methods=['POST'])
def correct():
    data=request.json
    if 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400
    
    text = data['text']
    word_limit = 300  # Set your desired word limit to 300
    if len(text.split()) > word_limit:
        return jsonify({'error': f'Text exceeds word limit of {word_limit} words.'}), 400
    
    text = data['text']
    sentences = text.split('.')  # Splitting text into sentences for chunk processing
    corrected_sentences = []

    for sentence in sentences:
        if sentence.strip():
            corrected = list(gf.correct(sentence.strip()))
            corrected_sentences.append(corrected[0] if corrected else sentence.strip())

    return jsonify({'corrected': ''.join(corrected_sentences)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)