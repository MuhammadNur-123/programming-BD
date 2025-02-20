# Generated by Django 5.1.1 on 2024-09-26 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructor', '0002_instractor_add_instractor_alter_instractor_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instractor',
            name='add_instractor',
        ),
        migrations.AlterField(
            model_name='instractor',
            name='education',
            field=models.CharField(choices=[('PSC', 'Primary School Certificate'), ('SL', 'Select Education Level'), ('JSC', 'Junior School Certificate'), ('SSC', 'Secondary School Certificate'), ('HSC', 'Higher Secondary Certificate'), ('DIP', 'Diploma in Engineering'), ('BSC', 'Bachelor of Science'), ('BA', 'Bachelor of Arts'), ('BBA', 'Bachelor of Business Administration'), ('MSC', 'Master of Science'), ('MA', 'Master of Arts'), ('MBA', 'Master of Business Administration'), ('PHD', 'Doctor of Philosophy')], default='SL', max_length=20),
        ),
        migrations.AlterField(
            model_name='instractor',
            name='excluci',
            field=models.CharField(choices=[('CCO', 'Chief Compliance Officer'), ('SL', 'Select Execlutive Posstion'), ('CPO', 'Chief Product Officer'), ('COO', 'Chief Operating Officer'), ('CEO', 'Chief Executive Officer'), ('CFO', 'Chief Financial Officer'), ('CTO', 'Chief Technology Officer'), ('CIO', 'Chief Information Officer'), ('CMO', 'Chief Marketing Officer'), ('CSO', 'Chief Security Officer'), ('CHRO', 'Chief Human Resources Officer'), ('CAO', 'Chief Analytics Officer'), ('CDAO', 'Chief Data and Analytics Officer'), ('CISO', 'Chief Information Security Officer'), ('CGO', 'Chief Growth Officer')], default='SL', max_length=20),
        ),
        migrations.AlterField(
            model_name='instractor',
            name='instractor_id',
            field=models.CharField(blank=True, default=1, max_length=50, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='instractor',
            name='possiton',
            field=models.CharField(choices=[('WEB', 'Web Developer'), ('MLE', 'Machine Learning Engineer'), ('DS', 'Data Scientist'), ('SL', 'Select Instractor Possition'), ('DBA', 'Database Administrator'), ('SE', 'Software Engineer'), ('UX', 'UX/UI Designer'), ('PM', 'Product Manager'), ('QA', 'Quality Assurance Engineer'), ('CS', 'Cyber Security Specialist'), ('AI', 'AI Researcher'), ('CLOUD', 'Cloud Architect'), ('BI', 'Business Intelligence Analyst'), ('DEVOPS', 'DevOps Engineer'), ('FRONTEND', 'Frontend Developer'), ('BACKEND', 'Backend Developer')], default='SL', max_length=20),
        ),
    ]
