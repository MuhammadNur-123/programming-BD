
from django.db import models

class Course(models.Model):
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


    image = models.ImageField(
        upload_to='course_image/', 
        blank=True, 
        null=True
    )

    course_name = models.CharField(max_length=25, choices=COURSE_NAME_CHOICES, default='IoT')
    
    # ForeignKey fields using lazy referencing to avoid circular imports
    entry_course = models.ForeignKey('user.User', on_delete=models.SET_NULL, null=True, blank=True)
    instractor = models.ForeignKey('instructor.Instractor', on_delete=models.CASCADE, null=True, blank=True)
    blogs = models.ForeignKey('blog.Blog', on_delete=models.CASCADE, null=True, blank=True)
    

    course_code = models.CharField(max_length=13, unique=True)
    start_class = models.DateField(blank=True, null=True)
    course_time = models.TimeField(blank=True, null=True)
    course_length = models.CharField(max_length=8, blank=True, null=True)  # Fixing the typo "course_lenght"
    total_sit = models.IntegerField(blank=True, null=True)  # Made it nullable
    course_fee = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.course_name
