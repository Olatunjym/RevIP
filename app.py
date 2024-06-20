from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ips.db'
db = SQLAlchemy(app)

class IP(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_ip = db.Column(db.String(50), nullable=False)
    reversed_ip = db.Column(db.String(50), nullable=False)

tables_created = False

@app.before_request
def create_tables():
    global tables_created
    if not tables_created:
        db.create_all()
        tables_created = True

@app.route('/')
def reverse_ip():
    client_ip = request.remote_addr
    reversed_ip = '.'.join(client_ip.split('.')[::-1])
    # Store the IPs in the database
    new_ip = IP(original_ip=client_ip, reversed_ip=reversed_ip)
    db.session.add(new_ip)
    db.session.commit()
    return f"Reversed IP: {reversed_ip}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
