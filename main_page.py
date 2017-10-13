from flask import Blueprint, render_template, abort, request
from jinja2 import TemplateNotFound

main_page = Blueprint('main_page', __name__,
                        template_folder='templates')

@main_page.route('/', defaults={'page': 'index'})

@main_page.route('/<page>')
def show(page):
    try:
        return render_template('pages/%s.html' % page)
    except TemplateNotFound:
        abort(404)