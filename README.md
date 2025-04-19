# Legisletter

installed npm/npx
$ npx frontity create frontity-react
    select Mars theme
$ cd app
In frontity.settings.js:
    replace line 49 with the domain of my Wordpress hosted website
    add "isWpCom":"true", because Im not connecting to a simple free website.
$ npm install dotenv --save
$ npx frontity serve


later...
$ npx frontity dev
    localhost opens in browser
$ Docker build

Common Commands: 
View Nginx log: $ /var/log/nginx/access.log
Edit Nginx Configs: $ sudo nano /etc/nginx/nginx.conf
Build Docker image: $ docker build -t legisletter .
Build Docker-Compose: $ docker-compose up --build (unlike in "detached mode, this will show output in the terminal)
Build Docker-Compose detached: $ docker-compose up --build -d
start nginx: $ sudo nginx
view active images: $ docker ps
