import os
import logging
from flask import Flask, request, jsonify, render_template

logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)

feedback_summary = {"presentacion": {}, "proyectos": {}}


def normalize_word(word):
    """Convierte una palabra a una forma base (minúscula, singular)."""
    clean_word = word.lower().strip()

    if len(clean_word) > 2 and clean_word.endswith('s'):
        clean_word = clean_word[:-1]

    return clean_word


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/recibir-feedback', methods=['POST'])
def recibir_feedback():
    global feedback_summary
    try:
        data = request.get_json()
        if not data or 'presentacion_summary' not in data or 'proyecto_summary' not in data:
            return jsonify({'error': 'Missing required keys'}), 400

        presentacion_key = normalize_word(data['presentacion_summary'])
        proyecto_key = normalize_word(data['proyecto_summary'])

        if presentacion_key:
            feedback_summary["presentacion"][
                presentacion_key] = feedback_summary["presentacion"].get(
                    presentacion_key, 0) + 1

        if proyecto_key:
            feedback_summary["proyectos"][
                proyecto_key] = feedback_summary["proyectos"].get(
                    proyecto_key, 0) + 1

        app.logger.info(f"Feedback summary updated: {feedback_summary}")
        return jsonify({
            'status': 'success',
            'message': 'Feedback received successfully'
        }), 200

    except Exception as e:
        app.logger.error(f"Error processing feedback: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500


@app.route('/get-feedback', methods=['GET'])
def get_feedback():
    return jsonify(feedback_summary)


@app.route('/clear-feedback', methods=['POST'])
def clear_feedback():
    global feedback_summary
    feedback_summary = {"presentacion": {}, "proyectos": {}}
    app.logger.info("Feedback data has been cleared.")
    return jsonify({"status": "cleared"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
