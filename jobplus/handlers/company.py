<<<<<<< HEAD
from flask import Blueprint, render_template, flash, redirect, url_for,request,current_app
from jobplus.models import User,Job,db,Dilivery
from flask_login import login_required, current_user
from jobplus.forms import ComproForm,JobForm

company = Blueprint('company', __name__, url_prefix='/company')

@company.route('/')
def index():
    page = request.args.get('page',1,type=int)
    pagination = User.query.filter(
            User.role==User.ROLE_Company
    ).order_by(User.created_at.desc()).paginate( 
            page=page,
            per_page=12,
            error_out=False
            ) 
    return render_template('company/index.html',pagination=pagination,active='company')



@company.route('/profile/', methods=['GET', 'POST'])
@login_required
def profile():
    if not current_user.is_company:
        flash('您不是企业用户', 'warning')
        return redirect(url_for('front.index'))
    form = ComproForm(obj=current_user.company)
    if form.validate_on_submit():
        form.ComupForm(current_user)
        flash('企业信息更新成功', 'success')
        return redirect(url_for('front.index'))
    return render_template('comprofile.html', form=form)

@company.route('/<int:company_id>')
def detail(company_id):
    company = User.query.get_or_404(company_id)
    if not company.is_company:
        abort(404)
    return render_template('company/detail.html',company=company,active='',panel='about')

@company.route('/<int:company_id>/jobs')
def company_jobs(company_id):
    company = User.query.get_or_404(company_id)
    if not company.is_company:
        abort(404)
    return render_template('company/detail.html', company=company, active='', panel='job')
@company.route('/<int:company_id>/admin')
@login_required
def admin_index(company_id):
    if not current_user.is_admin and not current_user.id == company_id:
        abort(404)
    page = request.args.get('page',default=1,type=int)
    pagination = Job.query.filter_by(company_id=company_id).paginate(
            page=page,
            per_page=current_app.config['ADMIN_PER_PAGE'],
            error_out=False
    ) 
    return render_template('company/admin_index.html',company_id=company_id,pagination=pagination)

@company.route('/<int:company_id>/admin/publish_job/',methods=['GET','POST'])
@login_required
def admin_publish_job(company_id):
    if current_user.id != company_id:
        abort(404)
    form = JobForm()
    if form.validate_on_submit():
        form.create_job(current_user)
        flash('职位创建成功','success')
        return redirect(url_for('company.admin_index',company_id=current_user.id))
    return render_template('company/publish_job.html',form=form,company_id=company_id)

@company.route('/<int:company_id>/admin/edit_job/<int:job_id>/',methods=['GET','POST'])
@login_required
def admin_edit_job(company_id,job_id):
    if current_user.id != company_id:
        abort(404)
    job = Job.query.get_or_404(job_id) 
    if job.company_id != current_user.id:
        abort(404)
    form = JobForm(obj=job) 
    if form.validate_on_submit():
        form.update_job(job)
        flash('职位更新成功','success')
        return redirect(url_for('company.admin_index',company_id=current_user.id))
    return render_template('company/edit_job.html',form=form,company_id=company_id,job=job)    

@company.route('/<int:company_id>/admin/jobs/<int:job_id>/delete')
@login_required
def admin_delete_job(company_id,job_id):
    if current_user.id != company_id:
        abort(404)
    job = Job.query.get_or_404(job_id) 
    if job.company_id != current_user.id:
        abort(404)
    db.session.delete(job) 
    db.session.commit()
    flash('职位更新成功','success')
    return redirect(url_for('company.admin_index',company_id=current_user.id))


@company.route('/<int:company_id>/admin/apply')
@login_required
def admin_apply(company_id):
    if not current_user.is_admin and not current_user.id == company_id:
        abort(404)
    status = request.args.get('status','all')
    page = request.args.get('page',default=1,type=int)
    q = Dilivery.query.filter_by(company_id=company_id)
    if status == 'waiting':
        q = q.filter(Dilivery.status==Dilivery.STATUS_WAITING)
    elif status == 'accept':
        q = q.filter(Dilivery.status==Dilivery.STATUS_ACCEPT)
    elif status == 'reject':
        q = q.filter(Dilivery.status==Dilivery.STATUS_REJECT)
    pagination = q.order_by(Dilivery.created_at.desc()).paginate(
            page=page,
            per_page=current_app.config['ADMIN_PER_PAGE'],
            error_out=False
            )
    return render_template('company/admin_apply.html',pagination=pagination,company_id=company_id)

@company.route('/<int:company_id>/admin/apply/<int:dilivery_id>/reject/')
@login_required
def admin_apply_reject(company_id,dilivery_id):
    d = Dilivery.query.get_or_404(dilivery_id)
    if current_user.id != company_id:
        abort(404)
    d.status = Dilivery.STATUS_REJECT
    flash('已经拒绝该投递','success')
    db.session.add(d)
    db.session.commit()
    return redirect(url_for('company.admin_apply',company_id=company_id))
@company.route('/<int:company_id>/admin/apply/<int:dilivery_id>/accept/')
@login_required
def admin_apply_accept(company_id,dilivery_id):
    d = Dilivery.query.get_or_404(dilivery_id)
    if current_user.id != company_id:
        abort(404)
    d.status = Dilivery.STATUS_ACCEPT
    flash('已经接受该投递，可以安排面试了','success')
    db.session.add(d)
    db.session.commit()
    return redirect(url_for('company.admin_apply',company_id=company_id))
            


=======
from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_required, current_user
from jobplus.forms import ComproForm

company = Blueprint('company', __name__, url_prefix='/company')


@company.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if not current_user.is_company:
        flash('error', 'warning')
        return redirect(url_for('front.index'))
    form = ComproForm(obj=current_user.company)
    form.name.data = current_user.username
    form.email.data = current_user.email
    if form.validate_on_submit():
        form.ComupForm(current_user)
        flash('success', 'success')
        return redirect(url_for('front.index'))
    return render_template('comprofile.html', form=form)
>>>>>>> ead018915caac62e47b76c3778fa36791cdf20a3
