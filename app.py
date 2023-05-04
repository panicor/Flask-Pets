"""Flask app for pet app."""
from flask import Flask, render_template, redirect, flash, url_for
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pets'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'hey'
app.debug = True

toolbar = DebugToolbarExtension(app)

connect_db(app)
with app.app_context():
    db.create_all()

@app.route("/")
def home():
    """List all pets."""
    pets = Pet.query.all()
    return render_template("pet_list.html", pets=pets)

@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Add a pet."""
    
    form = AddPetForm()

    if form.validate_on_submit():
        name  = form.name.data
        species = form.species.data
        image_url = form.image_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data

        new_pet = Pet(name=name, species=species, image_url=image_url, age=age, notes=notes, available=available)

        db.session.add(new_pet)
        db.session.commit()

        flash(f"{new_pet.name} added")

        return redirect(url_for('list_pets'))
    
    else:
        return render_template("pet_add_form.html", form=form) 
    # return render_template("pet_list.html")

@app.route("/<int:pet_id>", methods=["GET", "POST"])
def edit_pet(pet_id):
    """Edit a pet."""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.image_url = form.image_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()
        flash(f"{pet.name} updated")
        return redirect(url_for("list_pets"))
    else:
        return render_template("pet_edit_form.html", form=form, pet=pet)
    