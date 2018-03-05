# Viable Bot - API

The API used for Viable Facebook Messenger bot.
Check out the bot - [Click Here](https://www.facebook.com/Viable-1976953669252151/)
### Installation

Viable bot API requires [Python](https://www.python.org) v3+ to run.

Install the libraries and edit the config file and start the server.
1. Install Libraries

    ```
    $ cd ViableBotAPI
    $ pip3 install -r requirements.txt
    ```
2. Edit config.py file
    ```
    $ sudo nano config.py
    ```
    - Assign your Google Maps API Key to 'places_api_key' variable.
    - Save File
3. Set FLASK_APP environment Variable to app.py
    - For Linux
    ```
    $ export FLASK_APP=app.py
    ```
    - For Windows
     ```
    $ set FLASK_APP=app.py
    ```
4. Start the Server
     ```
    $ python3 -m flask run
    ```
5. Server will run at http://localhost:5000
6. Endpoint URL will be http://localhost:5000/api/search
