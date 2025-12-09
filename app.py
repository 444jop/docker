from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    # 파드 이름이나 환경변수를 출력해 보면 나중에 로드밸런싱 확인에 좋습니다
    return f"Hello Kubernetes! This is Python Flask v2."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
