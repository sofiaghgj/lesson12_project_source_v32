from json import JSONDecodeError
import logging
from flask import render_template, Blueprint, request
from functions import *

show_photo = Blueprint('show_photo', __name__, template_folder='templates')


@show_photo.route('/')
def page_index():
    posts = read_file()
    return render_template("index.html", posts=posts)


@show_photo.route("/search/")
def page_tag():
    s = request.args.get('s', "")
    logging.info('Выполняю поиск')
    try:
        posts = search(s)
    except FileNotFoundError:
        logging.error('файл не найден')
        return 'файл не найден'

    except JSONDecodeError:
        return 'Неправильный файл'

    return render_template("post_list.html", s=s, posts=posts)
