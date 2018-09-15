from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, SelectField
from wtforms.validators import Required


class PitchForm(FlaskForm):
    pitch_title=TextAreaField('Write a pitch title', validators=[Required()])
    category = SelectField('Category', choices=[('Technology','Technology'),('Science','Science'),('Entertainment','Entertainment'),('Sports','Sports')])
    submit = SubmitField('Pitch')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class CategoryForm(FlaskForm):
    pitch_title = TextAreaField('Write a category', validators=[Required()])
    submit = SubmitField('Submit')

class CommentPitch(FlaskForm):
    comment_title = TextAreaField('Write a comment',validators=[Required()])
    submit = SubmitField('Comment')
