from django.db import models

# Create your models here.
class ApprovalMessage(models.Model):
    user_id = models.IntegerField()
    realname = models.CharField(max_length=100)  # Field name made lowercase.
    faceimage = models.CharField(max_length=100)  # Field name made lowercase.
    phonenum = models.CharField(max_length=100)  # Field name made lowercase.
    message_type = models.IntegerField()
    message_title = models.CharField(max_length=255, blank=True, null=True)
    message_text = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    tasktype = models.CharField(max_length=100, blank=True, null=True)  # Field name made lowercase.
    money = models.IntegerField(blank=True, null=True)
    deadline = models.CharField(max_length=100, blank=True, null=True)
    ranges = models.IntegerField(blank=True, null=True)
    who = models.CharField(max_length=100, blank=True, null=True)
    update_time = models.DateTimeField()


class Collection(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    collection_type = models.IntegerField(blank=True, null=True)
    object_id = models.IntegerField()
    collect_time = models.DateTimeField(blank=True, null=True)



class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    message_id = models.IntegerField()
    user = models.IntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    updatetime = models.DateTimeField()  # Field name made lowercase.



class Community(models.Model):
    message_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('UserInfo', models.DO_NOTHING)
    message_type = models.CharField(max_length=1)
    message_text = models.CharField(max_length=140, blank=True, null=True)
    message_url = models.CharField(max_length=100, blank=True, null=True)
    update_time = models.DateTimeField()
    praise = models.IntegerField()



class Config(models.Model):
    id = models.IntegerField(primary_key=True)
    pageinfo = models.CharField(max_length=32)
    pageinfo2 = models.CharField(max_length=32)


class DutyInfo(models.Model):
    duty_id = models.AutoField(primary_key=True)
    duty = models.CharField(max_length=10, blank=True, null=True)



class FacesFeatManager(models.Model):
    time = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=256)
    flag = models.CharField(max_length=8)


class FunctionInfo(models.Model):
    function_id = models.AutoField(primary_key=True)
    function_name = models.CharField(unique=True, max_length=10, blank=True, null=True)



