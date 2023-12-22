from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:Vaishnavi_mandve@localhost:3306/product_tracking'
db = SQLAlchemy(app)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    status = db.Column(db.String(50))

# Move the create_all inside the application context
with app.app_context():
    # Create the database tables
    db.create_all()

# Endpoint to get the status of a specific product
@app.route('/api/products/<product_id>', methods=['GET'])
def get_product_status(product_id):
    product = Product.query.get(product_id)
    if product:
        return jsonify({"product_id": product.id, "status": product.status})
    else:
        return jsonify({"error": "Product not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
