# we invoke the necessary libraries
from flask import Flask, render_template, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin
import contraller

# The access point is created
server = Flask(__name__)

CORS(server)

# The connection point to the base is created
server.config['MYSQL_HOST'] = 'us-cdbr-east-06.cleardb.net'
server.config['MYSQL_USER'] = 'bee0e9755133d2'
server.config['MYSQL_PASSWORD'] = 'f3e9360a'
server.config['MYSQL_DB'] = 'heroku_23edc9681868d22'
mysql = MySQL(server)


@cross_origin
# The route to enter the service is created
@server.get('/supplier')
def index():
    try:
        return contraller.show_supplier(mysql)
    except Exception as error:
        return jsonify({"Message": error})


@cross_origin
# this route is created to remove data from this service
@server.delete('/supplier/<id>')
def supplier_delete(id):
    try:
        return contraller.delete_supplier(mysql, id)
    except Exception as ex:
        return page_not_found(ex)


@cross_origin
# this route is created to update data of this service
@server.put('/supplier/<id>')
def supplier_update(id):
    try:
        return contraller.update_supplier(mysql, id)
    except Exception as ex:
        return page_not_found(ex)


@cross_origin
# A function is created to show when a page is not found.
def page_not_found(error):
    return render_template('404.html')


# the application is executed
if __name__ == '__main__':
    server.run(debug=True)