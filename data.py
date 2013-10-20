from google.appengine.ext import db

    
class Schools(db.Model):
    name = db.StringProperty()
    term = db.StringProperty()
    year = db.StringProperty()
    
    @property
    def majors(self):
        items = MajorSchool.all().filter('school =', self)
        return items.fetch(1000)
        
        
class Majors(db.Model):
    name = db.StringProperty()
    school = db.StringProperty()
    term = db.StringProperty()
    year = db.StringProperty()
    
    @property
    def courses(self):
        items = CourseMajor.all().filter('major =', self)
        return items.fetch(1000)
        
class Courses(db.Model):
    name = db.StringProperty()
    des = db.TextProperty()
    code = db.StringProperty()
    major = db.StringProperty()
    instructor = db.StringProperty()
    schedule = db.StringProperty()
    school = db.StringProperty()
    term = db.StringProperty()
    year = db.StringProperty()
    credit = db.StringProperty()
    location = db.StringProperty()
    section = db.StringProperty()
    note = db.TextProperty()
    linkup = db.StringProperty()
    InsPer = db.TextProperty()
    url = db.StringProperty()
    
    @property
    def time(self):
        items = Time.all().filter('course =',self)
        return items.fetch(100)


class Time(db.Model):
    day = db.IntegerProperty()
    start = db.FloatProperty()
    end = db.FloatProperty()
    course = db.ReferenceProperty(Courses)

        
class MajorSchool(db.Model):
    school = db.ReferenceProperty(Schools)
    major = db.ReferenceProperty(Majors)
    
class CourseMajor(db.Model):
    major = db.ReferenceProperty(Majors)
    course = db.ReferenceProperty(Courses)
    
class Users(db.Model):
    email = db.UserProperty()
    id = db.StringProperty()

    @property
    def courses(self):
        items = UserCourse.all().filter('user =',self)
        return items.fetch(300)

class UserCourse(db.Model):
    user = db.ReferenceProperty(Users)
    course = db.ReferenceProperty(Courses)
    id = db.StringProperty()
    display = db.StringProperty()

class Feedbacks(db.Model):
    owner = db.EmailProperty()
    time = db.DateTimeProperty()
    content = db.TextProperty()
    