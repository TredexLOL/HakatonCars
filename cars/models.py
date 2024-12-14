from django.db import models

from django.db import models

class SliderImage(models.Model):
    image = models.ImageField(upload_to='slider/')
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)  # Для сортировки слайдов
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order']  # Сортировка слайдов по порядку

    def __str__(self):
        return self.title if self.title else 'Slider Image'
