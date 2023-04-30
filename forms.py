"""Forms for pet app."""
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, NumberRange, Length

class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet name", validators=[InputRequired()],)
    species = SelectField("Species", choices=[("c","Cat"),("d","Dog"),("p","Porcupine")],)
    photo_url = StringField("Pet photo URL", validators=[Optional(), URL()],)
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30)],)
    notes = StringField("Notes", validators=[Optional(), Length(min=10)],)

class EditPetForm(FlaskForm):
    """Form for editing pets."""
    
    photo_url = StringField("Pet photo URL", validators=[Optional(), URL()],)
    notes = StringField("Notes", validators=[Optional(), Length(min=10)],)
    available = BooleanField("Available?")