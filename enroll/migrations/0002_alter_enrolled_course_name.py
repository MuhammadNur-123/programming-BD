# Generated by Django 5.1.1 on 2024-09-28 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrolled',
            name='course_name',
            field=models.CharField(choices=[('Web Development', 'Web Development and Design'), ('Data Science', 'Data Science and Machine Learning'), ('AI Fundamentals', 'Artificial Intelligence Fundamentals'), ('Cloud Computing', 'Cloud Computing and Services'), ('Cybersecurity', 'Cybersecurity Basics'), ('Mobile App Dev', 'Mobile Application Development'), ('Database Systems', 'Database Management Systems'), ('Game Development', 'Game Development and Design'), ('Software Engineering', 'Software Engineering Principles'), ('Blockchain Tech', 'Blockchain Technology'), ('UI/UX Design', 'User Interface and User Experience Design'), ('DevOps Practices', 'DevOps and Continuous Integration'), ('Digital Marketing', 'Digital Marketing Essentials'), ('Big Data Analytics', 'Big Data Analytics'), ('Python Programming', 'Python Programming for Beginners'), ('Network Security', 'Network Security and Ethical Hacking'), ('AI in Healthcare', 'AI Applications in Healthcare'), ('Robotics', 'Robotics and Automation'), ('IoT', 'Internet of Things (IoT)'), ('Cloud Architecture', 'Cloud Architecture and Infrastructure')], default='IoT', max_length=25),
        ),
    ]
