from app.models import CommentModel
from http import HTTPStatus
from flask import current_app, request, jsonify
from datetime import datetime


def create(comment, user_id, image_id):
    session = current_app.db.session


    comment = CommentModel(comment=comment, user_id=user_id, image_id=image_id, datetime=datetime.now())

    session.add(comment)
    session.commit()

    return jsonify(comment)


def get(image_id):

    comments = {
        "comments": CommentModel.query.filter_by(image_id=image_id).all()
    }

    return jsonify(comments)


def patch(new_comment, comment_id, current_user_id):
    session = current_app.db.session

    comment = CommentModel.query.get(comment_id)

    if not comment.user_id == current_user_id:
        return {"error": "You're not allowed to modify other users comments"}

    comment.comment = new_comment

    session.add(comment)
    session.commit()


    return jsonify(comment)