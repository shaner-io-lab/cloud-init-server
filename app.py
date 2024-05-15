from flask import Flask, request, send_from_directory, abort
import os
import yaml

app = Flask(__name__)

# Load configuration from YAML file
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

TEMPLATE_DIR = config['template_directory']

@app.route('/cloud-init', methods=['GET'])
def get_cloud_init():
    template_name = request.args.get('template')
    
    if not template_name:
        return "Template query parameter is required", 400
    
    template_path = os.path.join(TEMPLATE_DIR, template_name)
    
    if not os.path.isfile(template_path):
        return "Template not found", 404

    return send_from_directory(TEMPLATE_DIR, template_name)

if __name__ == '__main__':
    app.run(debug=True)
