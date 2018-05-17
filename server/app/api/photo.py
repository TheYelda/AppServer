import os
from flask_restplus import Namespace, Resource
from werkzeug.security import generate_password_hash
from flask import request
from ..model import accounts
from .utils import get_message_json, DB_ERR_CODES, handle_internal_error, HTTPStatus, ConstCodes


api = Namespace('photos')


@api.route('/')
class AccountsPhotosCollectionResource(Resource):
    """Deal with collection of accounts' photos."""
    
    # @api.doc(parser=api.parser()
    #          .add_argument('body', type=str, required=True, help='json', location='json')
    #         )
    def post(self):
        """Create an account."""
        print('get photo')
        photo_file = request.files['file']
        #print(photo_file)
        print(os.path.join(os.getcwd()))
        photo_file.save(os.path.join(os.getcwd() + '/photos', 'test.png'))
        return get_message_json('收到注册图片'), HTTPStatus.OK
