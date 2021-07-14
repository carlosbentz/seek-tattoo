"""
Função base para verificar erro na entrada dos valores da tabela Style ou que será usada no filtro de busca.
value_list = ["floral", "traço fino", "anime", "aquarela", "preto e branco", "realista", "abstrato", "colorido",...]
"""

from http import HTTPStatus


class InvalidOptionError(Exception):
    def __init__(self, style_name, value_list: list) -> None:

        value_list = ["floral", "traço fino", "anime", "aquarela", "preto e branco", "realista", "abstrato", "colorido"]

        self.message = (
            {
                "error": {
                    "valid options": {value_list},
                    "recieved options": {style_name},
                }
            },
            HTTPStatus.BAD_REQUEST,
        )

        super().__init__(self.message)
