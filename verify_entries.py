from app import app, db, IP

def verify_database_entries():
    with app.app_context():
        ips = IP.query.all()
        for ip in ips:
            print(f"Original IP: {ip.original_ip}, Reversed IP: {ip.reversed_ip}")

if __name__ == "__main__":
    verify_database_entries()
