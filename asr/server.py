# -*- coding: utf-8 -*-

import json
import os
import time
import logging
from flask import Flask, request
from asr import asr
from tools.nnet_recognizer import recognizer
app = Flask(__name__)

global next_post
logging.basicConfig(level=logging.DEBUG)


def _declareRec():
    dir="models/"
    final=dir+"final.mdl"
    hclg=dir+"graph/HCLG.fst"
    words=dir+"graph/words.txt"
    try:
        rec = recognizer(final, hclg, words)
        return rec
    except Exception as e:
        print(e)

@app.route('/')
@app.route('/api/healthCheck', methods=['GET'])
def get_response():
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

@app.route('/api/transcribe', methods=['POST'])
def post_response():
    global next_post
    try:
        if request.method == 'POST':
            while(next_post!=True):
                time.sleep(1)
            next_post=False
            wav_file=request.files['audio_file']
            filePath = "temp/"+wav_file.filename
            wav_file.save(filePath)
            asr_result=asr(filePath,rec).replace("_"," ")
            logging.info("Razpoznava postenka " + filePath + " : " + asr_result)
            os.remove(filePath)
            result='{"result":' + '"' + asr_result + '"}'
            next_post=True
            return result
    except Exception as e:
        print(e)
        next_post=True

if __name__ == '__main__':
    rec=_declareRec()
    global next_post
    next_post=True
    print(next_post)
    app.run(host='0.0.0.0', port='5000')
