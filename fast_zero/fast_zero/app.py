from fastapi import FastAPI
from http import HTTPStatus
from fast_zero.schemas import Message, UserSchema

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá mundo'}

@app.post('/users/')
def create_user(user: UserSchema):
    ...

# https://www.youtube.com/watch?v=WnhDgVLYfx0&list=PLOQgLBuj2-3IuFbt-wJw2p2NiV9WTRzIP
# 19:40