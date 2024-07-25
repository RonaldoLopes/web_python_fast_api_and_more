from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(username='teste', email='t@gmail.com', password='323')
    session.add(user)
    session.commit()
    result = session.scalar(select(User).where(User.email == 't@gmail.com'))

    assert result.username == 'teste'
