from django.db import models
from shop.models import Product


class Order(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    email = models.EmailField(verbose_name='Эл.почта')
    address = models.CharField(max_length=250, verbose_name='Адресс')
    postal_code = models.CharField(
        max_length=20, verbose_name='Почтовый индекс'
    )
    city = models.CharField(max_length=100, verbose_name='Город')
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата создания'
    )
    updated = models.DateTimeField(
        auto_now=True, verbose_name='Дата обновления'
    )
    paid = models.BooleanField(default=False, verbose_name='Оплачено')

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created']),
        ]
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Order {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        related_name='items',
        on_delete=models.CASCADE,
        verbose_name='Заказ',
    )
    product = models.ForeignKey(
        Product,
        related_name='order_items',
        on_delete=models.CASCADE,
        verbose_name='Товар',
    )
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Цена'
    )
    quantity = models.PositiveIntegerField(
        default=1, verbose_name='Количество'
    )

    class Meta:
        verbose_name = 'Заказать товар'
        verbose_name_plural = 'Заказать товары'

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity
