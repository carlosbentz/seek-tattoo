from http import HTTPStatus


class MissingKeyError(Exception):
    
    def __init__(self, data: dict, key_list: list) -> None:

        self.message = (
            {"error": {"missing_keys": key_list, "recieved_keys": list(data.keys())}},
            HTTPStatus.BAD_REQUEST,
        )

        super().__init__(self.message)
        