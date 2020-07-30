from flask import Flask, render_template, request, make_response
import db

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        db.add_comment(request.form['comment'])

    search_query = request.args.get('q')

    comments = db.get_comments(search_query)

    r = make_response(render_template('index.html',
                                      comments=comments,
                                      search_query=search_query))

    return r


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
