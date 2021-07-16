from http import HTTPStatus


class InvalidOptionError(Exception):
    def __init__(self, style_name, value_options: list) -> None:

        value_options = ["floral", "traço fino", "anime", "aquarela", "preto e branco", "realista", "abstrato", "colorido"]

        self.message = (
            {
                "error": {
                    "valid options": {value_options},
                    "recieved options": {style_name},
                }
            },
            HTTPStatus.BAD_REQUEST,
        )

        super().__init__(self.message)
