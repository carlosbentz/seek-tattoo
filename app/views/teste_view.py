from flask import Blueprint


bp = Blueprint("teste", __name__, url_prefix="/api")


@bp.get("/")
def create():

    return {"home": "hello world"}
