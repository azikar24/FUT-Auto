# FUT-Auto
This is a Python Project to check for players prices in FUTWiz.com and sell them on FUT Web App<br/>

Before running Download and install Python:<br/>
https://www.python.org/downloads/<br/>

Then install the dependencies by going to the command line:<br/>
replace /path/to/ with the project directory<br/>
pip install -r /path/to/requirements.txt<br/>

Download ChromeDriver from https://sites.google.com/a/chromium.org/chromedriver/<br/>
Then move it to the following directory:<br/>
"C:\Program Files (x86)\Google\Chrome Beta\Application\chromedriver.exe"<br/>

Edit autoSelling.py and SellingOnWebApp.py script on any text editor:<br/>
replace 'CurrentUserName' with ur computer's user name and keep the quotes<br/>
  computerUserName = 'CurrentUserName'<br/>

then run the script:<br/>
  open the command line and move to the project directory by<br/>
    cd /path/to/project<br/>
  Start getting recent data from FUTWiz by <br/>
    python "FUTWiz Reader.py"<br/>
  This will take approximately 30 minutes<br/>
  then start the selling script by<br/>
    python autoSelling.py<br/>
  or<br/>
    python SellingOnWebApp.py<br/>
   A chrome page will appear, sign in with your FUT credential, and follow with the command line<br/>
    
    
  www.AziKar24.com<br/>
  
