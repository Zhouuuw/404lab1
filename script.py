
# This is a note of follwing lab instruction

# --- Question 1: What is your GitHub URL?
#     https://github.com/Zhouuuw


# --- Question 2: What version is the requests library 
# installed on the system? 
# 2.22.0
import requests
print(requests.__version__)


# pip install virtualenv
# create a Create a virtualenv: virtualenv venv --python=python3
# Activate the python virtual environment: source venv/bin/activate


# Try installing requests into your virtual environment.
# Run your Python script that prints out the version 
# of the requests library in your virtualenv.


# --- Question 3: What version is the requests library 
# installed in the virtualenv?
# still 2.22.0

# Open a new terminal.
# Run the script in your new terminal.

# --- Question 4: What is the difference between the virtual 
#     environment and the not virtual environment python?

# --- Question 5: What status code is returned for http://google.com ? 
#     301  
# --- Question 5: What URL must you visit to get a 200 status code?
#     Get something casheable. Reference: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/200


# --- Question 6: What status code is returned for http://google.com/teapot?
# --- 418. I'm a Teapot. Both -i and -iL
requests.get("http://google.com/teapot")
# --- Question 6 : What happens when you curl http://www.google.com/teapot?
# --- 418. both for -i and -il
# --- reference for 418: https://meta.stackexchange.com/questions/185426/stack-overflow-returning-http-error-code-418-im-a-teapot


# ---Question 7: What changed in the output of https://webdocs.cs.ualberta.ca/~hindle1/1.py 
# when you used -X POST? What is this method useful for?
# we change the request to post and sent the data of "X=Y" 

#