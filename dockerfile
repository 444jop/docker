# 파이썬 3.9 슬림 버전을 기반으로 함
FROM python:3.9-slim

# 작업 디렉토리 설정
WORKDIR /app

# 필요 파일 복사 및 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 소스 코드 복사
COPY . .

# 5000번 포트 개방
EXPOSE 5000

# 실행 명령
CMD ["python", "app.py"]