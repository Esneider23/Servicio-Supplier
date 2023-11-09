# we invoke the necessary libraries
from flask import jsonify, request

# This function returns the supplier information
def show_supplier(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT idsupplier, name, nit, address, phone, email FROM supplier")
        data = cursor.fetchall()

        if data:
            listSupplier = []
            for fila in data:
                listSupplierGet = {
                    'idsupplier': fila[0],
                    'name': fila[1],
                    'nit': fila[2],
                    'address': fila[3],
                    'phone': fila[4],
                    'email': fila[5]
                }
                listSupplier.append(listSupplierGet)
            return jsonify({'listSupplier': listSupplier, 'message': "List of suppliers"})
        else:
            return jsonify({'message': "There are no data"})
    except Exception as ex:
        return jsonify({'message': "Error: " + str(ex)})
 
# This function updates a data of a supplier
def delete_supplier(connection, idSupplier):
    try:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM supplier WHERE idsupplier = %s", (idSupplier,))
        connection.commit()
        return show_supplier(connection)
    except Exception as ex:
        return jsonify({'message': "Error: " + str(ex)})


# This function deletes a data from a supplier
def update_supplier(connection, idSupplier, data):
    try:
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE supplier SET name = %s, nit = %s, address = %s, phone = %s, email = %s WHERE idsupplier = %s",
            (data['name'], data['nit'], data['address'], data['phone'], data['email'], idSupplier)
        )
        connection.commit()
        return show_supplier(connection)
    except Exception as ex:
        return jsonify({'message': "Error: " + str(ex)})
