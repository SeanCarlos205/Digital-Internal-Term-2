from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '82381db102d05bab3f5369a592e18aca'

posts = [
    {
        'author': 'Sean Carlos',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'May 12, 2022'
    },
    {
        'author': 'Eugene Cruz',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'May 13, 2022'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__=='__main__':
    app.run(debug=True)