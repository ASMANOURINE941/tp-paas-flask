from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/postdata', methods=['POST'])
def post_data():
    # Vérifie que la requête contient du JSON
    if not request.is_json:
        return jsonify({"error": "Requête invalide, JSON requis"}), 400

    # Récupère les données JSON
    data = request.get_json()

    # Vérifie que les données ne sont pas vides
    if data is None:
        return jsonify({"error": "JSON invalide"}), 400

    # Retourne exactement les données reçues
    return jsonify({"received": data}), 200


if __name__ == '__main__':
    app.run(debug=True)

