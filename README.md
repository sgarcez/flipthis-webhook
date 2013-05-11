# Flipboard Relay Hook

Web application that will act as a hook, receiving an article URL and Title, which will then be added to your own Flipboard magazine.

## Installation



### Set up Virtual Environment
```
virtualenv venv
```

### Activate the Virtual Environment
```
source venv/bin/activate
```

### Install Requirements
Installs dependencies like 'requests' and 'Flask'
```
pip install -r requirements.txt
```

### Set-up Facebook Credentials
Set your Flipboard username and password as environment variables.
```
export FLIPBOARD_USERNAME='your-username-here'
export FLIPBOARD_PASSWORD='your-password-here'
```

## Running

### Running the App
Run the Flask server with:
```
python webapp.py
```

Now you have the web application running, you can accept GET requests with URLs and Titles that you want to add to Flipboard.
```
http://127.0.0.1:5000/?url=[URL_TITLE_HERE]&title=[ARTICLE_TITLE_HERE]
```

Example:
```
http://127.0.0.1:5000/?url=http://www.gizmodo.co.uk/2013/05/nasas-space-exploration-vehicle-pimp-my-rover/&title=NASA%E2%80%99s%20Space%20Exploration%20Vehicle:%20Pimp%20My%20Rover
```

## Testing
Only one test so far
```
python flipboard_tests.py
```

## TODO
1. Allow configuration of the magazine you would like to post this to.