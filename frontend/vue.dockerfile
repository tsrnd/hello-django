FROM node

# install simple http server for serving static content
RUN npm install -g @vue/cli

# make the 'app' folder the current working directory
WORKDIR /code/frontend
# copy both 'package.json' and 'package-lock.json' (if available)
# COPY . .

# install project dependencies
RUN npm install
# COPY . ./
# RUN npm run build
# copy project files and folders to the current working directory (i.e. 'app' folder)

# build app for production with minification
# RUN npm run build

EXPOSE 8080
CMD [ "npm", "run" , "serve" ]