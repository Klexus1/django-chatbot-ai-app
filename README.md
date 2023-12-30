This repository is using OpenAI API to bring chatbot GPT into your django app.

![img.png](img.png)

To install and start using:

1) switch into the django_app directory by ``` cd django_app ```
2) Install python requirements by running <br />
    ``` pip install -r requirements.txt ``` (configuring virtual environment recommended) <br />
3) You need to have an openAI API key, which you can get here <br />
    * note that you will need to add a payment method because as of 13/04/23 the API is paid <br />
   https://platform.openai.com/account/api-keys <br />
4) Run ``` python manage.py migrate ``` to create initial local project database 
5) Add your API key to ``` .env ``` file in the root directory
6) Run ``` python manage.py runserver ``` and access the application on http://127.0.0.1:8000/

<br />

Feel free to fork or create pull requests.


