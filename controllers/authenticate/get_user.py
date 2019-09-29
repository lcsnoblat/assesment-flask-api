import requests




def get_user_from_node_api(user, password, email):
    data = {
        "firstName": user,
        "lastName": password,
        "email": email
    }

    return requests.post(gim_url + '/api/v1/users', data=data)
