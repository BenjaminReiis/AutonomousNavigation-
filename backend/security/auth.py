from .password import hash_password

from .jwt_manager import create_token



users = [

{

"username":"admin",

"password":
hash_password("admin123"),

"role":"admin"

}

]



def login(
    username,
    password
):

    for user in users:


        if user["username"] == username and \

        user["password"] == hash_password(password):


            return create_token(user)



    return None
