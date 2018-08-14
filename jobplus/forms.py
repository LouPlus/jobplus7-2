from flask_wtf import FlaskForm
<<<<<<< HEAD
from wtforms import StringField, PasswordField, SubmitField, BooleanField,ValidationError,TextAreaField,IntegerField,SelectField
from wtforms.validators import Length, Email, EqualTo, Required
from jobplus.models import db, User,Company,Job


class RegisterForm(FlaskForm):
    username = StringField('用户名',validators=[Required(),Length(2,12)])
=======
from wtforms import StringField, PasswordField, SubmitField, BooleanField,ValidationError,TextAreaField
from wtforms.validators import Length, Email, EqualTo, Required
from jobplus.models import db, User,Company


class RegisterForm(FlaskForm):
    username = StringField('用户名',validators=[Required(),Length(4,12)])
>>>>>>> ead018915caac62e47b76c3778fa36791cdf20a3
    email = StringField('邮箱', validators=[Required(), Email()])   
    password = PasswordField('密码', validators=[Required(), Length(6, 24)])
    repeat_password = PasswordField('确认密码', validators=[Required(), EqualTo('password')])
    submit = SubmitField('提交')

    def validate_username(self,field):
        if User.query.filter_by(username=field.data).first():
                raise ValidationError('用户名已存在')
    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
                raise ValidationError('邮箱已存在')
    def create_user(self):
        user = User()
        user.username = self.username.data
        user.email = self.email.data
        user.password = self.password.data
        db.session.add(user) 
        db.session.commit()
        return user
class LoginForm(FlaskForm):
    email = StringField('邮箱', validators=[Required(), Email()])
    password = PasswordField('密码', validators=[Required(), Length(6, 24)])
    remember_me = BooleanField('记住密码')
    submit = SubmitField('提交')

    def validate_email(self,field):
        if field.data and not User.query.filter_by(email=field.data).first():
            raise ValidationError('该邮箱未注册')
    def validate_password(self,field):
        user = User.query.filter_by(email=self.email.data).first()
        if user and not user.check_password(field.data):
            raise ValidationError('密码错误')

class UserproForm(FlaskForm):

    real_name = StringField('姓名')
    email = StringField('邮箱',validators=[Required(),Email()])
    password = PasswordField('密码',validators=[Required(),Length(6,24)])
<<<<<<< HEAD
    work_years = StringField('工作经验')
    phone = StringField('手机号码')
    resume_urls = StringField('简历')
=======
    work_year = StringField('工作经验')
    phone = StringField('手机号码')
    resume_url = StringField('简历')
>>>>>>> ead018915caac62e47b76c3778fa36791cdf20a3
    submit = SubmitField('提交')
    def validate_phone(self,field):
        if field.data[:2] not in ('13','15','18') and len(field.data)!=11:
           raise ValidationError('请输入正确的手机号')
    
    def UserupForm(self,user):
        user.real_name = self.real_name.data
        user.email = self.email.data
        if self.password.data:
           user.password = self.password.data
<<<<<<< HEAD
        user.work_years = self.work_years.data
        user.phone = self.phone.data
        user.resume_urls = self.resume_urls.data
        self.populate_obj(user)   
=======
        user.work_year = self.work_year.data
        user.phone = self.phone.data
        user.resume_url = self.resume_url.data
     
>>>>>>> ead018915caac62e47b76c3778fa36791cdf20a3
        db.session.add(user)
        db.session.commit()
class ComproForm(FlaskForm):
    name = StringField('公司名称') 
    email = StringField('邮箱',validators=[Required(),Email()])
    password = PasswordField('密码')
    location = StringField('公司地址',validators=[Required(),Length(0,64)])
<<<<<<< HEAD
    website = StringField('公司主页',validators=[Required(),Length(0,64)])
    logo = StringField('公司Logo',validators=[Required()])
    field = StringField('公司领域',validators=[Required(),Length(0,64)])
    description = StringField('一句话描述',validators=[Length(0,100)])
    about = TextAreaField('关于公司',validators=[Length(0,1024)])
    finance_stage = StringField('融资阶段',validators=[Required()]) 
=======
    site = StringField('公司主页',validators=[Required(),Length(0,64)])
    logo = StringField('公司Logo',validators=[Required()])
    description = StringField('一句话描述',validators=[Length(0,100)])
    about = TextAreaField('关于公司',validators=[Length(0,1024)])
>>>>>>> ead018915caac62e47b76c3778fa36791cdf20a3
    submit = SubmitField('提交')

    def ComupForm(self,user):
       user.username = self.name.data
       user.email = self.email.data
       user.role = 20
<<<<<<< HEAD
       if self.password:
           user.password =self.password.data
=======
       if self.password.data:
          user.password = self.password.data
>>>>>>> ead018915caac62e47b76c3778fa36791cdf20a3
       if user.company:
          company = user.company
       else:
          company = Company()
          company.user_id = user.id
       self.populate_obj(company)  
       db.session.add(user)
       db.session.add(company)
       db.session.commit()
<<<<<<< HEAD
class UserEditForm(FlaskForm):
     email = StringField('邮箱',validators=[Required(),Email()])
     password = PasswordField('密码')
     real_name = StringField('姓名')
     phone = StringField('手机号')
     submit = SubmitField('提交')

     def update(self,user):
         self.populate_obj(user)
         if self.password.data:
             user.password = self.password.data
         db.session.add(user)
         db.session.commit()
class CompanyEditForm(FlaskForm):
     username = StringField('企业名称')
     email = StringField('邮箱',validators=[Required(),Email()])
     password = PasswordField('密码')
     phone = StringField('手机号')
     website = StringField('公司网站',validators=[Length(0,64)])
     description = StringField('一句话简介',validators=[Length(0,100)])
     submit = SubmitField('提交')

     def update(self,company):
         company.username = self.username.data
         company.email = self.email.data
         company.phone = self.phone.data
         if self.password.data:
             company.password = self.password.data
         if company.detail:
             detail = company.detail
         else:
             detail = Company()
             detail.user_id = company.id
         detail.website = self.website.data    
         detail.description = self.description.data
         db.session.add(company)
         db.session.add(detail)
         db.session.commit()

class JobForm(FlaskForm):
    name = StringField('职位名称',validators=[Required()])
    lowsalary = IntegerField('最低薪酬')
    highsalary = IntegerField('最高薪酬')
    location = StringField('工作地点',validators=[Required()])
    tags = StringField('职位标签(多个用,隔开)',validators=[Required()])
    work_year = SelectField(
        '经验要求(年)',
        choices=[
            ('不限', '不限'),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('1-3', '1-3'),
            ('3-5', '3-5'),
            ('5+', '5+')
        ]
    )
    education = SelectField(
       '学历要求',
        choices=[
            ('不限', '不限'),
            ('专科', '专科'),
            ('本科', '本科'),
            ('硕士', '硕士'),
            ('博士', '博士')
        ]
    )
    description = TextAreaField('职位描述', validators=[Length(0, 1500)])
    submit = SubmitField('发布')

    def create_job(self, company):
        job = Job()
        self.populate_obj(job)
        job.company_id = company.id
        db.session.add(job)
        db.session.commit()
        return job

    def update_job(self, job):
        self.populate_obj(job)
        if job.company:
           company = job.company
        company.detail.description = self.description.data

        db.session.add(company)
        db.session.add(job)
        db.session.commit()
        
        return job         
=======
>>>>>>> ead018915caac62e47b76c3778fa36791cdf20a3
