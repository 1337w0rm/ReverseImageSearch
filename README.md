# ReverseImageSearc

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Reverse Image Search is a Telegram Bot which do reverse image seraches for you. It have bot ```Yandex``` and ```Google``` reverse image search. Just a image to your Bot and reply to that image with ```/yfind``` for Yandex search and ```/gfind``` for Google Search it'll reply back to you with a screenshot of the search and URL to the URL so that you can check the results manually.

## Installation

 #### 1. On Local System

```sh
$ git clone https://github.com/1337w0rm/ReverseImageSearch.git
$ cd Reverse Image Search
$ pip install -r requirements.txt
```
- Open ```config.py``` file in any text editor.
- Put Imgur API   client_id in ```CLIENT_ID``` variable
- Put your Bot Token in ```TELEGRAM_ACCESS_TOKEN``` variable.

- Run
    ```
    python main.py
    ```

#### 2. On Install Heroku
    
- Clone this repository on your local system
    ```
    git clone https://github.com/1337w0rm/Libgen-Telegram-Bot.git
    cd Reverse Image Search
    pip install -r requirements.txt
    ```
 - Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
 - Login to your account with the below command

     ```
    heroku login
    ```
 - Create a new heroku app:
     ```
     heroku create appname
    ```
- Goto the ReverseImageSearch directory, select this app that you creted using Heroku-CLI
    ```
    heroku git:remote -a appname
    ```
- Open ```config.py``` in any text editor 
- Add your Bot Token to ```TELEGRAM_ACCESS_TOKEN``` variable
- Add Heroku app name to ```HEROKU_APP_NAME``` variable
- Add Imgur API client_id in ```CLIENT_ID``` variable

- Add all the files to staging.
    ```
    git add . 
    ```
- Commit new changes:
    ```
    git commit -m "First Push"
    ```
- Push Code to Heroku:
    ```
    git push heroku master
    ```
- Enable Heroku Dyno
    ```
    heroku ps:scale web=1
    ```