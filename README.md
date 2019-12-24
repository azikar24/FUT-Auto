# FUT-Auto
This is a Python Project to check for players prices in FUTWiz.com and sell then sell them on FUT Web App

Before running Download and install Python:
https://www.python.org/downloads/

Then install the dependencies by going to the command line:
replace /path/to/ with with the project directory
pip install -r /path/to/requirements.txt

Download ChromeDriver from https://sites.google.com/a/chromium.org/chromedriver/
Then move it to the following directory:
"C:\Program Files (x86)\Google\Chrome Beta\Application\chromedriver.exe"

Edit autoSelling.py script on any text editor:
  computerUserName = 'CurrentUserName'

then run the script:
  open the command line and move to the project directory by
    cd /path/to/project
  Start getting recent data from FUTWiz by 
    python "FUTWiz Reader.py"
  This will take approximately 30 minutes
  then start the selling script by
    python autoSelling.py
  or
    python SellingOnWebApp.py
   A chrome page will appear, sign in with your FUT credential, and follow with the command line
    
    
  www.AziKar24.com
  
