from flask import request,  jsonify, current_app
from api.model.recordModel import RecordModel
import datetime
import uuid
#############################################################################
# Class declare in single responsible & Factory method design pattern
#############################################################################
class recordData:

    def __init__(self, data=None):
        self.data = data
        pass

    def set(self):
        try:
            record = RecordModel(
                id=str(uuid.uuid4()),
                name=self.data['name'],
                email=self.data['email'],
                updated_at=datetime.datetime.now(),
            )
            record.save()
            return record
        except Exception as msg:
            print("{} already exist...".format(self.data['email']))
            pass

    def list(self, page):

        record_list = RecordModel.query.order_by('updated_at').paginate(int(page), per_page=current_app.config['DATA_PERPAGE'])

        result = [
            {
                'id': row.id,
                'name': row.name,
                'email': row.email,
            } for row in record_list.items]

        response_object = {
            'code': 200,
            'type': 'Success',
            'message': 'Data found',
            'data': result,
            'paginate': {
                'pages': record_list.pages,
                'page': record_list.page,
                'per_page': record_list.per_page,
                'total': record_list.total,
                'prev_num': record_list.prev_num,
                'next_num': record_list.next_num,
                'has_prev': record_list.has_prev,
                'has_next': record_list.has_next
            }
        }
        return response_object
