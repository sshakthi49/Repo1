#!/usr/bin/env python

from flask import Flask, jsonify
from megabank_rest_api import CUSTOMERS, ACCOUNTS
app = Flask(__name__)


@app.route('/', methods=['GET'])
def naked():
    return "GOOD"


@app.route('/customers', methods=['GET'])
def list_customers():
    return jsonify([{'id': key, 'data': CUSTOMERS[key]} for key in CUSTOMERS.keys()])


@app.route('/customers/<customer_id>', methods=['GET'])
def get_customer(customer_id):
    if customer_id not in CUSTOMERS:
        return jsonify({'error': 'Customer %s does not exist' % customer_id}), 404

    return jsonify({'id': customer_id, 'data': CUSTOMERS[customer_id]})


@app.route('/customers/<customer_id>/accounts', methods=['GET'])
def list_customer_accounts(customer_id):
    if customer_id not in CUSTOMERS:
        return jsonify({'error': 'Customer %s does not exist' % customer_id}), 404

    return jsonify([{'id': key, 'data': ACCOUNTS[customer_id][key]} for key in ACCOUNTS[customer_id].keys()])


@app.route('/customers/<customer_id>/accounts/<account_id>', methods=['GET'])
def get_customer_account(customer_id, account_id):
    if customer_id not in CUSTOMERS:
        return jsonify({'error': 'Customer %s does not exist' % customer_id}), 404
    if account_id not in ACCOUNTS[customer_id]:
        return jsonify({'error': 'Account %s for customer %s does not exist' % (account_id, customer_id)}), 404

    return jsonify({'id': account_id, 'data': ACCOUNTS[customer_id][account_id]})
