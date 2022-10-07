from flask import render_template, request, redirect, url_for, flash
from app import app, db
from models import Foods

# --- READ ---
@app.route('/')
def index():
    page_title = 'SHELF LIFE WEB APP'
    list_foods = Foods.query.order_by(Foods.id)
    return render_template('index.html', page_title=page_title, foods=list_foods)


# --- CREATE ---
@app.route('/new')
def new_register():
    return render_template('new.html', page_title="Registrar novo alimento")


@app.route('/create', methods=['POST',])
def create_register():
    #requisitar as informações do formulário
    food_name = request.form['food']
    food_date = request.form['expiration']
    
    #verificar se o registro já existe no banco de dados
    food = Foods.query.filter_by(food=food_name).first()
    if food:
        flash('Alimento já existe')
        return redirect(url_for('index'))
    
    #criar o novo objeto
    new_food = Foods(food=food_name, expiration=food_date)

    #adicionar no banco de dados
    db.session.add(new_food)
    db.session.commit()

    #redirecionar ao index
    return redirect(url_for('index'))


# --- UPDATE ----
@app.route('/update/<int:id>')
def update_page(id):
    #filtrar a o id que foi passada ao clicar no editar do index e capturar as informações deste registro
    food = Foods.query.filter_by(id=id).first()
    #retornar a página de edição e possibilitar que as informações filtradas sejam exibidas nesta página
    return render_template('update.html', page_title="Registrar novo alimento", food=food)


@app.route('/update_register', methods=['POST',])
def update_register():
    #buscar o id que foi passado na página update da função update_form
    food = Foods.query.filter_by(id=request.form['id']).first()
    #atualizar os valores
    food.food = request.form['food']
    food.expiration = request.form['expiration']
    #registrar as alterações
    db.session.add(food)
    db.session.commit()
    #retornar para página inicial
    return redirect(url_for('index'))


# --- DELETE ---
@app.route('/delete/<int:id>')
def delete_register(id):
    Foods.query.filter_by(id=id).delete()
    db.session.commit()
    flash('Registro deletado com sucesso')
    return redirect(url_for('index'))