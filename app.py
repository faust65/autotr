import pyperclip
import keyboard
import time
import threading
from flask import Flask, request, jsonify, render_template

app=Flask(__name__)

pt=""
running=False

def loop():
    global running, pt

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
        running=False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    global running

    if not running:
        running=True
        threading.thread(target=loop, daemon=True).start()

@app.route('/stop', methods=['POST'])
def stop():
    global running
    running=False

if __name__ == "__main__":
    app.run()