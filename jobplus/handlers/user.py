from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_required, current_user
from jobplus.forms import UserproForm

user = Blueprint('user', __name__, url_prefix='/user')


@user.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = UserproForm(obj=current_user)
<<<<<<< HEAD
    #form.resume_urls.data = current_user.resume_urls
    #form.wrok_year.data = current_user.work_year
=======
>>>>>>> ead018915caac62e47b76c3778fa36791cdf20a3
    if form.validate_on_submit():
        form.UserupForm(current_user)
        flash('update success', 'success')
        return redirect(url_for('front.index'))
    return render_template('useprofile.html', form=form)
