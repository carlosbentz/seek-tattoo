# SEEK TATTO API



Rotas que necessitam de autorização deve ser informado no cabeçalho da requisição o campo "Authorization", dessa forma:

`Authorization: Bearer {token}`



## Signup

### Request

`Para criar um artista, é necessário enviar "is_artist" como True, caso queira criar um usuário normal, basta ignorar este campo.`

`POST /user/signup`

    {
        "name": <name>: str,
        "email": <email>: str,
        "password": <password>: str,
        "is_artist": <is_artist>: Boolean, NOT REQUIRED
        "description_id": <description_id>: int NOT REQUIRED
    }

### Response

    {
        "User": {
            "name": <name>: str,
            "email": <email>: str,
            "is_artist": <is_artist>: Boolean,
            "description_id": <description_id>: int,
            "id": <id>: int
        },

    }

    HTTP Status: 201 CREATED

## Login

### Request

`POST /user/login`

    {
        "email": <email>: str,
        "password": <password>: str,
    }

### Response

    {
        "message": <token> 
    }

    HTTP Status: 200 OK

## GET ARTIST/ARTISTS

### Request

`GET user/artist`

### Response

    {
        "User": {
            "name": <name>: str,
            "email": <email>: str,
            "is_artist": True: Boolean,
            "description_id": <description_id>: int,
            "id": <id>: int,
            "address": "/user/artist/<user_id>/address",
            "description": "user/artist/<user_id>/description",
            "images": "user/artist/<user_id>/image"
        }
    }

    HTTP Status: 200 OK

### Request

`GET user/artist/<user_id>`

### Response

    {
        "Users": [
            "User": {
                "name": <name>: str,
                "email": <email>: str,
                "is_artist": True: Boolean,
                "description_id": <description_id>: int,
                "id": <id>: int,
                "address": "/user/artist/<user_id>/address",
                "description": "user/artist/<user_id>/description",
                "images": "user/artist/<user_id>/image"
            },
        ]
    }

    HTTP Status: 200 OK

## GET CLIENT/CLIENTS (**PROTECTED**)

### Request

`GET user/client`

### Response

    {
        "Users": [
            "User": {
                "name": <name>: str,
                "email": <email>: str,
                "is_artist": False: Boolean,
                "id": <id>: int
            },
        ]
    }

    HTTP Status: 200 OK

### Request

`GET user/client/<user_id>`

### Response

    {
        "User": {
            "name": <name>: str,
            "email": <email>: str,
            "is_artist": False: Boolean,
            "id": <id>: int
        }
    }

    HTTP Status: 200 OK

## GET USER/USERS (**PROTECTED**)

### Request

`GET user/`

### Response

    {
        "Users": [
            "User": {
                "name": <name>: str,
                "email": <email>: str,
                "is_artist": <is_artist>: Boolean,
                "description_id": <description_id>: int,
                "id": <id>: int
            },
        ]
    }

    HTTP Status: 200 OK

## Alter user (**PROTECTED**)

### Request

`PATCH /user/<user_id>`

**Valid Fields**:

    {
        "name": <name>: str,
        "email": <email>: str,
        "password": <password>: str,
        "is_artist": <is_artist>: Boolean,
        "description_id": <description_id>: int
    }

### Response

    {
        "User": {
            "name": <name>: str,
            "email": <email>: str,
            "is_artist": <is_artist>: Boolean,
            "description_id": <description_id>: int,
            "id": <id>: int
        }
    }

    HTTP Status: 200 OK

## Delete user (**PROTECTED**)

### Request

`Delete /user/<user_id>`

### Response

    {}

    HTTP Status: 204 NO CONTENT

## Create Artist Address (**PROTECTED**)

Para criar um endereço, o usuário deve ser do tipo artista.

### Request

`POST /user/artist/<user_id>/address`

    {
        "city: <city>: str,
        "state": <state>: str,
    }

### Response

    {
        "Address": {
            "city: <city>: str,
            "state": <state>: str,
            "user_id": <user_id>: int
            "id": <id>: int
        }
    }

    HTTP Status: 201 CREATED

## GET ARTIST/ARTISTS ADDRESS

### Request

`GET user/artist/address`

### Response

    {
        "Addresses": [
            "Address": {
                "city: <city>: str,
                "state": <state>: str,
                "user_id": <user_id>: int
                "id": <id>: int
            },
        ]
    }

    HTTP Status: 200 OK

### Request

`GET user/artist/<user_id>/address`

### Response

    {
        "Address": {
            "city: <city>: str,
            "state": <state>: str,
            "user_id": <user_id>: int
            "id": <id>: int
        }
    }

    HTTP Status: 200 OK

## Alter Address (**PROTECTED**)

### Request

`PATCH /user/artist/<user_id>/address`

**Valid Fields**:

    {
        "city: <city>: str,
        "state": <state>: str,
    }

### Response

    {
        "Address": {
            "city: <city>: str,
            "state": <state>: str,
            "user_id": <user_id>: int
            "id": <id>: int
        }
    }

    HTTP Status: 200 OK

## Delete addres (**PROTECTED**)

### Request

`DELETE /user/artist/<user_id>/address`

### Response

    {}

    HTTP Status: 204 NO CONTENT

## Create Artist Description (**PROTECTED**)

### Request

`POST /user/artist/<user_id>/description`

    {
        "experience": <experience>: int,
        "trait": <trait>: str,
        "paint": <paint>: str,
        "description": <description>: str
    }

### Response

    {
        "Description": {
            "experience": <experience>: int,
            "trait": <trait>: str,
            "paint": <paint>: str,
            "description": <description>: str,
            "id": <id>: int
        }
    }

    HTTP Status: 201 CREATED

## GET ARTIST DESCRIPTION

