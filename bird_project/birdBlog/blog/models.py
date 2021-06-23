from django.db import models
from django.urls import reverse
from datetime import datetime

class Key(models.Model):
    key = models.CharField(max_length=15)
    # keys = [
    #     'Ab Major', 'A Major', 'Bb Major', 'B Major', 'C Major', 'Db Major', 'D Major', 'Eb Major', 'E Major', 'F Major', 'Gb Major', 'G Major',
    #     'A Minor', 'Bb Minor', 'B Minor', 'C Minor', 'C# Minor', 'D Minor', 'Eb Minor', 'E Minor', 'F Minor', 'F# Minor', 'G Minor', 'G# Minor'
    # ]

    def __str__(self):
        return self.key
#
class Session(models.Model):
    # %Y-%M-%D
    title = models.CharField(max_length=255)
    date = models.CharField(max_length=255, blank=True)
    # date = models.DateField(blank=True)
    location = models.TextField(blank=True)
    personnel = models.TextField(blank=True)
    # album_release = models.ForeignKey(Album, on_delete=models.CASCADE)
    album_releases = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title} {self.date}"

    def get_absolute_url(self):
        return reverse('blog:list_session')

class SongForm(models.Model):
    song_form = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.song_form

    def get_absolute_url(self):
        return reverse('blog:list_songform')

class Song(models.Model):
    title = models.CharField(max_length=255, unique=True)
    song_form = models.ForeignKey(SongForm, on_delete=models.PROTECT)
    key = models.ForeignKey(Key, on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:list_song')
#
# class Album(models.Model):
#     title = models.TextField()
#     release_date = models.DateField()

class Version(models.Model): # New version
    song = models.ForeignKey(Song, on_delete=models.PROTECT, blank=True, null=True)
    session = models.ForeignKey(Session, on_delete=models.PROTECT)
    session_song_number = models.CharField(max_length=255, blank=True, null=True)
    releases = models.CharField(max_length=2000, default="")
    version_title = models.CharField(max_length=255)
    notes = models.TextField(blank=True)
    transcription_pdf = models.FileField(upload_to='transcriptions_pdf', blank=True)
    sibelius_file = models.FileField(upload_to='sibelius_files', blank=True)
    sound_file = models.FileField(upload_to='sound_files', blank=True)
    youtube_link = models.URLField(blank=True)
    # midi_file = models.URLField(blank=True)
    # where to buy
    # could send profits to charlie parker estate

    def __str__(self):
        return f"{self.version_title} | Date: {self.session.date}"

    def get_absolute_url(self):
        return reverse('blog:list_version')


# class Version(models.Model): # old version
#     song = models.ForeignKey(Song, on_delete=models.PROTECT)
#     session = models.ForeignKey(Session, on_delete=models.PROTECT)
#     version_title = models.CharField(max_length=255)
#     notes = models.TextField(blank=True)
#     transcription_pdf = models.FileField(upload_to='transcriptions_pdf', blank=True)
#     sibelius_file = models.FileField(upload_to='sibelius_files', blank=True)
#     youtube_link = models.URLField(blank=True)
#     # midi_file = models.URLField(blank=True)
#     # where to buy
#     # could send profits to charlie parker estate
#
#     def __str__(self):
#         return f"Version: {self.version_title} Date: {self.session}"
#
#     def get_absolute_url(self):
#         return reverse('blog:list_version')

# -----------------------------------------------------------------------
# class Track(models.Model):
#     title = models.ForeignKey(required=True, on_delete=models.CASCADE)
#     song_form = models.ForeignKey(on_delete=models.CASCADE)
#     key_signature = models.ForeignKey(on_delete=models.CASCADE)
#     location = models.CharField(max_length=200)
#     date = models.DateField(required=True) # python datetime.date
#     # duration = models.DurationField()
#     personnel = models.TextArea()
#     tempo_choices = [
#         ("b", "Ballad"),
#         ("m", "Medium"),
#         ("mu", "Medium Up"),
#         ("u", "Up"),
#         ("f", "Fast"),
#     ]
#     tempo = models.CharField(max_length=2, choices=tempo_choices, default="Medium")
#     transcription_upload = models.FileField(upload_to='transcriptions/') # file will be uploaded to MEDIA_ROOT/uploads
#
#     def get_absolute_url(self):
#         # once done creating post (after hitting publication)
#         # go to post_detail, using primary key of post just created
#         return reverse("post_detail",kwargs={'pk':self.pk})
#
#     def __str__(self):
#         return self.title, self.date
#
#
# from django.db import models
# from django.utils import timezone
# from django.urls import reverse
#
# # Create your models here.
# class Post(models.Model):
#     author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
#     title = models.CharField(max_length=200)
#     text = models.TextField()
#     create_date = models.DateTimeField(default=timezone.now)
#     published_date = models.DateTimeField(blank=True,null=True)
#
#     def publish(self):
#         self.published_date = timezone.now()
#         self.save()
#
#     def approve_comments(self):
#         return self.comments.filter(approved_comment=True)
#
#     def get_absolute_url(self):
#         # once done creating post (after hitting publication)
#         # go to post_detail, using primary key of post just created
#         return reverse("post_detail",kwargs={'pk':self.pk})
#
#     def __str__(self):
#         return self.title
