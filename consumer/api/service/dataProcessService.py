
from api.model.recordModel import RecordModel
import datetime
import uuid
#############################################################################
# Class declare in single responsible & Factory method design pattern
#############################################################################
class recordData:

    def __init__(self, data):
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

