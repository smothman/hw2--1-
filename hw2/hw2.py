from flask import Flask
import pymysql
from flask import jsonify
from flask import flash, request
app = Flask(__name__)
from flaskext.mysql import MySQL
mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'admin'
app.config['MYSQL_DATABASE_PASSWORD'] = 'pakistan123'
app.config['MYSQL_DATABASE_DB'] = 'CIS3368'
app.config['MYSQL_DATABASE_HOST'] = 'cis3368dall.cmjen6ln1nx7.us-east-2.rds.amazonaws.com'
mysql.init_app(app)


		
@app.route('/api/gem/post', methods=['POST'])
def add_user():
	try:
		_json = request.json
		_gemtype = _json['gemtype']
		_gemcolor = _json['gemcolor']
		_carat = _json['carat']
		_price = _json['price']
		# validate the received values
		if _gemtype and _gemcolor and _carat and _price and request.method == 'POST':
			
			# save edits
			sql = "INSERT INTO CIS3368.gem(gemtype, gemcolor, carat,price) VALUES(%s, %s, %s, %s)"
			data = (_gemtype, _gemcolor,_carat,_price)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			resp = jsonify('Added successfully!')
			resp.status_code = 200
			return resp
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()


		
@app.route('/api/gem/get', methods=['GET'])
def users():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM CIS3368.gem")
		rows = cursor.fetchall()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		

@app.route('/api/gem/put', methods=['PUT'])
def update_user():
	try:
		_json = request.json
		_id = _json['id']
		_gemtype = _json['gemtype']
		_gemcolor = _json['gemcolor']
		_carat = _json['carat']
		_price = _json['price']	
		# validate the received values
		if _gemtype and _gemcolor and _carat and _price and request.method == 'PUT':
			#do not save password as a plain text
			# save edits
			sql = "UPDATE CIS3368.gem SET gemtype=%s, gemcolor=%s, carat=%s, price=%s WHERE id=%s"
			data = (_gemtype, _gemcolor, _carat,_price,_id)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			resp = jsonify('Updated successfully!')
			resp.status_code = 200
			return resp
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
@app.route('/api/gem/delete/<int:id>', methods=['DELETE'])
def delete_user(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM CIS3368.gem WHERE id=%s", (id,))
		conn.commit()
		resp = jsonify('Deleted successfully!')
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp
		
if __name__ == "__main__":
    app.run()