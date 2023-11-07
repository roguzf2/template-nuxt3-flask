#!/bin/bash
cd /srv/app

if [ ! -d "/srv/app/node_modules" ]; then
    echo ">> Running `yarn install`"
    yarn install
fi

echo ">> Starting Nuxt"
yarn dev
