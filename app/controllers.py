import json
import urllib
from pprint import pprint

from flask import jsonify

from app import app, db
from app.models import Gps


@app.route('/add', defaults={'data': None})
@app.route('/add/<data>')
def index(data):
	json_result = {}

	if data is not None:
		try:
			data = json.loads(data)
			gps = Gps(sensor=data['sensor'],value=data['value'])
			db.session.add(gps)
			db.session.commit()
		except Exception, e:
			pprint(str(e))

	gps = Gps.query.order_by(Gps.date_created.desc()).first()
	if gps is not None:
		json_result['sensor'] = gps.sensor
		json_result['value'] = gps.value

	return jsonify(json_result)
