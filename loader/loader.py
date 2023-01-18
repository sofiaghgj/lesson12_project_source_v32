import logging
from json import JSONDecodeError

from flask import Blueprint, render_template, request
from functions import *
photo_download = Blueprint('photo_download', __name__, template_folder='templates')


@photo_download.route("/post", methods=["GET"])
def page_post_form():
    return render_template("post_form.html")


@photo_download.route("/post", methods=["POST"])
def page_post_upload():
    """ Эта вьюшка обрабатывает форму, вытаскивает из запроса файл """
    # Получаем объект картинки из формы
    picture = request.files.get("picture")
    content = request.form['content']

    if not picture or not content:
        return "ошибка загрузки, нет картинки или тескта"

    if picture.filename.split('.')[-1] not in ['jpeg', 'png']:
        logging.info('Загруженный файл не картинка')
        return 'Загруженный файл - не картинка'

    try:
         picture_path = "/" + save_photo(picture)
    except FileNotFoundError:
        logging.info('Файл не найден')
        return 'Файл не найден'

    except JSONDecodeError:
        return 'Неправильный файл'

    post = save_post({'pic' : picture_path, 'content' : content})

    return render_template("post_uploaded.html", post=post)


