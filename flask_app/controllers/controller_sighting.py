from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.model_sighting import Sighting

@app.route('/dashboard')
def dashboard():
    if 'uid' not in session:
        return redirect('/')
    sightings = Sighting.get_all()
    for item in sightings:
        item.skeptics_num()
    return render_template('dashboard.html', sightings=sightings)

@app.route('/sighting/<int:id>')
def s_show(id):
    if 'uid' not in session:
        return redirect('/')
    sighting = Sighting.get_one({'sid': id})
    sighting.skeptics_peo_name()
    sighting.skeptics_peo_id()
    return render_template('s_show.html', sighting=sighting)

@app.route('/sighting/add')
def s_add():
    if 'uid' not in session:
        return redirect('/')
    return render_template('s_add.html')

@app.route('/process_s_add', methods=['POST'])
def process_s_add():
    if not Sighting.validate(request.form):
        return redirect('/sighting/add')
    data = {
        **request.form,
        'user_id': session['uid'],
        'user_fname': session['first_name'],
        'user_lname': session['last_name']
    }
    sid = Sighting.create(data)
    return redirect(f'/sighting/{sid}')
    
@app.route('/sighting/edit/<int:id>')
def s_edit(id):
    if 'uid' not in session:
        return redirect('/')
    sighting = Sighting.get_one({'sid': id})
    session['sighting'] = {
        'sid': sighting.id,
        'location': sighting.location,
        'happen': sighting.happen,
        'date': sighting.date,
        'num': sighting.num,
    }
    return render_template('s_edit.html')

@app.route('/process_s_edit', methods=['POST'])
def process_s_edit():
    if not Sighting.validate(request.form):
        return redirect(f'/sighting/edit/{session["sighting"]["sid"]}')
    data = {
        **request.form,
        'sid': session['sighting']['sid']
    }
    Sighting.edit(data)
    return redirect(f'/sighting/{session["sighting"]["sid"]}')
    # Where to free session['recipe'] is best?
    # I do clear session in logout route, maybe it's not bad?

@app.route('/sighting/delete/<int:id>')
def recipe_delete(id):
    Sighting.delete({'sid': id})
    return redirect('/dashboard')

@app.route('/process_believe/<int:id>', methods=['POST'])
def process_believe(id):
    Sighting.believe({'uid': session['uid'], 'sid': id})
    return redirect(f'/sighting/{id}')

@app.route('/process_skeptic/<int:id>', methods=['POST'])
def process_skeptic(id):
    Sighting.skeptic({'uid': session['uid'], 'sid': id})
    return redirect(f'/sighting/{id}')