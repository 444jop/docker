from flask import Flask , Response
import os
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

REQUEST_COUNT = Counter('my_app_requests_total', 'Total request count')

@app.route('/')
def hello():
    REQUEST_COUNT.inc()
    # 파드 이름이나 환경변수를 출력해 보면 나중에 로드밸런싱 확인에 좋습니다
    return f"Hello Kubernetes! This is Python Flask v3.0."

@app.route('/metrics')
def metrics():
    # 수집된 데이터를 텍스트로 변환해서 보여줌
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