### Request

`GET user/artist/<user_id>/description`

### Response

    {
        "Description": {
            "experience": <experience>: int,
            "trait": <trait>: str,
            "paint": <paint>: str,
            "description": <description>: str,
            "id": <id>: int
        }
    }

    HTTP Status: 200 OK

## Alter Description (**PROTECTED**)

### Request

`PATCH /user/artist/<user_id>/description`

**Valid Fields**:

    {
            "experience": <experience>: int,
            "trait": <trait>: str,
            "paint": <paint>: str,
            "description": <description>: str,
    }

### Response

    {
        "Description": {
            "experience": <experience>: int,
            "trait": <trait>: str,
            "paint": <paint>: str,
            "description": <description>: str,
            "id": <id>: int
        }
    }

    HTTP Status: 200 OK

## Delete description (**PROTECTED**)

### Request

`DELETE /user/artist/<user_id>/description`

### Response

    {}

    HTTP Status: 204 NO CONTENT

## Create Artist Image (**PROTECTED**)

### Request

`POST /user/artist/<user_id>/image`

    {
        "img_url": <img_url>: str,
        "description": <description>: str
    }

### Response

    {
        "Image": {
            "img_url": <img_url>: str,
            "description": <description>: str,
            "user_id": <user_id>: int
            "id": <id>: int
        }
    }

    HTTP Status: 201 CREATED

## GET ARTIST IMAGES

### Request

`GET user/artist/<user_id>/image`

### Response

    {
        "Images": [
            "Image": {
                "img_url": <img_url>: str,
                "description": <description>: str,
                "user_id": <user_id>: int
                "id": <id>: int,
                "comments": "/user/artist/<user_id>/image/<image_id>/comment",
                "styles": "/user/artist/<user_id>/image/<image_id>/style"
            },
        ]
    }

    HTTP Status: 200 OK

### Request

`GET user/artist/<user_id>/image/<image_id>`

### Response

    {
        "Image": {
            "img_url": <img_url>: str,
            "description": <description>: str,
            "user_id": <user_id>: int
            "id": <id>: int
        }
    }

    HTTP Status: 200 OK

## Alter Image (**PROTECTED**)

### Request

`PATCH /user/artist/<user_id>/image/<image_id>`

**Valid Fields**:

    {
        "img_url": <img_url>: str,
        "description": <description>: str,
    }

### Response

    {
        "Image": {
            "img_url": <img_url>: str,
            "description": <description>: str,
            "user_id": <user_id>: int
            "id": <id>: int
        }
    }
    HTTP Status: 200 OK

## Delete image (**PROTECTED**)

### Request

`DELETE /user/artist/<user_id>/image/<image_id>`

### Response

    {}

    HTTP Status: 204 NO CONTENT

## GET STYLES

`Os styles já devem vir previamente criados no banco de dados.`

### Request

`GET /style`

### Response

    {
        "Styles": [
                "Style": {
                    "style_name": <style_name>: str,
                    "style_id": <style_id>: int
                },
        ]
    }

    HTTP Status: 200 OK

### Request

`GET /style/style_id`

### Response

    {
            "Style": {
                "style_name": <style_name>: str,
                "style_id": <style_id>: int
            }
    }

    HTTP Status: 200 OK

## Create Image Style (**PROTECTED**)

`Podem ser atribuídos vários styles a uma mesma imagem.`

### Request

`POST /user/artist/<user_id>/image/<image_id>/style`

    {
        "style_id": <style_id>: int
    }

### Response

    {
        "Image_Style": {
            "image_id": <image_id>:int,
            "style_id: <style_id>: int,
            "id": <id>: int
        }
    }

    HTTP Status: 201 CREATED

## GET IMAGE STYLE

### Request

`GET /user/artist/<user_id>/image/<image_id>/style`

### Response

    {
        "Image_Syles": [
            "Image_Style": {
                "image_id": <image_id>:int,
                "style_id: <style_id>: int,
                "id": <id>: int
            },
        ]
    }

    HTTP Status: 200 OK

## Delete image style (**PROTECTED**)

### Request

`DELETE /user/artist/<user_id>/image/<image_id>/style/<style_id>`

### Response

    {}

    HTTP Status: 204 NO CONTENT

## Create Image Comment (**PROTECTED**)

### Request

`POST /user/artist/<user_id>/image/<image_id>/comment`


    {
        "comment": <comment>: str,
    }

### Response

    {
        "Comment": {
            "comment": <comment>: str,
            "user_id": <user_id>: int,
            "datetime": <datetime>: date,
            "image_id": <image_id>: int,
            "id": <id>: int
        }
    }

    HTTP Status: 201 CREATED

## GET Image Comments

### Request

`GET /user/artist/<user_id>/image/<image_id>/comment`

### Response

    {
        "Comments": [
            "Comment": {
                "comment": <comment>: str,
                "user_id": <user_id>: int,
                "datetime": <datetime>: date,
                "image_id": <image_id>: int,
                "id": <id>: int
            },
        ]
    }

    HTTP Status: 200 OK

## Alter Image Comment (**PROTECTED**)

### Request

`PATCH /user/artist/<user_id>/image/<image_id>/comment/<comment_id>`

**Valid Fields**:

    {
        "comment": <comment>: str,
    }

### Response

    {
        "Comment": {
            "comment": <comment>: str,
            "user_id": <user_id>: int,
            "datetime": <datetime>: date,
            "image_id": <image_id>: int,
            "id": <id>: int
        },
    }
    HTTP Status: 200 OK

## Delete Image Comment (**PROTECTED**)

### Request

`DELETE /user/artist/<user_id>/image/<image_id>/comment/<comment_id>`

### Response

    {}

    HTTP Status: 204 NO CONTENT
