# coding=utf-8
"""Deal with label-related APIs."""
from flask_restplus import Namespace, Resource, reqparse
from flask_login import login_required
from flask import request
from ..model import labels
from http import HTTPStatus
from .utils import get_message_json, handle_internal_error

api = Namespace('labels')

""" ---------- These are for Testing ----------- """
SINGLE_LABEL_RESPONSE = {
    'message': '',
    'label_id': 123,
    'quality': False,
    'dr': True,
    'stage_id': 2,
    'dme': True,
    'hr_id': 3,
    'age_dme_id': 3,
    'rvo': False,
    'crao': False,
    'od': False,
    'glaucoma': False,
    'others': True,
    'comment': 'no'
}
COLLECTION_LABEL_RESPONSE = {
    'message': '',
    'data':
        [
            {
                'label_id': 123,
                'quality': False,
                'dr': True,
                'stage_id': 2,
                'dme': True,
                'hr_id': 3,
                'age_dme_id': 3,
                'rvo': False,
                'crao': False,
                'od': False,
                'glaucoma': False,
                'others': True,
                'comment': 'no'
            },{
                'label_id': 143,
                'quality': False,
                'dr': True,
                'stage_id': 2,
                'dme': True,
                'hr_id': 3,
                'age_dme_id': 3,
                'rvo': False,
                'crao': False,
                'od': False,
                'glaucoma': False,
                'others': True,
                'comment': 'no'
            },{
                'label_id': 1213,
                'quality': False,
                'dr': True,
                'stage_id': 2,
                'dme': True,
                'hr_id': 3,
                'age_dme_id': 3,
                'rvo': False,
                'crao': False,
                'od': False,
                'glaucoma': False,
                'others': True,
                'comment': 'no'
            }
        ]
}
""" -------------------------------------------- """

@api.route('/<int:label_id>')
class LabelResource(Resource):
    """Deal with single label."""

    def get(self, label_id):
        """Retrieve a single label by id."""
        SINGLE_LABEL_RESPONSE['message'] = '标签获取成功'
        return SINGLE_LABEL_RESPONSE, HTTPStatus.OK
    
    @api.doc(parser=api.parser()
             .add_argument('quality', type=bool, required=True, help='图片质量', location='form')
             .add_argument('dr', type=bool, required=True, help='是否有糖尿病视网膜病变', location='form')
             .add_argument('stage', type=int, required=True, help='所处阶段', location='form')
             .add_argument('dme', type=bool, required=True, help='是否有糖尿病性黄斑水肿', location='form')
             .add_argument('hr', type=int, required=True, help='高血压视网膜病变阶段', location='form')
             .add_argument('age_dme', type=int, required=True, help='年龄相关性黄斑水肿阶段', location='form')
             .add_argument('rvo', type=bool, required=True, help='是否有视网膜静脉阻塞', location='form')
             .add_argument('crao', type=bool, required=True, help='是否有视网膜动脉阻塞', location='form')
             .add_argument('myopia', type=bool, required=True, help='', location='form')
             .add_argument('od', type=bool, required=True, help='是否有病理性近视', location='form')
             .add_argument('glaucoma', type=bool, required=True, help='是否有青光眼', location='form')
             .add_argument('others', type=bool, required=True, help='是否有其他疾病', location='form')
             .add_argument('comment', type=str, required=True, help='备注', location='form')
             )
    def put(self, label_id):
        SINGLE_LABEL_RESPONSE['message'] = '标签修改成功'
        return SINGLE_LABEL_RESPONSE, HTTPStatus.OK

    def delete(self, label_id):
        """Delete a single label by id."""
        return get_message_json('标签删除成功'), HTTPStatus.NO_CONTENT

@api.route('/')
class LabelsCollectionResource(Resource):
    """Deal with collection of labels."""

    @api.doc(parser=api.parser()
             .add_argument('quality', type=bool, required=True, help='图片质量', location='form')
             .add_argument('dr', type=bool, required=True, help='是否有糖尿病视网膜病变', location='form')
             .add_argument('stage', type=int, required=True, help='所处阶段', location='form')
             .add_argument('dme', type=bool, required=True, help='是否有糖尿病性黄斑水肿', location='form')
             .add_argument('hr', type=int, required=True, help='高血压视网膜病变阶段', location='form')
             .add_argument('age_dme', type=int, required=True, help='年龄相关性黄斑水肿阶段', location='form')
             .add_argument('rvo', type=bool, required=True, help='是否有视网膜静脉阻塞', location='form')
             .add_argument('crao', type=bool, required=True, help='是否有视网膜动脉阻塞', location='form')
             .add_argument('myopia', type=bool, required=True, help='', location='form')
             .add_argument('od', type=bool, required=True, help='是否有病理性近视', location='form')
             .add_argument('glaucoma', type=bool, required=True, help='是否有青光眼', location='form')
             .add_argument('others', type=bool, required=True, help='是否有其他疾病', location='form')
             .add_argument('comment', type=str, required=True, help='备注', location='form')
             )
    def post(self):
        """Create a label."""
        SINGLE_LABEL_RESPONSE['message'] = '标签创建成功'
        return SINGLE_LABEL_RESPONSE, HTTPStatus.CREATED
