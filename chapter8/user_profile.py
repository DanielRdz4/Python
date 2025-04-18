#Programa que acepta nombre y apellido, además de una cantidad indefinidad de pares de valores

def build_profile(f_name, l_name="",**user_info):
    """Función que almacena información del usuario"""
    user_info['First name']=f_name
    user_info['Middle name']=l_name
    return user_info


user_profile = build_profile("daniel","Rdz", location='Mexico')

print(user_profile)
