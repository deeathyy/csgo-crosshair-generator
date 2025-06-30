from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
    data = request.json

    commands = []
    commands.append(f"cl_crosshairstyle {data['crosshairstyle']}")
    commands.append(f"cl_crosshaircolor {data['crosshaircolor']}")

    if data['crosshaircolor'] == '5':
        commands.append(f"cl_crosshaircolor_r {data['crosshaircolor_r']}")
        commands.append(f"cl_crosshaircolor_g {data['crosshaircolor_g']}")
        commands.append(f"cl_crosshaircolor_b {data['crosshaircolor_b']}")

    commands.append(f"cl_crosshairsize {data['crosshairsize']}")
    commands.append(f"cl_crosshairthickness {data['crosshairthickness']}")
    commands.append(f"cl_crosshairgap {data['crosshairgap']}")
    commands.append(f"cl_crosshairdot {data['crosshairdot']}")
    commands.append(f"cl_crosshair_drawoutline {data['crosshair_drawoutline']}")
    commands.append(f"cl_crosshair_outlinethickness {data['crosshair_outlinethickness']}")

    return jsonify({"commands": "\n".join(commands)})


if __name__ == '__main__':
    app.run(debug=True)