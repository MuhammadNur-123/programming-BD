
from django.db import models
from user.models import User
from instructor.models import Instractor
from blog.models import Blog,Course_Module
from all_course.models import Course
from django.apps import apps

class Enrolled(models.Model):
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

    PAYMENT_METHODS = [
        ('Cash', 'Cash'),
        ('Nogod', 'Nogod'),
        ('Bkash', 'Bkash'),
        ('Rocket', 'Rocket'),
        ('Visa', 'Visa Card'),
        ('Paypal', 'Paypal'),
    ]
    course_name = models.CharField(max_length=25, choices=COURSE_NAME_CHOICES, default='IoT')
    
    enroll_by = models.ForeignKey('user.User', on_delete=models.CASCADE)
    course_module = models.ForeignKey('blog.Course_Module', on_delete=models.CASCADE)
    enroll_date = models.DateField(auto_now_add=True)
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHODS, null=True, blank=True)
    payment_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.enroll_by} enrolled in {self.course_name}"