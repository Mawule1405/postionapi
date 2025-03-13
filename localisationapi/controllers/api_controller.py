from flask import Blueprint, request, jsonify
from ..services.pole_service import PoleService

api = Blueprint('api', __name__)
pole_service = PoleService()


@api.route('/nearest-pole', methods=['GET'])
def nearest_pole():
    try:
        lat = float(request.args.get('latitude'))
        lon = float(request.args.get('longitude'))
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid coordinates"}), 400

    pole = pole_service.get_nearest_pole( lon , lat)

    return jsonify(pole) if pole else (jsonify({"error": "No pole found"}), 404)