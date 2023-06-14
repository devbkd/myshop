from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True, verbose_name='Код')
    valid_from = models.DateTimeField(verbose_name='Действителен от')
    valid_to = models.DateTimeField(verbose_name='Действителен до')
    discount = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text='Процентное значение (от 0 до 100)',
        verbose_name='Скидка',
    )
    active = models.BooleanField(verbose_name='Активный')

    class Meta:
        verbose_name = 'Купон'
        verbose_name_plural = 'Купоны'

    def __str__(self):
        return self.code
        # return 'Купон: {}'.format(self.code)
