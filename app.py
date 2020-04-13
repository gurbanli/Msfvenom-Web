from flask import Flask, render_template, request, Response, redirect
from forms import GenerateForm
from secrets import token_urlsafe
from sploit import get_options, generate_payload

app = Flask(__name__)
app.config['SECRET_KEY'] = token_urlsafe(16)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    form = GenerateForm()
    if request.method == "POST":
        if form.validate_on_submit():
            payload = form.payloads.data
            encoder = form.encoders.data
            variable_name = form.variable_name.data
            payload_format = form.payload_formats.data
            bad_chars = form.bad_chars.data
            option_names = dict()
            for key in request.form:
                if key.startswith('options'):
                    option_names[key.partition('.')[2]] = request.form[key]
            results = generate_payload(payload, option_names, encoder, variable_name, payload_format, bad_chars)
            print(results)
            generator = (cell for row in results
                         for cell in row)
            return Response(generator,
                            mimetype="application/octet-stream",
                            headers={"Content-Disposition":
                                         f"attachment;filename=payload.{payload_format}"})
        else:
            return redirect('/')
    return render_template('index.html', form=form)


@app.route('/get/<payload>', methods=['POST'])
def get_payload(payload):
    return get_options(payload)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
