from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from jobplus.config import configs
from flask_login import UserMixin,current_user
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,
                           default=datetime.utcnow,
                           onupdate=datetime.utcnow)


user_job = db.Table(
    'user_job',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id', ondelete='CASCADE')),
    db.Column('job_id', db.Integer, db.ForeignKey('job.id', ondelete='CASCADE'))
)

class User(Base, UserMixin):
    ROLE_JobHunter = 10
    ROLE_Company = 20
    ROLE_ADMIN = 30

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32),index=True, nullable=False)
    email = db.Column(db.String(64), unique=True, index=True, nullable=False)
    _password = db.Column('password', db.String(256), nullable=False)
    real_name = db.Column(db.String(20))
    role = db.Column(db.SmallInteger, default=ROLE_JobHunter)
    phone = db.Column(db.String(11))
    work_years = db.Column(db.SmallInteger) 
    add_jobs = db.relationship('Job', secondary='user_job')
    resume_urls = db.Column(db.String(64))
    detail = db.relationship('Company',uselist=False)
    is_disable = db.Column(db.Boolean,default=False)
 
    @property
    def enable_jobs(self):
        if not self.is_company:
            raise AttributeError('User has no attribute enable_jobs')
        return self.jobs.filter(Job.is_disable.is_(False))
   
   
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, orig_password):
        self._password = generate_password_hash(orig_password)

    def check_password(self, password):
        return check_password_hash(self. _password, password)
   
    @property
    def is_staff(self):
        return self.role == self.ROLE_JobHunter

    @property
    def is_admin(self):
        return self.role == self.ROLE_ADMIN

    @property
    def is_company(self):
        return self.role == self.ROLE_Company


class Job(Base):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    lowsalary = db.Column(db.Integer, nullable=False)
    highsalary = db.Column(db.Integer, nullable=False)
    tags = db.Column(db.String(64))
    location = db.Column(db.String(128))
    education = db.Column(db.String(64))
    work_year = db.Column(db.String(24))
    is_disable = db.Column(db.Boolean,default=False)
    is_open = db.Column(db.Boolean, default=True)
    company_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    company = db.relationship('User', uselist=False,backref=db.backref('jobs',lazy='dynamic'))
    views_count = db.Column(db.Integer,default=0)
   
    @property
    def tag_list(self):
        return self.tags.split(',')
    @property
    def current_user_is_applied(self):
        d = Dilivery.query.filter_by(job_id=self.id,user_id=current_user.id).first()
        return (d is not None)

class Company(Base):
    id = db.Column(db.Integer, primary_key=True)
    logo = db.Column(db.String(256),nullable=False)
    website = db.Column(db.String(64),nullable=False)
    email = db.Column(db.String(24), nullable=False)
    location = db.Column(db.String(24), nullable=False)
    description = db.Column(db.String(24))
    about = db.Column(db.String(1024))
    tags = db.Column(db.String(128))
    stack = db.Column(db.String(128))
    team_introduction = db.Column(db.String(256))
    welfares = db.Column(db.String(256))
    field = db.Column(db.String(128))
    finance_stage = db.Column(db.String(128))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='SET NULL'))
    user = db.relationship('User', uselist=False, backref=db.backref('company', uselist=False))


class Dilivery(Base):
    STATUS_WAITING = 1
    STATUS_REJECT = 2
    STATUS_ACCEPT = 3

    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer, db.ForeignKey('job.id', ondelete='SET NULL'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='SET NULL'))
    company_id = db.Column(db.Integer)
    status = db.Column(db.SmallInteger, default=STATUS_WAITING)

    response = db.Column(db.String(64))

    @property
    def user(self):
        return User.query.get(self.user_id)
    @property
    def job(self):
        return Job.query.get(self.job_id)

