from django.db.models import Q
from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from . import forms
from . import models


class HomePageView(generic.TemplateView):
    template_name = "home.html"

class SearchPageView(generic.TemplateView):
    template_name = "blog/search.html"
    keys = [
        "" , 'Ab Major', 'A Major', 'Bb Major', 'B Major', 'C Major', 'Db Major', 'D Major', 'Eb Major', 'E Major', 'F Major', 'Gb Major', 'G Major',
        'A Minor', 'Bb Minor', 'B Minor', 'C Minor', 'C# Minor', 'D Minor', 'Eb Minor', 'E Minor', 'F Minor', 'F# Minor', 'G Minor', 'G# Minor'
    ]
    def get_context_data(self, **kwargs):
        context = super(SearchPageView, self).get_context_data(**kwargs)
        context.update({'keys': self.keys})
        return context

class SearchResultsView(generic.ListView):
    model = models.Version
    template_name = 'blog/search_results.html'

    def get_queryset(self):
        object_list = models.Version.objects.all()

        key_query = self.request.GET.get('key')
        if key_query:
            object_list = object_list.filter(song__key__key__icontains=key_query)
             # object_list = models.Version.objects.raw("SELECT * FROM blog_version")

        form_query = self.request.GET.get('form')
        if form_query:
            object_list = object_list.filter(song__song_form__song_form__icontains=form_query)

        form_query = self.request.GET.get('song')
        if form_query:
            object_list = object_list.filter(version_title__icontains=form_query)

        form_query = self.request.GET.get('person')
        if form_query:
            queries = form_query.split(", ")
            for query in queries:
                object_list = object_list.filter(session__personnel__icontains=query)

        form_query = self.request.GET.get('date')
        if form_query:
            object_list = object_list.filter(session__date__icontains=form_query)

        form_query = self.request.GET.get('location')
        if form_query:
            object_list = object_list.filter(session__location__icontains=form_query)

        form_query = self.request.GET.get('album')
        if form_query:
            object_list = object_list.filter(session__album_releases__icontains=form_query)

        form_query = self.request.GET.get('notes')
        if form_query:
            object_list = object_list.exlude(notes__icontains=form_query)

        form_query = self.request.GET.get('pdf')
        if form_query:
            object_list = object_list.exclude(transcription_pdf="")

        form_query = self.request.GET.get('sound')
        if form_query:
            object_list = object_list.exclude(sound_file="")

        form_query = self.request.GET.get('youtube')
        if form_query:
            object_list = object_list.exclude(youtube_link="")

        # person_query = self.request.GET.get('person')
        # object_list = models.Version.objects.filter(session__personnel__icontains=person_query)
        return object_list

class VersionDetailView(generic.DetailView):
    model = models.Version
    template_name = 'blog/version_detail.html'

    def get_object(self, queryset=None):
        return models.Version.objects.get(pk=self.kwargs.get("pk"))

class VersionListView(generic.ListView):
    model = models.Version
