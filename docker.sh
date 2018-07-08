docker build -t i .
docker kill co
docker rm co
docker run -d --name co -p 80:80 i
