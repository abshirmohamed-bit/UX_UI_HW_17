# Read Me

## Installing Env

1.  Install Python 3.9
2.  Install Flask in your Environment


## Running The Project

**Run the following in your Terminal when creating from scratch**

1. export FLASK_APP=web_app   
2. export FlASK_ENV=development  
3. export FLASK_DEBUG=1 && flask run
4. Click on the link found in your terminal
   1. Or go to [Click This Link](http://127.0.0.1:5000)


**For existing Flask projects such as this one, follow the following steps:-**

1. Ensure you are in the same directory as web_app.py
2. In Command Prompt Run **set FLASK_APP=web_app.py**
   - In Powershell Run **$env:FLASK_APP = "web_app.py"**
3. Then Run **python -m flask run**
