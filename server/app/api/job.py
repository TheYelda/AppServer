# coding=utf-8
"""Deal with job-related APIs."""
from flask import request
from flask_restplus import Namespace, Resource
from flask_login import login_required, current_user
from ..model import jobs, accounts
from .utils import get_message_json, handle_internal_error, HTTPStatus

api = Namespace('jobs')

""" ---------- These are for Testing ----------- """
SINGLE_JOB_RESPONSE = {
    'message': '',
    'job_id': 132,
    'image_id': 81768,
    'doctor_id': 17,
    'state': 'unassigned',
    'finished_date': '2018-01-01',
    'label_id': 3
}
COLLECTION_JOB_RESPONSE = {
    'message': '',
    'data':
        [
            {
                'job_id': 132,
                'image_id': 81768,
                'doctor_id': 17,
                'state': 'unassigned',
                'finished_date': '2018-01-01',
                'label_id': 3
            },{
                'job_id': 142,
                'image_id': 814168,
                'doctor_id': 14,
                'state': 'unassigned',
                'finished_date': '2018-03-01',
                'label_id': 3
            },{
                'job_id': 1345,
                'image_id': 513168,
                'doctor_id': 72,
                'state': 'unassigned',
                'finished_date': '2018-02-01',
                'label_id': 3
            }
        ]
}
""" -------------------------------------------- """


@api.route('/<int:job_id>')
class JobResource(Resource):
    """Deal with single job."""

    def get(self, job_id):
        """Retrieve a single job by id."""
        SINGLE_JOB_RESPONSE['message'] = '图片获取成功'
        return SINGLE_JOB_RESPONSE, HTTPStatus.OK

    @api.doc(parser=api.parser()
             .add_argument('image_id', type=str, required=True, help='图片ID', location='form')
             .add_argument('doctor_id', type=str, required=True, help='医生ID', location='form')
             .add_argument('label_id', type=str, required=True, help='标签ID', location='form')
             .add_argument('state', type=str, required=True, help='任务状态', location='form')
             .add_argument('finished_date', type=str, required=True, help='任务完成日期', location='form')
             )
    def put(self, job_id):
        """Edit a single job by id."""
        SINGLE_JOB_RESPONSE['message'] = '任务修改成功'
        return SINGLE_JOB_RESPONSE, HTTPStatus.OK

    def delete(self, job_id):
        """Delete a single job by id."""
        return get_message_json('任务删除成功'), HTTPStatus.NO_CONTENT


@api.route('/')
class JobsCollectionResource(Resource):
    """Deal with collection of jobs."""

    def get(self):
        """List all jobs."""
        COLLECTION_JOB_RESPONSE['message'] = '任务集合获取成功'
        return COLLECTION_JOB_RESPONSE, HTTPStatus.OK
    
    @api.doc(parser=api.parser()
             .add_argument('image_id', type=str, required=True, help='图片ID', location='form')
             .add_argument('doctor_id', type=str, required=True, help='医生ID', location='form')
             )
    def post(self):
        """Create a job."""
        SINGLE_JOB_RESPONSE['message'] = '任务创建成功'
        return SINGLE_JOB_RESPONSE, HTTPStatus.CREATED

