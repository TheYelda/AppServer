import os
from flask import request, current_app, send_from_directory
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

                return get_message_json('头像上传成功'), HTTPStatus.OK

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
        return send_from_directory(os.path.join(os.environ['HOME'], current_app.config['PHOTOS_FOLDER']), filename)


@api.route('/medical-images')
class MedicalImagesCollectionResource(Resource):
    """Deal with collection of medical images."""
    
    @login_required
    @api.doc(parser=api.parser()
             .add_argument('file', type=FileStorage, required=True, help='medical-images', location='files')
            )
    def post(self):
        """upload a madical image."""

        photo_file = request.files['file']
        if photo_file and allowed_file(photo_file.filename):
            photo_filename = secure_filename(photo_file.filename)
            expand_name = photo_filename.rsplit('.', 1)[1]
            photo_filename = current_user.username + '.' + expand_name
            try:
                photo_location = os.path.join(os.environ['HOME'], current_app.config['MEDICAL_IMAGES_FOLDER'])
                photo_file.save(os.path.join(photo_location, photo_filename))

                return get_message_json('医学影像上传成功'), HTTPStatus.OK

            except Exception as err:
                return handle_internal_error(str(err))
        else:
            return get_message_json('医学影像上传失败'), HTTPStatus.BAD_REQUEST


@api.route('/medical-images/<string:filename>')
class MedicalImageResource(Resource):
    """Deal with single medical-images."""
    
    @login_required
    def get(self, filename):
        """retrive a photo."""
        return send_from_directory(os.path.join(os.environ['HOME'], current_app.config['MEDICAL_IMAGES_FOLDER']), filename)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS