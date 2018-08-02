from flask_restful import Resource
from xenon_runsDB_api import app, api, mongo


class RunsSubdetector(Resource):
    def get(self, subdetector):
        app.logger.debug('Requesting all runs with subdetector: %s',
                         subdetector)
        cursor = mongo.db.runs_new.find({'detector': subdetector})
        # app.logger.debug('%s', mongo.db.runs_new.find({'status': status}))
        results = [x for x in cursor]
        return results


api.add_resource(RunsSubdetector, '/runs/subdectector/<string:subdetector>/')