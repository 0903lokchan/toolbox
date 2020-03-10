from flask import render_template, request, render_template, url_for, redirect, flash
from flask import current_app

from app import db
from app.post_wall import bp
from app.post_wall.forms import PostForm
from app.post_wall.models import Post

from datetime import datetime

@bp.before_request
def before_request():
    db.session.commit()


@bp.route('/post_wall', methods=['GET', 'POST'])
def main():

    form = PostForm()
    
    if form.validate_on_submit():
        post = Post(name=form.name.data, content=form.content.data)
        db.session.add(post)
        db.session.commit()
        flash('Your Post is now on air!')
        return redirect(url_for('post_wall.main'))

    posts = Post.query.all()

    return render_template('post_wall/main.html', title='Post Wall', posts=posts, form=form)
