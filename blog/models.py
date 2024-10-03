from django.db import models
from user.models import User
from instructor.models import Instractor
from all_course.models import Course

# Create your models here.
class Blog(models.Model):
    COURSE_NAME_CHOICES = [
    ('Web Development', 'Web Development and Design'),
    ('Data Science', 'Data Science and Machine Learning'),
    ('AI Fundamentals', 'Artificial Intelligence Fundamentals'),
    ('Cloud Computing', 'Cloud Computing and Services'),
    ('Cybersecurity', 'Cybersecurity Basics'),
    ('Mobile App Dev', 'Mobile Application Development'),
    ('Database Systems', 'Database Management Systems'),
    ('Game Development', 'Game Development and Design'),
    ('Software Engineering', 'Software Engineering Principles'),
    ('Blockchain Tech', 'Blockchain Technology'),
    ('UI/UX Design', 'User Interface and User Experience Design'),
    ('DevOps Practices', 'DevOps and Continuous Integration'),
    ('Digital Marketing', 'Digital Marketing Essentials'),
    ('Big Data Analytics', 'Big Data Analytics'),
    ('Python Programming', 'Python Programming for Beginners'),
    ('Network Security', 'Network Security and Ethical Hacking'),
    ('AI in Healthcare', 'AI Applications in Healthcare'),
    ('Robotics', 'Robotics and Automation'),
    ('IoT', 'Internet of Things (IoT)'),
    ('Cloud Architecture', 'Cloud Architecture and Infrastructure')
]

    
    blog_name=models.CharField(max_length=30,choices=COURSE_NAME_CHOICES,default='IoT')
    author=models.ForeignKey(Instractor, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.blog_name
class Course_Module(models.Model):
    COURSE_NAME_CHOICES = [
    ('Web Development', 'Web Development and Design'),
    ('Data Science', 'Data Science and Machine Learning'),
    ('AI Fundamentals', 'Artificial Intelligence Fundamentals'),
    ('Cloud Computing', 'Cloud Computing and Services'),
    ('Cybersecurity', 'Cybersecurity Basics'),
    ('Mobile App Dev', 'Mobile Application Development'),
    ('Database Systems', 'Database Management Systems'),
    ('Game Development', 'Game Development and Design'),
    ('Software Engineering', 'Software Engineering Principles'),
    ('Blockchain Tech', 'Blockchain Technology'),
    ('UI/UX Design', 'User Interface and User Experience Design'),
    ('DevOps Practices', 'DevOps and Continuous Integration'),
    ('Digital Marketing', 'Digital Marketing Essentials'),
    ('Big Data Analytics', 'Big Data Analytics'),
    ('Python Programming', 'Python Programming for Beginners'),
    ('Network Security', 'Network Security and Ethical Hacking'),
    ('AI in Healthcare', 'AI Applications in Healthcare'),
    ('Robotics', 'Robotics and Automation'),
    ('IoT', 'Internet of Things (IoT)'),
    ('Cloud Architecture', 'Cloud Architecture and Infrastructure')
]


    course_name =models.CharField(max_length=30,choices=COURSE_NAME_CHOICES,default='IoT')
    modules = models.TextField(blank=True)

    def __str__(self):
        return f"{self.course_name} - {self.modules}"  # Return a meaningful string
