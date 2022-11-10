## Simpli Finance Budget Repo
Take control of your finances. Your money, simplified.

The original intent of this project was to create a budget website that lets user enter their financial information across different expense and income categories.
The website would then total everything to come up with a monthly budget amount of total expenses, income, and money leftover. 
We planned to also give users the ability to create multiple named budgets that could be seen under their login profile. 
We were not able to fulfill all of the original outline ideas and features for this website unfortunately. 

Navigate to www.simpli-finance.onrender.com

_Currently if you click on any button or try to navigate elsewhere, the site will error out._
_This was meant as a mock homepage in order to be able to set up the rest of the Django app and deploy on Render successfully.._

###### Requirements to run files:
- virtualenv
- Python 3.8 or higher

###### These files will be installed inside the virtual environment
- psycopg2-binary
- django==4.1
- django-cockroachdb==4.1

###### Follow these steps:
- Use the command prompt to navigate inside the downloaded file SimpliFinance _(use the 'cd' command)_
- Use 'pip install virtualenv' if not already installed
- Enter 'virtualenv env'
- Navigate to env folder with 'cd env'
- Enter 'Scripts\activate' _This starts the virtual environment_
- Navigate back to main SimpliFinance with 'cd <insert file path>'
- Enter 'pip install -r requirements.txt'
- Once the libraries have been installed, then you can run the command 'python manage.py runserver'
- At which point 
