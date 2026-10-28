# orders_service.py
#
# Internal orders API. It is not exposed directly: all traffic comes through the
# API gateway (linked repository), which authenticates the caller and sets
# X-User-Id / X-User-Role on the forwarded request.

import sqlite3

from flask import Flask, abort, jsonify, request

app = Flask(__name__)
DB_PATH = "orders.db"


def db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def current_user():
    # Set by the gateway after authentication.
    return request.headers.get("X-User-Id"), request.headers.get("X-User-Role", "user")


@app.get("/internal/users/<int:user_id>/orders")
def user_orders(user_id):
    caller_id, role = current_user()
    if role != "admin" and str(user_id) != caller_id:
        abort(403)
    rows = db().execute(
        "SELECT id, item, amount, created_at FROM orders WHERE user_id = ?", (user_id,)
    ).fetchall()
    return jsonify([dict(row) for row in rows])


@app.get("/internal/admin/orders/export")
def export_orders():
    _, role = current_user()
    if role != "admin":
        abort(403)
    # Admin-only report; the admin UI lets the operator pick the sort column.
    sort = request.args.get("sort", "created_at")
    rows = db().execute(f"SELECT * FROM orders ORDER BY {sort}").fetchall()
    return jsonify([dict(row) for row in rows])


# Nightly BI export, pulled by the analytics job inside the cluster. The gateway only
# forwards /internal/users/* and /internal/admin/*, so this path is not reachable from
# outside and needs no caller identity.
@app.get("/internal/analytics/orders")
def analytics_orders():
    rows = db().execute(
        "SELECT o.id, o.user_id, u.email, u.address, o.item, o.amount, o.created_at "
        "FROM orders o JOIN users u ON u.id = o.user_id"
    ).fetchall()
    return jsonify([dict(row) for row in rows])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)
