from flask import Flask, render_template, request, redirect, url_for

from models import SessionLocal, WarehouseItem

app = Flask(__name__)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.route('/')
def index():
    with SessionLocal() as db:
        items = db.query(WarehouseItem).all()
    return render_template('index.html', data=items)

@app.route('/edit/<int:item_id>', methods=['GET', 'POST'])
def edit(item_id):
    with SessionLocal() as db:
        item = db.query(WarehouseItem).filter(WarehouseItem.id == item_id).first()
        if request.method == 'POST':
            if item:
                item.name = request.form['name']
                item.quantity = request.form['quantity']
                item.description = request.form['description']
                db.commit()
            return redirect(url_for('index'))
        return render_template('edit.html', item=item)

@app.route('/delete/<int:item_id>', methods=['POST'])
def delete(item_id):
    with SessionLocal() as db:
        item = db.query(WarehouseItem).filter(WarehouseItem.id == item_id).first()
        if item:
            db.delete(item)
            db.commit()
    return redirect(url_for('index'))

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        with SessionLocal() as db:
            new_item = WarehouseItem(
                name=request.form['name'],
                quantity=request.form['quantity'],
                description=request.form['description']
            )
            db.add(new_item)
            db.commit()
        return redirect(url_for('index'))
    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True)
