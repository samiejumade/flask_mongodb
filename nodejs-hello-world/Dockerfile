FROM node:18-alpine

WORKDIR /app

run touch a.txt

run echo "hello world" > a.txt
ADD . .

ENTRYPOINT ["node"]

CMD [ "app.js" ]
