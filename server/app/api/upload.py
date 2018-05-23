# coding=utf-8
import os
from flask import request, current_app, send_file
from flask_restplus import Namespace, Resource
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
from ..model import accounts
from .utils import get_message_json, handle_internal_error, HTTPStatus

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

api = Namespace('uploads')


@api.route('/photos')
class PhotosCollectionResource(Resource):
    """Deal with collection of accounts' photos."""
    
    @login_required
    @api.doc(parser=api.parser()
             .add_argument('file', type=FileStorage, required=True, help='photo', location='files')
            )
    def post(self):
        """upload a photo."""

        photo_file = request.files['file']
        if photo_file and allowed_file(photo_file.filename):
            photo_filename = secure_filename(photo_file.filename)
            expand_name = photo_filename.rsplit('.', 1)[1]
            photo_filename = current_user.username + '.' + expand_name
            try:
                photo_location = os.path.join(os.environ['HOME'], current_app.config['PHOTOS_FOLDER'])
                photo_file.save(os.path.join(photo_location, photo_filename))

                return get_message_json('头像上传成功'), HTTPStatus.CREATED

            except Exception as err:
                return handle_internal_error(str(err))
        else:
            return get_message_json('头像上传失败'), HTTPStatus.BAD_REQUEST


@api.route('/photos/<string:filename>')
class PhotoResource(Resource):
    """Deal with single photos."""
    
    @login_required
    def get(self, filename):
        """retrive a photo."""

        photo_file_path = os.path.join(os.environ['HOME'], current_app.config['PHOTOS_FOLDER'], filename)
        if os.path.exists(photo_file_path):
            try:
                return send_file(photo_file_path)
            except Exception as err:
                return handle_internal_error(str(err))
        else:
            return get_message_json('头像不存在'), HTTPStatus.NOT_FOUND


@api.route('/medical-images')
class MedicalImagesCollectionResource(Resource):
    """Deal with collection of medical images."""
    
    @login_required
    @api.doc(parser=api.parser()
             .add_argument('file', type=FileStorage, required=True, help='medical-images', location='files')
            )
    def post(self):
        """upload a madical image."""

        medical_file = request.files['file']
        if medical_file and allowed_file(medical_file.filename):
            medical_filename = secure_filename(medical_file.filename)
            expand_name = medical_filename.rsplit('.', 1)[1]
            medical_filename = current_user.username + '.' + expand_name
            try:
                medical_location = os.path.join(os.environ['HOME'], current_app.config['MEDICAL_IMAGES_FOLDER'])
                medical_file.save(os.path.join(medical_location, medical_filename))

                return get_message_json('医学影像上传成功'), HTTPStatus.CREATED

            except Exception as err:
                return handle_internal_error(str(err))
        else:
            return get_message_json('医学影像上传失败'), HTTPStatus.BAD_REQUEST


@api.route('/medical-images/<string:filename>')
class MedicalImageResource(Resource):
    """Deal with single medical-images."""
    
    @login_required
    def get(self, filename):
        """retrive a medical image."""
        
        medical_file_path = os.path.join(os.environ['HOME'], current_app.config['PHOTOS_FOLDER'], filename)
        if os.path.exists(medical_file_path):
            try:
                return send_file(medical_file_path)
            except Exception as err:
                return handle_internal_error(str(err))
        else:
            return get_message_json('头像不存在'), HTTPStatus.NOT_FOUND


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
