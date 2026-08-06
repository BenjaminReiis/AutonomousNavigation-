def is_admin(user):

    return user.get(
        "role"
    ) == "admin"



def can_control_robot(user):

    roles = [

        "admin",

        "operator"

    ]


    return user.get(
        "role"
    ) in roles
