# coding=utf-8
"""Deal with image-related APIs."""
from sqlalchemy.exc import IntegrityError
from flask import request
from flask_restplus import Namespace, Resource
from flask_login import login_required, current_user
from ..model import images
from .utils import get_message_json, handle_internal_error, HTTPStatus, ConstantCodes, DBErrorCodes

api = Namespace('images')


@api.route('/<int:image_id>')
class ImageResource(Resource):
    """Deal with single image."""
    
    @login_required
    def get(self, image_id):
        """Retrieve a single image by id."""
        try:
            image_list = images.find_image_by_id(image_id)
            if image_list:
                json_res = image_list[0].to_json()
                json_res['message'] = '图片获取成功'
                return json_res, HTTPStatus.OK
            else:
                return get_message_json('图片不存在'), HTTPStatus.NOT_FOUND
        except IntegrityError as err:
                return handle_internal_error(err.orig.args[1])
        except Exception as err:
            return handle_internal_error(str(err))
    
    @api.doc(parser=api.parser()
             .add_argument('body', type=str, required=True, help='json', location='json')
            )
    @login_required
    def put(self, image_id):
        """Edit a single image by id."""
        form = request.get_json()
        try:
            if not current_user.is_admin():
                return get_message_json("修改图像信息需要管理员权限"), HTTPStatus.UNAUTHORIZED
            if images.find_image_by_id(image_id):
                images.update_image_by_id(
                    image_id,
                    form['label_id'],
                    form['image_state'],
                    form['filename'],
                    form['source']
                )
                if result == 1:
                    json_res = form.copy()
                    json_res['message'] = '图像信息修改成功'
                    return json_res, HTTPStatus.OK
            else:
                return get_message_json('图片未创建'), HTTPStatus.NOT_FOUND

        except IntegrityError as err:
            if err.orig.args[0] == DBErrorCodes.FOREIGN_KEY_FAILURE:
                return get_message_json('指定的标签不存在'), HTTPStatus.BAD_REQUEST
            else:
                return handle_internal_error(err.orig.args[1])

        except Exception as err:
            return handle_internal_error(str(err))

    @login_required
    def delete(self, image_id):
        """Delete an image given an id."""
        try:
            if not current_user.is_admin():
                return get_message_json("删除图像需要管理员权限"), HTTPStatus.UNAUTHORIZED
            result = images.delete_image_by_id(image_id)
            if result == 1:
                return get_message_json('图片删除成功'), HTTPStatus.OK
            else:
                return get_message_json('图片不存在'), HTTPStatus.NOT_FOUND

        except IntegrityError as err:
            return handle_internal_error(err.orig.args[1])

        except Exception as err:
            return handle_internal_error(str(err))


@api.route('/')
class ImagesCollectionResource(Resource):
    """Deal with collection of images."""

    @login_required
    @api.doc(parser=api.parser()
             .add_argument('image_state', type=int, required=False, help='state of image', location='args')
            )
    def get(self):
        """List all images."""
        image_state = request.args.get('image_state')
        try:
            result = images.find_all_images(image_state)
            state_list = []
            for _, state in enumerate(result):
                state_list.append(state.to_json())
            json_res = {'message': '图片集合获取成功',
                        'data': state_list}
            return json_res, HTTPStatus.OK
        
        except IntegrityError as err:
            return handle_internal_error(err.orig.args[1])

        except Exception as err:
            return handle_internal_error(str(err))
    
    @login_required
    @api.doc(parser=api.parser()
             .add_argument('body', type=str, required=True, help='json', location='json')
            )
    def post(self):
        """Create an image."""
        form = request.get_json()
        try:
            if not current_user.is_admin():
                return get_message_json("创建图片需要管理员权限"), HTTPStatus.UNAUTHORIZED
            image_list = images.add_image(
                ConstantCodes.Unassigned,
                form['filename'],
                form['source']
            )
            json_res = image_list.to_json()
            json_res['message'] = '图片创建成功'

            return json_res, HTTPStatus.CREATED
        except IntegrityError as err:
            if err.orig.args[0] == DBErrorCodes.DUPLICATE_ENTRY:
                return get_message_json('图片已存在'), HTTPStatus.CONFLICT
            else:
                return handle_internal_error(err.orig.args[1])

        except Exception as err:
            return handle_internal_error(str(err))
