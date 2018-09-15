from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required, current_user
from .. import auth
from ..models import User,Pitch,Comments
from .forms import UpdateProfile, PitchForm, CommentPitch
from .. import db,photos



#views
@main.route('/')
def index():
    '''
    View root page function that returns index page and its data
    '''
    title = 'PITCH'

    return render_template('index.html', title = title )   


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    form = UpdateProfile()
    if form.validate_on_submit():
        user.bio = form.bio.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('.profile',uname=user.username))
    return render_template('profile/update.html',form =form)

@main.route('/pitch/technology',methods = ['GET','POST'])
@login_required
def add_category_technology():
    form = PitchForm()
    pitch = Pitch.query.filter_by(category='Technology').all()
    if form.validate_on_submit():
        pitch = Pitch(pitch_title=form.pitch_title.data,category=form.category.data,user=current_user)
        db.session.add(pitch)
        db.session.commit()    
        return redirect(url_for('.index'))
    return render_template('technology.html',category_form = form,pitch=pitch)

@main.route('/comment/technology',methods = ['GET','POST'])
@login_required
def add_comment_technology():
    form = CommentPitch()
    comment = Comments.query.filter_by(category='Technology').all()
    if form.validate_on_submit():
        comment = Comments(comment_title=form.comment_title.data)
        db.session.add(comment)
        db.session.commit()    
        return redirect(url_for('.index'))
    return render_template('technology.html',category_form = form,comment=comment)

@main.route('/pitch/science',methods = ['GET','POST'])
@login_required
def add_category_science():
    form = PitchForm()
    pitch = Pitch.query.filter_by(category='Science').all()
    if form.validate_on_submit():
        pitch = Pitch(pitch_title=form.pitch_title.data,category=form.category.data,user=current_user)
        db.session.add(pitch)
        db.session.commit()    
        return redirect(url_for('.index'))
    return render_template('science.html',category_form = form,pitch=pitch)

@main.route('/comment/science',methods = ['GET','POST'])
@login_required
def add_comment_science():
    form = CommentPitch()
    comment = Comments.query.filter_by(category='Science').all()
    if form.validate_on_submit():
        comment = Comments(comment_title=form.comment_title.data)
        db.session.add(comment)
        db.session.commit()    
        return redirect(url_for('.index'))
    return render_template('science.html',category_form = form,comment=comment)

@main.route('/pitch/entertainment',methods = ['GET','POST'])
@login_required
def add_category_entertainment():
    form = PitchForm()
    pitch = Pitch.query.filter_by(category='Entertainment').all()
    if form.validate_on_submit():
        pitch = Pitch(pitch_title=form.pitch_title.data,category=form.category.data,user=current_user)
        db.session.add(pitch)
        db.session.commit()    
        return redirect(url_for('.index'))
    return render_template('entertainment.html',category_form = form,pitch=pitch)

@main.route('/comment/entertainment',methods = ['GET','POST'])
@login_required
def add_comment_entertainment():
    form = CommentPitch()
    comment = Comments.query.filter_by(category='Science').all()
    if form.validate_on_submit():
        comment = Comments(comment_title=form.comment_title.data)
        db.session.add(comment)
        db.session.commit()    
        return redirect(url_for('.index'))
    return render_template('entertainment.html',category_form = form,comment=comment)

@main.route('/pitch/sports',methods = ['GET','POST'])
@login_required
def add_category_sports():
    form = PitchForm()
    pitch = Pitch.query.filter_by(category='Sports').all()
    if form.validate_on_submit():
        pitch = Pitch(pitch_title=form.pitch_title.data,category=form.category.data,user=current_user)
        db.session.add(pitch)
        db.session.commit()    
        return redirect(url_for('.index'))
    return render_template('sports.html',category_form = form,pitch=pitch)

@main.route('/comment/sports',methods = ['GET','POST'])
@login_required
def add_comment_sports():
    form = CommentPitch()
    comment = Comments.query.filter_by(category='Science').all()
    if form.validate_on_submit():
        comment = Comments(comment_title=form.comment_title.data)
        db.session.add(comment)
        db.session.commit()    
        return redirect(url_for('.index'))
    return render_template('sports.html',category_form = form,comment=comment)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))
