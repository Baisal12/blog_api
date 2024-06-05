import time
from jwt_handler import encodeJWT, decodeJWT, refreshJWT

user = {"email":"musacojaevbaisalbek@gmail.com", "username":"ASDF12437", "id":1}

jwt_token = encodeJWT(user) # {'access_token':q2jefgvjnmknnjr,'refresh':'bnmkvkbtnrjrgij3i43rojjfekr'}
print(jwt_token)

time.sleep(6)

decoded = decodeJWT(jwt_token['access_token'])
print(decoded)

new_jwt_token = refreshJWT(jwt_token['refresh_token'])
print(new_jwt_token)

