from http import HTTPStatus

class RequiredKeyError(Exception):
    def __init__(self, data: dict, key_list: list) -> None:
        self.message = (
            {"error": {"required_keys": key_list, "recieved_keys": list(data.keys())}},
            HTTPStatus.BAD_REQUEST,
        )

        super().__init__(self.message)
