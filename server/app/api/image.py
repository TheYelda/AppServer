# coding=utf-8
"""Deal with image-related APIs."""
from sqlalchemy.exc import IntegrityError
from flask import request, current_app
from flask_restplus import Namespace, Resource
from flask_login import login_required
from werkzeug.security import check_password_hash
from ..model import images
from .utils import get_message_json, handle_internal_error, DB_ERR_CODES, HTTPStatus

api = Namespace('images')

""" ---------- These are for Testing ----------- """
SINGLE_IMAGE_RESPONSE = {
    'message': '',
    'image_id': 10,
    'label_id': 123,
    'state_id': 3,
    'filename': 'test.png',
    'Source': 'abcde'
}
COLLECTION_ACCOUNT_RESPONSE = {
    'message': '',
    'data':
        [
            {
                'image_id': 10,
                'label_id': 123,
                'state_id': 3,
                'filename': 'test1.png',
                'Source': 'abcde'
            },{
                'image_id': 12,
                'label_id': 1245,
                'state_id': 1,
                'filename': 'test2.png',
                'Source': 'abse'
            },{
                'image_id': 11341,
                'label_id': 8923,
                'state_id': 1,
                'filename': 'test3.png',
                'Source': 'oiie'
            }
        ]
}
""" -------------------------------------------- """

@api.route('/<int:image_id>')
class ImageResource(Resource):
    """Deal with single image."""
    
    def get(self, image_id):
        """Retrieve a single image by id."""
        SINGLE_IMAGE_RESPONSE['message'] = '图片获取成功'
        return SINGLE_IMAGE_RESPONSE, HTTPStatus.OK
    
    @api.doc(parser=api.parser()
             .add_argument('filename', type=str, required=True, help='文件名', location='form')
             .add_argument('state', type=str, required=True, help='状态', location='form')
             .add_argument('ground_truth_id', type=str, required=True, help='标签序号', location='form')
             .add_argument('source', type=str, required=True, help='来源', location='form')
             )
    def put(self, image_id):
        """Edit a single image by id."""
        SINGLE_IMAGE_RESPONSE['message'] = '图片更新成功'
        return SINGLE_IMAGE_RESPONSE, HTTPStatus.OK
 
    def delete(self, image_id):
        """Delete a single image by id."""
        return get_message_json('图片删除成功'), HTTPStatus.OK

@api.route('/')
class ImagesCollectionResource(Resource):
    """Deal with collection of images."""

    def get(self):
        """List all images."""
        COLLECTION_ACCOUNT_RESPONSE['message'] = '图片集合获取成功'
        return COLLECTION_ACCOUNT_RESPONSE, HTTPStatus.OK
    
    @api.doc(parser=api.parser()
         .add_argument('filename', type=str, required=True, help='文件名', location='form')
         .add_argument('state', type=str, required=True, help='状态', location='form')
         .add_argument('ground_truth_id', type=str, required=True, help='标签序号', location='form')
         .add_argument('source', type=str, required=True, help='来源', location='form')
         )
    def post(self):
        """Create an image."""
        SINGLE_IMAGE_RESPONSE['message'] = '图片创建成功'
        return SINGLE_IMAGE_RESPONSE, HTTPStatus.CREATED