class HelpMessage(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_name = models.CharField(max_length=32)
    head_image = models.CharField(max_length=32)
    title = models.CharField(max_length=32)
    time = models.DateTimeField()
    context = models.TextField()
    tasktype = models.CharField(max_length=32)
    money = models.IntegerField()
    deadline = models.CharField(max_length=12)
    ranges = models.IntegerField()
    who = models.CharField(max_length=32)
    phonenum = models.CharField(max_length=12)
    state = models.CharField(max_length=12)



class HibernateSequence(models.Model):
    next_val = models.BigIntegerField(blank=True, null=True)



class Jokes(models.Model):
    joke_id = models.IntegerField()
    joke_text = models.CharField(primary_key=True, max_length=255)



class JpushInfo(models.Model):
    jpush_id = models.IntegerField(unique=True, blank=True, null=True)
    reg_id = models.CharField(max_length=20, blank=True, null=True)



class JqrUsers(models.Model):
    unino = models.CharField(primary_key=True, max_length=21)  # Field name made lowercase.
    name = models.CharField(max_length=30, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(max_length=21, blank=True, null=True)  # Field name made lowercase.


class LoginToken(models.Model):
    id = models.IntegerField(primary_key=True)
    token = models.CharField(max_length=255)
    insert_time = models.DateTimeField()
    delete_time = models.DateTimeField()


class OfficeInfo(models.Model):
    office_id = models.AutoField(primary_key=True)
    office = models.CharField(max_length=10, blank=True, null=True)



class QuestionAnswer(models.Model):
    question_id = models.AutoField(primary_key=True)
    key1 = models.CharField(max_length=20, blank=True, null=True)
    answer = models.CharField(max_length=512, blank=True, null=True)
    question = models.CharField(max_length=255, blank=True, null=True)
    good = models.IntegerField()
    bad = models.IntegerField()
    browse_count = models.IntegerField()
    question_office = models.CharField(max_length=10, blank=True, null=True)



class QuestionDailyconversation(models.Model):
    conversation_id = models.AutoField(primary_key=True)
    conversation_key = models.CharField(max_length=255, blank=True, null=True)
    conversation_question = models.CharField(max_length=255, blank=True, null=True)
    conversation_answer = models.CharField(max_length=255, blank=True, null=True)



class QuestionFunction(models.Model):
    function_id = models.AutoField(primary_key=True)
    function_key = models.CharField(unique=True, max_length=20, blank=True, null=True)
    function_order = models.ForeignKey(FunctionInfo, models.DO_NOTHING, db_column='function_order', blank=True, null=True)
    function_prior = models.IntegerField(blank=True, null=True)



class QuestionRecommender(models.Model):
    qr_id = models.AutoField(primary_key=True)
    question_id = models.IntegerField()
    user_id = models.IntegerField()
    is_recommender = models.IntegerField(blank=True, null=True)



class RecommenderHistory(models.Model):
    community_id = models.IntegerField(primary_key=True)
    recommender_user = models.CharField(max_length=255)
    recommender_count = models.IntegerField()


class RoomInfo(models.Model):
    room_id = models.AutoField(primary_key=True)
    room_num = models.CharField(max_length=10, blank=True, null=True)
    room_name = models.CharField(max_length=20, blank=True, null=True)
    room_image = models.CharField(max_length=200, blank=True, null=True)



class SigninInfo(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_status = models.CharField(max_length=10, blank=True, null=True)
    update_time = models.DateTimeField()


class SigninType(models.Model):
    signin_type = models.CharField(primary_key=True, max_length=10)
    sign_name = models.CharField(max_length=32)


class StaffCheckin(models.Model):
    checkin_id = models.CharField(primary_key=True, max_length=100)
    staff = models.ForeignKey('StaffInfo', models.DO_NOTHING, blank=True, null=True)
    checkin_time = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)



class StaffCheckout(models.Model):
    checkout_id = models.IntegerField(primary_key=True)
    staff = models.ForeignKey('StaffInfo', models.DO_NOTHING, blank=True, null=True)
    checkout_time = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=20)


class StaffFace(models.Model):
    face_id = models.CharField(primary_key=True, max_length=255)
    staff = models.ForeignKey('StaffInfo', models.DO_NOTHING, blank=True, null=True)
    face_time = models.DateTimeField(blank=True, null=True)
    face_image = models.CharField(max_length=255, blank=True, null=True)


class StaffInfo(models.Model):
    staff_id = models.AutoField(primary_key=True)
    staff_name = models.CharField(max_length=10, blank=True, null=True)
    office = models.ForeignKey(OfficeInfo, models.DO_NOTHING, db_column='office', blank=True, null=True)
    duty = models.ForeignKey(DutyInfo, models.DO_NOTHING, db_column='duty', blank=True, null=True)
    room = models.CharField(max_length=20, blank=True, null=True)
    phone1 = models.CharField(max_length=20, blank=True, null=True)
    phone2 = models.CharField(max_length=20, blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    voice = models.CharField(max_length=255, blank=True, null=True)
    sortkey = models.CharField(max_length=20, blank=True, null=True)


class StaffInfo2(models.Model):
    staff_id = models.AutoField(primary_key=True)
    staff_name = models.CharField(max_length=10, blank=True, null=True)
    office = models.CharField(max_length=10, blank=True, null=True)
    duty = models.CharField(max_length=10, blank=True, null=True)
    room = models.CharField(max_length=20, blank=True, null=True)
    phone1 = models.CharField(max_length=20, blank=True, null=True)
    phone2 = models.CharField(max_length=20, blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    voice = models.CharField(max_length=255, blank=True, null=True)
    sortkey = models.CharField(max_length=20, blank=True, null=True)



class TUser(models.Model):
    address = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    nickname = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=10, blank=True, null=True)
    username = models.CharField(max_length=255)



class UnsolvedQuestion(models.Model):
    unsolvedquestion_id = models.AutoField(primary_key=True)
    unsolvedquestion = models.CharField(max_length=255, blank=True, null=True)
    unsolvedquestion_time = models.DateTimeField()
    issolved = models.IntegerField()
    quser = models.ForeignKey('UserInfo', models.DO_NOTHING, blank=True, null=True)
    solved_time = models.DateTimeField(blank=True, null=True)


class UserAttention(models.Model):
    user_id = models.IntegerField()
    attention_id = models.IntegerField()
    attention_rank = models.IntegerField()
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()



class UserFeatptr(models.Model):
    id = models.IntegerField(primary_key=True)
    featptr = models.CharField(max_length=5120)  # Field name made lowercase.


class UserInfo(models.Model):
    idnum = models.CharField(max_length=32, blank=True, null=True)  # Field name made lowercase.
    realname = models.CharField(max_length=64)  # Field name made lowercase.
    jobnum = models.CharField(max_length=64)  # Field name made lowercase.
    phonenum = models.CharField(max_length=32)  # Field name made lowercase.
    password = models.CharField(max_length=32)
    gender = models.CharField(max_length=1)
    sortkey = models.CharField(max_length=32)
    city = models.CharField(max_length=64)
    school = models.CharField(max_length=64, blank=True, null=True)
    faceimage = models.CharField(max_length=32)  # Field name made lowercase.
    rankscore = models.IntegerField()  # Field name made lowercase.
    creditscore = models.IntegerField()  # Field name made lowercase.
    createtime = models.DateTimeField()  # Field name made lowercase.
    job = models.CharField(max_length=32)
    nickname = models.CharField(max_length=32, blank=True, null=True)
    sign = models.CharField(max_length=64, blank=True, null=True)
    admin = models.IntegerField()



class UserProfile(models.Model):
    user_id = models.IntegerField(primary_key=True)
    view_history = models.CharField(max_length=255)



class UsersFeatptr(models.Model):
    featptr = models.TextField()  # Field name made lowercase.
    name = models.CharField(max_length=32, blank=True, null=True)
    realname = models.CharField(max_length=32, blank=True, null=True)  # Field name made lowercase.



class Voice(models.Model):
    voice_id = models.AutoField(primary_key=True)
    patient_id = models.IntegerField()
    user_id = models.IntegerField()
    voice_text = models.CharField(max_length=512, blank=True, null=True)
    voice_url = models.CharField(max_length=255, blank=True, null=True)
    voice_time = models.DateTimeField()

