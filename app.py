"""Flask App Project."""

from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/')
def index():
    """Return homepage."""
#   json_data = {'Hello': 'World!'}
#   return jsonify(json_data)
    return "นายรณทธิ์ แสนสวัสดิ์" เลขที่ 4 ห้อง ม.4/1


if __name__ == '__main__':
    app.run()
