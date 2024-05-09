from django.db import models


# Create your models here.
class Questions(models.Model):
    number = models.IntegerField('id', unique=True)
    question = models.TextField('Вопрос')
    question_image = models.ImageField(null=True, blank=True, upload_to="images/", verbose_name='Изображение')
    answer = models.TextField('ответ')

    def __str__(self):
        return self.question


class TestQuestions(models.Model):
    number = models.IntegerField('id', unique=True)
    question = models.TextField('Вопрос')
    options = models.TextField('Варианты Ответов')
    question_image = models.ImageField(null=True, blank=True, upload_to="images/", verbose_name='Изображение')
    answer = models.TextField('ответ')

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Users(models.Model):
    user_id = models.IntegerField('id', unique=True)
    current_question = models.IntegerField('current_question_number')

    def __str__(self):
        return f'{self.user_id}, {self.current_question}'


class UsersQuestionTables(models.Model):
    user_ip = models.CharField('ip', max_length=50)
    current_question = models.IntegerField('current_question_number')

    def __str__(self):
        return f'{self.user_ip}, {self.current_question}'
