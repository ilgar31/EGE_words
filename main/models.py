from django.db import models


class Words(models.Model):
    word = models.CharField("Слово", max_length=30)
    real_word = models.CharField("Часть речи", max_length=30, default='')
    ind_udar = models.IntegerField("Индекс ударной буквы")

    def __str__(self):
        return self.word

    class Meta:
        verbose_name = "Слово"
        verbose_name_plural = "Слова"
