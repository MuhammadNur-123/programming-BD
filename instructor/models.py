from django.db import models
from user.models import User
from django.apps import apps



class Instractor(models.Model):
    # Choices
    USER_TYPE_CHOICES1 = [
        ('PSC', 'Primary School Certificate'),
       ('SL', 'Select Education Level'),
        ('JSC', 'Junior School Certificate'),
        ('SSC', 'Secondary School Certificate'),
        ('HSC', 'Higher Secondary Certificate'),
        ('DIP', 'Diploma in Engineering'),
        ('BSC', 'Bachelor of Science'),
        ('BA', 'Bachelor of Arts'),
        ('BBA', 'Bachelor of Business Administration'),
        ('MSC', 'Master of Science'),
        ('MA', 'Master of Arts'),
        ('MBA', 'Master of Business Administration'),
        ('PHD', 'Doctor of Philosophy'),
    ]
    
    COUNTRY_NAME_CHOICES = [
        ('SL', 'Select Country Name'),
        ('BD', 'Bangladesh'),
        ('IN', 'India'),
        ('US', 'United States'),
        ('CA', 'Canada'),
        ('AU', 'Australia'),
        ('GB', 'United Kingdom'),
        ('CN', 'China'),
        ('JP', 'Japan'),
       ('DE', 'Germany'),
       ('FR', 'France'),
        ('ZA', 'South Africa'),
    ('RU', 'Russia'),
    ('MX', 'Mexico'),
    ('IT', 'Italy'),
    ('ES', 'Spain'),
    ('NG', 'Nigeria'),
    ('AR', 'Argentina'),
    ('SA', 'Saudi Arabia'),
    ('KR', 'South Korea'),
    ('ID', 'Indonesia'),
    ('TR', 'Turkey'),
    ('EG', 'Egypt'),
    ('PK', 'Pakistan'),
    ('NL', 'Netherlands'),
    ('SE', 'Sweden'),
    ('CH', 'Switzerland'),
    ('BE', 'Belgium'),
    ('PL', 'Poland'),
    ('MY', 'Malaysia'),
    ('PH', 'Philippines'),
    ('TH', 'Thailand'),
    ('IR', 'Iran'),
    ('IQ', 'Iraq'),
    ('VN', 'Vietnam'),
    ('IL', 'Israel'),
    ('NO', 'Norway'),
    ('FI', 'Finland'),
    ('NZ', 'New Zealand'),
    ('SG', 'Singapore'),
    ('AE', 'United Arab Emirates'),
    ('GR', 'Greece'),
    ('PT', 'Portugal'),
    ('CZ', 'Czech Republic'),
    ('HU', 'Hungary'),
    ('AT', 'Austria'),
    ('DK', 'Denmark'),
    ('IE', 'Ireland'),
    ('CL', 'Chile'),
    ('RO', 'Romania'),
    ('KE', 'Kenya'),
        # Add other countries...
    ]

    INSTRUCTOR_POSITION = [
        ('WEB', 'Web Developer'),
        ('MLE', 'Machine Learning Engineer'),
        ('DS', 'Data Scientist'),
        ('SL', 'Select Instractor Possition'),
        ('DBA', 'Database Administrator'),
        ('SE', 'Software Engineer'),
        ('UX', 'UX/UI Designer'),
        ('PM', 'Product Manager'),
        ('QA', 'Quality Assurance Engineer'),
        ('CS', 'Cyber Security Specialist'),
        ('AI', 'AI Researcher'),
        ('CLOUD', 'Cloud Architect'),
        ('BI', 'Business Intelligence Analyst'),
        ('DEVOPS', 'DevOps Engineer'),
        ('FRONTEND', 'Frontend Developer'),
        ('BACKEND', 'Backend Developer'),
    ]

    EXECUTIVE_POSITIONS = [
        ('CCO', 'Chief Compliance Officer'),
        ('SL', 'Select Execlutive Posstion'),
        ('CPO', 'Chief Product Officer'),
        ('COO', 'Chief Operating Officer'),
        ('CEO', 'Chief Executive Officer'),
        ('CFO', 'Chief Financial Officer'),
        ('CTO', 'Chief Technology Officer'),
        ('CIO', 'Chief Information Officer'),
        ('CMO', 'Chief Marketing Officer'),
        ('CSO', 'Chief Security Officer'),
        ('CHRO', 'Chief Human Resources Officer'),
        ('CAO', 'Chief Analytics Officer'),
        ('CDAO', 'Chief Data and Analytics Officer'),
        ('CISO', 'Chief Information Security Officer'),
        ('CGO', 'Chief Growth Officer'),
        # Add more executive positions as necessary...
    ]

    # Fields
    # add_instractor=models.ForeignKey('user.User',on_delete=models.CASCADE,blank=True)
    email = models.EmailField(verbose_name="email address", max_length=255, unique=True)
    name = models.CharField(max_length=50, blank=True)
    instractor_id = models.CharField(max_length=50, blank=True)
    excluci = models.CharField(max_length=20, choices=EXECUTIVE_POSITIONS, default='SL')
    education = models.CharField(max_length=20, choices=USER_TYPE_CHOICES1, default='SL')
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    
    date_of_birth = models.DateField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    country = models.CharField(max_length=20, choices=COUNTRY_NAME_CHOICES, default='SL')
    possiton = models.CharField(max_length=20, choices=INSTRUCTOR_POSITION, default='SL')
    linkdlen_id = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='instractor_image/', blank=True, null=True)
    
    def __str__(self):
        return self.name
   



