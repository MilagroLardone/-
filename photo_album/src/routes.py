from flask import Blueprint, render_template, redirect, url_for, request, jsonify
from . import db
from typing import List, Tuple, Any
from .models import Photo
from.schemas import PhotoCreateSchema

photo_bp = Blueprint('photo_bp', __name__)


@photo_bp.route("/")
def index() -> str:
    photos:List[Tuple[Any]] = Photo.query.all()

    return render_template('index.html', photos=photos)


@photo_bp.route("/SubirFoto")
def new_photo_form() -> str:
   return render_template('photo_form.html')


@photo_bp.route("/foto", methods=['POST'])
def create_photo() -> str:
    data: Tuple[Any] = request.form
    
    try:
        PhotoCreateSchema(title=data[''],
                                       description=data[''],
                                       image=str(data['']))
        
    except ValueError as e:
        return jsonify({"error": e}), 400
    
    new_photo: Photo=Photo(title=data[''],
                                       description=data[''],
                                       image=str(data['']))
    
    db.session.add(new_photo)
    db.session.commit()

    return render_template('photo_item.html', photo=new_photo)

@photo_bp.route("/photo/<int:photo_id>/edit")
def edit_photo_form(photo_id:int) -> str:
    photo: Photo=Photo.query.get_or_404(photo_id)
    return render_template('photo_item.html', photo=photo)

@photo_bp.route("/photo/<int:photo_id>", methods=['DELETE'])
def delete_photo(photo_id:int) -> str:
    photo: Photo=Photo.query.get_or_404(photo_id)
