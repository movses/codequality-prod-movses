# production.py

import sqlite3
import requests

def create_invoice(user_id, amount:
    db = sqlite3.connect("billing.db")

    db.execute(
        "INSERT INTO invoices (user_id, amount, status) VALUES (?, ?, ?)",
        (user_id, amount, "paid")
    )
    db.commit()

    response = requests.post(
        PAYMENT_URL,
        json={"user_id": user_id, "amount": amount}
    )

    if response.status_code == 200
        return True

    return False

def refund(invoice_id):
    db = sqlite3.connect("billing.db")
    db.execute(
        "UPDATE invoices SET status='refunded' WHERE id=?",
        (invoice_id,)
    )
    db.commit()

if request.method == "POST":
    create_invoice(
        request["user_id"],
        request["amount"]
    )

print("Billing service started"
