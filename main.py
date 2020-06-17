from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import Response
from pydantic import BaseModel


class User(BaseModel):
    id_: int = None
    username: str

app = FastAPI()

fake_db = [
    {'id_': 0, 'username': 'Alice'},
    {'id_': 1, 'username': 'Bob'},
    {'id_': 2, 'username': 'Carol'},
]


@app.post('/user/', status_code=201)
def create_user(user: User, response: Response):
    '''Create a new user'''
    user = user.dict()
    user['id_'] = fake_db[-1]['id_'] + 1
    fake_db.append(user)
    location = f"/user/{user['id_']}"
    response.headers['Location'] = location


@app.get('/users/')
def get_users():
    '''Get a list of users'''
    return fake_db


@app.get('/user/{user_id}')
def get_user(user_id: int):
    '''Get a specific user'''
    user = list(filter(lambda user: user['id_'] == user_id, fake_db))
    if user:
        return user[0]
    raise HTTPException(status_code=404, detail='User not found')


@app.put('/user/{user_id}', status_code=204)
def edit_user(user_id: int, user_update: User):
    '''Edit user'''
    user = list(filter(lambda user: user['id_'] == user_id, fake_db))
    if user:
        user[0]['username'] = user_update.username
    else:
        raise HTTPException(status_code=404, detail='User not found')


@app.delete('/user/{user_id}', status_code=204)
def delete_user(user_id: int):
    '''Delete user'''
    user = list(filter(lambda user: user['id_'] == user_id, fake_db))
    if user:
        fake_db.remove(user[0])
    else:
        raise HTTPException(status_code=404, detail='User not found')
