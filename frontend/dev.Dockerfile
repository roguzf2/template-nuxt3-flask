# USING NODE 18.16.1 LTS
FROM node:18.16.1-alpine3.17

# SET WORKDIR
WORKDIR /srv/app

# COPY SOURCE FILES
COPY . .

# RUN ENTRYPOINT
ENTRYPOINT [ "sh", "/srv/app/dev.entrypoint.sh" ]
