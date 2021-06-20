import uuid

from django.db import models
from django.urls import reverse


# Create your models here.


class Client(models.Model):
    """
    Model representing an author.
    """
    id_client = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Код кдиента")
    first_name = models.CharField(max_length=100, help_text="Фамилия")
    last_name = models.CharField(max_length=100, help_text="Имя")
    addres = models.CharField(max_length=100, help_text="Имя")
    telephon = models.CharField(max_length=11, help_text="Введите номер телефона 11 чисел")
    id_pass = models.CharField(max_length=10, help_text="Введите серию и номер паспорта")

    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('client-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s, (%s)' % (self.id_client, self.first_name)


class Oborudovanie(models.Model):
    id_oborud = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Код оборудования")
    name_oborud = models.CharField(max_length=100, help_text="Название оборудование")
    type_oborud = models.CharField(max_length=100, help_text="Тип оборудования")
    date_of_priem = models.DateField('приема', null=True, blank=True)
    date_of_sdachi = models.DateField('сдачи', null=True, blank=True)

    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('oborudovanie-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s, %s' % (self.id_oborud, self.name_oborud)


class Vozvrat(models.Model):
    id_voz = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Код возврата")
    nomer_doc = models.CharField(max_length=100, help_text="Номер документа")

    LOAN_STATUS = (
        ("m", "Отличное"),
        ("n", "Хорошее"),
        ("b", "Плохое"),
    )

    status_oborudovania = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m',
                                           help_text='Статус оборудования')

    id_oborud = models.UUIDField(primary_key=False, default=uuid.uuid4, help_text="Код оборудования")
    id_client = models.UUIDField(primary_key=False, default=uuid.uuid4, help_text="Код кдиента")
    shtraf = models.CharField(max_length=10, help_text="Размер штрафа")

    def __str__(self):
        """
        String for representing the Model object
        """
        return '%s (%s)' % (self.id_voz, self.nomer_doc.title)
