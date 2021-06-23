from django import forms
from . import models

# using django-search-views API
# class VersionSearchForm(forms.Form):
#     search_personnel = forms.CharField(required=False, label='Search Keyword', widget=forms.TextInput(attrs={'placeholder': 'search here!'}))


# class SessionModelForm(ModelForm):
#     date = DateField(widget=DateInput
#         (attrs={'placeholder':'yyyy-mm-dd'})
#     )
#     class Meta:
#         model = models.Session
#         fields = ['title', 'date', 'location', 'personnel', 'album_releases']
#
# class SongFormModelForm(ModelForm):
#     class Meta:
#         model = models.SongForm
#         fields = ['song_form']
#
# class SongModelForm(ModelForm):
#     class Meta:
#         model = models.Song
#         fields = ['title', 'song_form', 'key']
#
# class VersionModelForm(ModelForm):
#     class Meta:
#         model = models.Version
#         fields = ['song', 'session', 'version_title', 'notes', 'transcription_pdf', 'sibelius_file', 'youtube_link']


# class TrackForm(ModelForm):
#     class Meta:
#         model = models.Track
#         fields = ['song_name','title', 'recording_date', 'personnel', 'notes']
#
#         # widgets = {
#         #     'recording_date': DateInput
#         # }
#     #     widgets = {
#     #         'personnel': Textarea(attrs={'class':'editable'}),
#     #         'notes': Textarea(attrs={'class':'editable'})
#     #     }
#     # def __init__(self, *args, **kwargs):
#     #     super().__init__(*args,**kwargs)
#     #     self.fields['song_name'].label = 'Song Name'
#     #     self.fields['title'].label = "Specific Track Name"
