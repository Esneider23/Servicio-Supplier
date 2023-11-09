# we invoke the necessary libraries
from flask import Flask, jsonify
# from config import config
from flask_cors import CORS, cross_origin
import contraller
from db import get_db_connection

# The access point is created
server = Flask(__name__)


#this allow recurser exchange
CORS(server)


@cross_origin
# The route to enter the service is created
@server.get('/supplier')
def index():
    config = get_db_connection()
    if config:
        try:
            return contraller.show_supplier(config)
        except Exception as error:
            return jsonify({"Message": error})
    else:
        return jsonify({'message': 'Error connecting to the database'})

        
# this route is created to remove data from this service
@cross_origin
@server.delete('/supplier/<id>')
def supplier_delete(id):
    try:
        config = get_db_connection()
        if config:
            return contraller.delete_supplier(config, id)
        else:
            return jsonify({'message': 'Error connecting to the database'})
    except Exception as ex:
        return jsonify({'message': str(ex)})


# this route is created to update data of this service
@cross_origin
@server.put('/supplier/<id>')
def supplier_update(id):
    try:
        config = get_db_connection()
        if config:
            return contraller.update_supplier(config, id)
        else:
            return jsonify({'message': 'Error connecting to the database'})
    except Exception as ex:
        return jsonify({'message': str(ex)})



@cross_origin
# A function is created to show when a page is not found.
def page_not_found(error):
    return render_template('404.html')


# the application is executed
if __name__ == '__main__':
    server.run(debug=True)