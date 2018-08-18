from django.db import models

from django.utils import timezone
from django.urls import reverse

from accounts.models import Enterprise
from accounts.models import User

# Create your models here.
class Annonce(models.Model):
    LANGUAGES_FRENCH = 'FR'
    LANGUAGES_ENGLISH = 'EN'

    OFFER_CDI = 'CDI'
    OFFER_CDD = 'CDD'
    OFFER_FREELANCE = 'FRE'
    OFFER_STAGE = 'STA'
    OFFER_ALTERNANCE = 'ALT'
    OFFER_FULLTIME = 'FUL'
    OFFER_HALFTIME = 'HAL'

    FIELD_UI = 'UI'
    FIELD_FRONT_END = 'FE'
    FIELD_BACK_END = 'BA'
    FIELD_APP = 'AP'
    FIELD_INFO_ARCHITECTURE = 'AR'
    FIELD_CONTENT_STRATEGY = 'CS'
    FIELD_MANAGEMENT = 'MA'
    FIELD_SOCIAL_MEDIA = 'SM'
    FIELD_MISCELLARY = 'MI'

    LANGUAGES_CHOICES = (
        (LANGUAGES_FRENCH,'French'),
        (LANGUAGES_ENGLISH, 'English'),
    )

    OFFER_CHOICES = (
        (OFFER_CDI,'CDI'),
        (OFFER_CDD, 'CDD'),
        (OFFER_FREELANCE,'Freelance'),
        (OFFER_STAGE, 'Stage'),
        (OFFER_ALTERNANCE,'Alternance'),
        (OFFER_FULLTIME, 'Temps plein'),
        (OFFER_HALFTIME, 'Temps partiel'),
    )

    JOB_FIELDS_CHOICES = (
        (FIELD_UI, 'UI design'),
        (FIELD_FRONT_END, 'Front-end development'),
        (FIELD_BACK_END, 'Back-end development'),
        (FIELD_APP, 'App Development'),
        (FIELD_INFO_ARCHITECTURE, 'Information Architecture'),
        (FIELD_CONTENT_STRATEGY, 'Content Strategy'),
        (FIELD_MANAGEMENT, 'Management'),
        (FIELD_SOCIAL_MEDIA, 'Social Media Expert'),
        (FIELD_MISCELLARY, 'Miscellary'),
    )

    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, null=True)
    enterprise = models.ForeignKey('accounts.Enterprise', on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    is_available = models.BooleanField(default=True)
    localization = models.CharField(max_length=100, blank=True, null=True)
    contact_email = models.EmailField(max_length=180, null=True)
    url_redirection = models.URLField(max_length=740, blank=True)
    language = models.CharField(max_length=2, choices=LANGUAGES_CHOICES, default=LANGUAGES_FRENCH)
    job_offer = models.CharField(max_length=3, choices=OFFER_CHOICES, default=OFFER_CDI)
    job_fields = models.CharField(max_length=2, choices=JOB_FIELDS_CHOICES, default=FIELD_UI)

    class Meta:
        ordering = ('published_date',)
        verbose_name = 'Annonce'
        verbose_name_plural = 'Annonces'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Annonce, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('job-details', kwargs={'slug', self.slug})


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.published_date <= now

    def is_upperclass(self):
        return self.model in (self.OFFER_CDI, self.OFFER_CDD)

    def __str__(self):
        return 'Annonce {}'.format(self.title)
