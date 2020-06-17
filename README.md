# users

This app allows you to work with the list of users. It is possible to create new users, edit or delete the current ones, get the list of all existing users or info on a specific one. Each user has a numeric ID and a username.

I used [FastAPI](https://fastapi.tiangolo.com/) web framework to build the app, because it has high performance, it is easy to code and learn and has a rather well-written [documentation](https://fastapi.tiangolo.com).

### How to install

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### Launch

```
uvicorn main:app --reload
```
The app will be running on http://localhost:8000/.

### HTTP Methods

This app uses following HTTP methods:

| HTTP Methods | URI | Action | Params |
| --- | --- | --- | --- |
| POST | http://localhost:8000/user/ | Add new user | `username`, str type |
| GET | http://localhost:8000/users/ | Get the list of users | - |
| GET | http://localhost:8000/user/{user_id} | Get a specific user | - |
| PUT | http://localhost:8000/user/{user_id} | Update user | `username`, str type |
| DELETE | http://localhost:8000/user/{user_id} | Delete User | `username`, str type |

For more information please see automatic interactive API documentation [here](http://localhost:8000/docs/) that will be generated once you run the app.

### Project Goals

The code is written as a test for [TrueConf](https://trueconf.ru).
