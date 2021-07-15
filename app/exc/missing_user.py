from http import HTTPStatus

class NotFoundUser(Exception):

    def __init__(self, user_id: int) -> None:

        self.message = (
            {
                "error": f"'NOT FOUND {user_id}'"
            }, HTTPStatus.NOT_FOUND,
        )

        super().__init__(self.message)