# Node.js 20.18 Slim 이미지 사용
FROM alibaba-cloud-linux-3-registry.cn-hangzhou.cr.aliyuncs.com/alinux3/node:20.16

# 작업 디렉터리 설정
WORKDIR /app

# 패키지 매니페스트 복사 및 의존성 설치
COPY package.json package-lock.json ./
RUN npm install --production

# 애플리케이션 코드 복사
COPY . .

# 컨테이너가 실행될 때 실행할 명령어
CMD ["node", "index.js"]
