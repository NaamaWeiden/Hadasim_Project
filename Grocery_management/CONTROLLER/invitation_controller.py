from flask import request
from server import app
from DTO.invitation import invitation
import STORE.invitation_store as store
import json
from flask import Flask, request, jsonify

@app.route('/add_invitation', methods=['POST'])
def add_invitation():
    try:
        data = request.json
        invitation = invitation(
            invitation_id=data['invitation_id'],
            product_name=data['product_name'],
            company_name=data['company_name'],
            quantity=data['quantity'],
            total_payment=0
        )
        store.add_invitation(invitation)
        return json.dumps({"status": "success"}), 200
    except Exception as e:
        return json.dumps({"error": str(e)}), 400


@app.route('/get_supplier_invitations', methods=['GET'])
def get_supplier_invitations():
    company_name = request.args.get('company_name')
    if not company_name:
        return jsonify({'error': 'Missing company_name'}), 400

    invitations = store.get_invitations_by_supplier(company_name)
    return jsonify({'invitations': invitations}), 200


@app.route('/update_invitation_status', methods=['POST'])
def update_invitation_status():
    data = request.json
    invitation_id = data.get('invitation_id')
    new_status = data.get('status')

    if not invitation_id or not new_status:
        return jsonify({'error': 'Missing data'}), 400

    success = store.update_invitation_status(invitation_id, new_status)
    if success:
        return jsonify({'message': 'Status updated successfully'}), 200
    else:
        return jsonify({'error': 'Invitation not found or not updated'}), 404


@app.route('/get_all_invitations', methods=['GET'])
def get_all_invitations():
    try:
        invitations = store.get_all_invitations()
        return jsonify(invitations), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route('/get_in_process_invitations', methods=['GET'])
def get_in_process_invitations():
    try:
        invitations = store.get_in_process_invitations()
        return jsonify(invitations), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route('/complete_invitation/<invitation_id>', methods=['PUT'])
def complete_invitation(invitation_id):
    try:
        success = store.update_invitation_status_to_completed(invitation_id)
        if success:
            return jsonify({"message": "הסטטוס עודכן להושלמה"}), 200
        else:
            return jsonify({"error": "הזמנה לא נמצאה"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route('/get_completed_invitations/<company_name>', methods=['GET'])
def get_completed_invitations(company_name):
    try:
        invitations = store.get_completed_invitations_for_supplier(company_name)
        return jsonify(invitations), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
