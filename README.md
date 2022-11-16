## Simpli Finance Budget Website README
#### Take control of your finances. Your money, simplified.

The website is a static one page site that educates users on how to make a budget, where you can download pre-existing budgets, and offers budget examples. 
The goal of the website is to help users take control of their finances again and focus on ways to improve saving money and lowering expenses. 

Navigate to www.simpli-finance.onrender.com to see the site live on Render.

##### Requirements to run downloaded GitHub zip file:
- virtualenv
- Python 3.8 or higher

##### These files will be installed inside the virtual environment
- psycopg2-binary
- django==4.1
- django-cockroachdb==4.1
- gunicorn==20.1.0
- whitenoise==6.2.0

##### Follow these steps to run the unzipped files from your computer:
1. In the command prompt, navigate inside the downloaded file SimpliFinance with the `cd` command
2. Use `pip install virtualenv` if not already installed
3. Enter `virtualenv env`
4. Navigate to env folder with `cd env`
5. Enter `Scripts\activate` _This starts the virtual environment_
6. Navigate back to main SimpliFinance with `cd <insert file path>`
7. Enter `pip install -r requirements.txt`
8. Once the libraries have been installed, then you can run the command `python manage.py runserver`
9. At which point, the below text should appear:
 ```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
November 10, 2022 - 14:56:23
Django version 4.1, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```
10. Copy the IP address and paste into a browswer to see the project live. The same home page from the Render site will appear at the IP address
