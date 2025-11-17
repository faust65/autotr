import pyperclip
import keyboard
import time
from flask import Flask, request, jsonify, render_template

app=Flask(__name__)

'''
프로그램을 실행하고 복사하는 모든 항목을 붙여넣을 때 desc를 붙여줍니다
문장에 판정이 들어가면 emas를 붙여줍니다
불친절합니다
개선점 있으면 주십시오 저도쓰게
'''

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