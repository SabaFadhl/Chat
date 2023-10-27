
# Chat
It is simple app for chating using Django framework and for learning how to use docker
Chat Room has been the most basic step toward creating real-time and live projects. The chat page will be a simple HTML boilerplate with a simple h1 text with the name of the current user and a link to log out to the user who is just logged in. This ensures that when two users are chatting, one can log out and it will not affect the other user. The other will be still logged in and he can send and receive messages. 

# How to run chat app
## Using docker

    docker run --name=chat_app -d -p 8080:80 sabacb/chat_app

## Running the Django App Locally with venv

### Prerequisites
Before getting started, make sure you have the following installed on your system:
- Python (version 3.6 or higher)
- pip (Python package installer)

### Windows

1. Clone the repository from GitHub:
   
   ```
   git clone https://github.com/SabaFadhl/Chat.git
   ```
   
2. Navigate to the project directory:
   ```
    cd Chat
   ```
3. Create a new virtual environment:

    ```
    python -m venv venv
   ```

4. Activate the virtual environment:

   ```
   venv\Scripts\activate
   ```

5. Install the required dependencies:

   ```
   pip install -r requirements.txt  
   ```

6. Apply the database migrations:

   ```
   python manage.py migrate  
   ```

7. Run the development server:

   ```
   python manage.py runserver  
   ```

8. Open your web browser and visit [http://localhost:8000](http://localhost:8000) to access the Django app.

9. To stop the development server, press `Ctrl + C` in the command prompt.

### Linux

1. Clone the repository from GitHub:
   
   ```
   git clone [https://github.com/SabaFadhl/Chat.git](https://github.com/SabaFadhl/Chat.git)  
   ```

2. Navigate to the project directory:

   ```
   cd Chat  
   ``` 

3. Create a new virtual environment:

   ```
   python3 -m venv venv  
   ```

4. Activate the virtual environment:

   ```
   source venv/bin/activate  
   ```

6. Install the required dependencies:

   ```
   pip install -r requirements.txt  
   ```

6. Apply the database migrations:

   ```
   python manage.py migrate 
   ```

7. Run the development server:

   ```
   python manage.py runserver  
   ```

8. Open your web browser and visit [http://localhost:8000](http://localhost:8000) to access the Django app.

9. To stop the development server, press `Ctrl + C` in the terminal.


# How to use chat app

 1. Open the app http://localhost:8080 
 2.  Click on [Create account](http://localhost:8080/register/)
 3. Enter Username , Password  and Password confirmation.
	-   Your password can’t be too similar to your other personal information.
	-   Your password must contain at least 8 characters.
	-   Your password can’t be a commonly used password.
	-   Your password can’t be entirely numeric.
4. It will redirect to login page enter username and password
5. **Repeat** the previous operations again in **another** browser .


Now you can Send real time message and receive it, the user can log out and it will not affect the other user. The other will be still logged in and he can send and receive messages. 
















