
# Chat
It is simple app for chating using Django framework and for learning how to use docker
Chat Room has been the most basic step toward creating real-time and live projects. The chat page will be a simple HTML boilerplate with a simple h1 text with the name of the current user and a link to log out to the user who is just logged in. This ensures that when two users are chatting, one can log out and it will not affect the other user. The other will be still logged in and he can send and receive messages. 

# How to run chat app
## Using docker

    docker run --name=chat_app -d -p 8080:80 sabacb/chat_app
    docker container run -p 8080:8000 sabacb/chat_app
open [http://127.0.0.1:8888/](http://127.0.0.1:8888)
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
    <img width="917" alt="image" src="https://github.com/SabaFadhl/Chat/assets/80360074/f69fb673-a049-4f83-b07d-16ae8ee867eb">

 3. Enter Username , Password  and Password confirmation.
	-   Your password can’t be too similar to your other personal information.
	-   Your password must contain at least 8 characters.
	-   Your password can’t be a commonly used password.
	-   Your password can’t be entirely numeric.
   ![image](https://github.com/SabaFadhl/Chat/assets/80360074/359f6b11-64e6-48f7-bd6a-287eee9dcdf5)

5. It will redirect to login page enter username and password
![image](https://github.com/SabaFadhl/Chat/assets/80360074/4800b040-5e2d-4f31-89aa-7f0357f732c5)

6. **Repeat** the previous operations again in **another** browser .
![image](https://github.com/SabaFadhl/Chat/assets/80360074/9c82ea43-ad2a-42e6-b972-2d9cc3154c54)


Now you can Send real time message and receive it, the user can log out and it will not affect the other user. The other will be still logged in and he can send and receive messages. 
















