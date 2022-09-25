from flask import render_template
from app import app
from models import Foods

@app.route('/')
def index():
    page_title = 'SHELF LIFE WEB APP'
    list_foods = Foods.query.order_by(Foods.id)
    return render_template('index.html', page_title=page_title, foods=list_foods)