from flask import Blueprint, render_template, request, jsonify, flash
from .process_data import process_data
from .auth import is_registered_member
routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    return render_template(r'index.html')

@routes.route('/upload', methods=['POST'])
def handle_post_request():
    data = request.get_json().get('image_data')
    id = process_data(data)
    print(id)
    if id:
        if is_registered_member(id):
            flash('Granted')
        else:
            flash("Denied")
    else:
        flash("Denied")
    return jsonify({})