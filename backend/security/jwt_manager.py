from datetime import datetime, timedelta

import jwt


SECRET_KEY = "ROBOT_SECRET_KEY"



def create_token(user):

    payload = {

        "user": user,

        "exp":
        datetime.utcnow()
        +
        timedelta(hours=8)

    }


    return jwt.encode(

        payload,

        SECRET_KEY,

        algorithm="HS256"

    )



def verify_token(token):

    try:

        return jwt.decode(

            token,

            SECRET_KEY,

            algorithms=["HS256"]

        )

    except:

        return None
