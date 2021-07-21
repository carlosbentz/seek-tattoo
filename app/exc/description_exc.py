from http import HTTPStatus


# class MissingKeyError(Exception):
    
#     def __init__(self, data: dict, key_list: list) -> None:

#         self.message = (
#             {"error": {"missing_keys": key_list, "recieved_keys": list(data.keys())}},
#             HTTPStatus.BAD_REQUEST,
#         )

#         super().__init__(self.message)



# POST - verificar se e um artista para cadastrar a descriçao

# GET - verificar se tem alguma descrição, se nao mandar mensagem de erro

# PATCH - verificar se tem descrição e se as chaves estao corretas

# DELETE - verificar se tem descrição e se a descrição a ser deletada é do current_user 