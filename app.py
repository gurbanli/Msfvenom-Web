from flask import Flask, render_template, request, flash, redirect
from forms import GenerateForm
from secrets import token_urlsafe
from sploit import set_cmd


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
            arch = form.arch.data
            set_cmd(payload, encoder, variable_name, payload_format, bad_chars, arch)
            return redirect('/')
    return render_template('index.html', form=form)


@app.after_request
def add_header(req):
    req.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    req.headers["Pragma"] = "no-cache"
    req.headers["Expires"] = "0"
    req.headers['Cache-Control'] = 'public, max-age=0'
    return req


if __name__ == '__main__':
    app.run(host='0.0.0.0')
