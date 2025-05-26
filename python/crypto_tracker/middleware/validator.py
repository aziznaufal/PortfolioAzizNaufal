from flask import request, jsonify
from functools import wraps

def validate_json(required_fields):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if not request.is_json:
                return jsonify({"error": "Request must be in JSON format"}), 400

            data = request.get_json()

            # Check required fields
            for field in required_fields:
                if field not in data:
                    return jsonify({"error": f"Missing field: {field}"}), 400

            # Type validation
            if not isinstance(data.get("name"), str):
                return jsonify({"error": "Field 'name' must be a string"}), 400

            if not isinstance(data.get("symbol"), str) or not data["symbol"].isalpha():
                return jsonify({"error": "Field 'symbol' must be letters only"}), 400

            if not isinstance(data.get("price"), (int, float)):
                return jsonify({"error": "Field 'price' must be a number"}), 400

            if not isinstance(data.get("change_24h"), (int, float)):
                return jsonify({"error": "Field 'change_24h' must be a number"}), 400

            # Extra formatting (optional)
            data["symbol"] = data["symbol"].strip().upper()

            # Replace modified data in request context
            request.validated_json = data

            return fn(*args, **kwargs)
        return wrapper
    return decorator
