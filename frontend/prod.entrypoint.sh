#!/bin/bash
cd /srv/app

if [ ! -d "/srv/app/node_modules" ]; then
    echo ">> Running `yarn install`"
    yarn install
fi

if [ ! -d "/srv/app/.output" ]; then
    echo ">> Running `yarn build`"
    yarn build
fi

echo ">> Starting Nuxt"
node ./.output/server/index.mjs
