from app.repositories.user_repository import create_user, get_all_users

def add_user(data):
    return create_user(data['name'], data['email'])

def list_users():
    return get_all_users()
