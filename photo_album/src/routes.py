from flask import Blueprint, render_template, redirect, url_for
from . import db
from typing import List, Tuple, Any
from .models import Photo
from.schemas import PhotoCreateSchema

photo_bp = Blueprint('photo_bp', __name__)


@photo_bp.route("/")
def index():
    photos:List[Tuple[Any]] = Photo.query.all()

    return render_template('index.html', photos=photos)

@photo_bp.route("SubirFoto", methods=['POST'])
def create_photo():
    data: Tuple[Any] = request.form
    