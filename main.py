from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import Response
from pydantic import BaseModel
from pathlib import Path
import json


class User(BaseModel):
    id_: int = None
    username: str


def load_users(filepath):
    '''Load users.json or create an empty list'''
    with open(filepath, 'r') as src:
        try:
            users = json.load(src)
        except json.decoder.JSONDecodeError:
            users = []
    return users


Path('files').mkdir(parents=True, exist_ok=True)
filepath = Path('files') / Path('users.json')
filepath.touch(exist_ok=True)

app = FastAPI()


@app.post('/user/', status_code=201)
def create_user(user: User, response: Response):
    '''Create a new user'''
    users = load_users(filepath)
    user = user.dict()
    user['id_'] = users[-1]['id_'] + 1
    users.append(user)
    with open(filepath, 'w') as src:
        json.dump(users, src)
    location = f"/user/{user['id_']}"
    response.headers['Location'] = location


@app.get('/users/')
def get_users():
    '''Get a list of users'''
    users = load_users(filepath)
    return users


@app.get('/user/{user_id}')
def get_user(user_id: int):
    '''Get a specific user'''
    users = load_users(filepath)
    user = list(filter(lambda user: user['id_'] == user_id, users))
    if user:
        return user[0]
    raise HTTPException(status_code=404, detail='User not found')


@app.put('/user/{user_id}', status_code=204)
def edit_user(user_id: int, user_update: User):
    '''Edit user'''
    users = load_users(filepath)
    user = list(filter(lambda user: user['id_'] == user_id, users))
    if user:
        user[0]['username'] = user_update.username
        with open(filepath, 'w') as src:
            json.dump(users, src)
    else:
        raise HTTPException(status_code=404, detail='User not found')


@app.delete('/user/{user_id}', status_code=204)
def delete_user(user_id: int):
    '''Delete user'''
    users = load_users(filepath)
    user = list(filter(lambda user: user['id_'] == user_id, users))
    if user:
        users.remove(user[0])
        with open(filepath, 'w') as src:
            json.dump(users, src)
    else:
        raise HTTPException(status_code=404, detail='User not found')
