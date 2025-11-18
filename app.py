import pyperclip
import keyboard
import time
from flask import Flask, request, jsonify, render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    pt=""

    while 1:
    
        try:
            if keyboard.is_pressed('esc'):
                print("종료")
                break
        
            ct=pyperclip.paste()
    
            if pt!=ct:
                pt=ct
        
                if "판정" in pt :
                    pt='/emas " " '+pt
                else :
                    pt='/desc '+pt
        
                pyperclip.copy(pt)
                time.sleep(0.5)
        except :
            print("종료됨")
            break