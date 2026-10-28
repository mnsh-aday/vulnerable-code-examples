from flask import request, render_template_string

# User input is rendered as data and escaped by Jinja
@app.route('/hello')
def hello():
    username = request.args.get('username')
    template = "<p>Hello {{ username }}</p>"
    return render_template_string(template, username=username)