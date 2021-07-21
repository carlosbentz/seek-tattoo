# SEEK TATTO API

Encontre o artista ideal -
Essa API tem a proposta de oferecer um serviço de busca (atraves de filtros ou não) por tatuadores que fazem parte de nossa rede de cadastro.

# REGRAS DE NEGÓCIO:

1- CADASTRO:

      1.1 - Para poder usar os serviços dessa API é necessário fazer um cadastro.

      1.2 - Todo cadastro se inicia com campos básicos: nome, e-mail, senha, e se o usuario é um artista.

      1.3 - O e-mail é usado como login.

      1.4 - Se o cadastro for feito no formato cliente, o usuário ja esta habilitado a fazer suas pesquisas.

      1.5 - Se o cadastro for feito no formato de artista, o usuário é direcionado a preencher outro cadastro com suas especificações de artista: tempo de experiência, nome do estúdio, traço, tinta, e descrição.

      1.6 - Os usuários/artista precisam indicar em qual estado (indicado pela sigla) e cidade se encontram, para facilitar a busca de um artista que esta próximo ao cliente.

2- FOTOS / COMENTARIOS / ESTILOS:

      2.1 - Para postar uma foto ou comentário é necessário estar logado em sua respectiva conta.

      2.2 - A postagem de imagens é feita, apenas, pelo usuário que tem uma conta no formato artista.

      2.3 - Ao postar uma imagem, o usuário/artista irá selecionar tags que indincam o estilo da arte na imagem em questão, e adicionar uma descrição.

      2.4 - Os comentários são feitos, apenas, pelo usuário que tem uma conta no formato de cliente.

      2.4 - Os comentários são feitos apenas nas imagens. O usuário/cliente pode falar sobre o trabalho em questão ou descrever sua experiência ao ser tatuado pelo usuário/artista.

      2.5 - apenas o usuário/cliente que fez o comentário pode apagar ou editar o comentário feito

      2.6 - Comentários e fotos são publicos, e todos os usuários podem vizualizar.

3- FILTROS E PESQUISA:

      3.1 - Para fazer uma pesquisa é necessario estar logado em sua respectiva conta.

      3.2 - Os filtros funcionam como uma ferramenta para que o usuário/cliente possa achar um usuario/artista que trabalhe com seus estilos de preferência, mesma cidade/estado.

      3.3 - O usuario/cliente pode fazer sua pesquisa selecionando as tags de estilo desejadas, uma cidade/estado, ou tambem inserindo em um campo de busca um nome de estudio, nome do usuário/artista.

      3.4 - O usuario/cliente pode navegar pelas imagens postadas, organizadas pela data de postagem (se iniciando pelas imagens mais recentes), sem utilizar filtros.

    !!!!!!  3.5 - Os perfis de artistas aos quais o cliente se idenfica podem ser salvos como artistas favoritos

4- ATUALIZAÇÃO DE DADOS:

      4.1 - Para fazer alguma alteração em seu cadastro é necesario estar logado em sua respectiva conta.

    !!!!!!  4.2 - Para atualizar o e-mail do cadastro é necessario confirmar a mudança atraves de um link enviado ao novo e-mail.

      4.3 - Para atualizar a senha é necessario indicar a senha antiga primeiro, depois sua nova senha.

    !!!!!!  4.4 - Caso o usuário esquecer a senha será enviado um link atraves do e-mail de cadastro, no qual o usuario poderá atualiza-la

5- DELETE DO USUARIO:

      5.1 - Para apagar um cadastro é necesario estar logado em sua respectiva conta.

      5.2 - A conta pode ser deletada apenas pelo usuário ao qual essa conta pertence.

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
        "token": <token>
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

## GET ALL ARTIST IMAGES

### Request

`GET user/artist/image`

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
