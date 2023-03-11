from django.db import models
from captcha.fields import ReCaptchaField


class Application(models.Model):
    name = models.CharField('Имя', max_length=15)
    email = models.EmailField('E-mail')
    phone = models.CharField('Телефон', max_length=20)
    comment = models.TextField('Вопрос', max_length=250)
    date = models.DateTimeField('Дата обращения', auto_now_add=True)
    status = models.BooleanField('Статус', default=False)
    captcha = ReCaptchaField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


class News(models.Model):
    title = models.CharField('Заголовок', max_length=20)
    text = models.TextField('Текст')
    img = models.ImageField('Изображение')
    vision = models.BooleanField('Черновик', default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class GAGAGA(models.Model):
    img = models.ImageField('Изображение')

    def __str__(self):
        return self.img.name

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'


class Review(models.Model):
    name = models.CharField('Имя', max_length=15)
    date = models.DateTimeField('Дата и время', auto_now_add=True)
    company = models.CharField('Компания', max_length=250)
    review = models.TextField('Отзыв')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
