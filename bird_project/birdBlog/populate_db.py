import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'birdBlog.settings')

import django
django.setup()

import shelve

db = shelve.open('/home/jonathan/portfolio/bird_project/bird-disco-scrape/clean-bird-data')

from blog.models import Session, Version

# db = [{'SESSION': 'Jay McShann And His Orchestra', 'PERSONNEL': 'Buddy Anderson, Bob Merrill, Orville Minor, trumpet; Lawrence Anderson, Joe Taswell Baird, trombone; John Jackson, Charlie Parker, alto sax; Fred Culliver, Bob Mabane, tenor sax; James Coe, baritone sax;  Jay McShann, piano; Leonard "Lucky" Enois, guitar; Gene Ramey, bass; Doc West, drums; Al Hibbler, vocals #2.', 'LOCATION': '"Savoy Ballroom", NYC', 'DATE': 'February 13, 1942', 'ALBUM_RELEASE': ['Stash ST-CD-542; Charlie Parker With Jay McShann And His Orchestra - Early Bird'], 'TRACKS': [('1.', 'St. Louis Mood', 'Stash ST-CD-542'), ('2.', "I've Got It Bad", 'Stash ST-CD-542'), ('3.', "I'm Forever Blowing Bubbles", 'Stash ST-CD-542'), ('4.', 'Hootie Blues', 'Stash ST-CD-542'), ('5.', 'Swingmatism', 'Stash ST-CD-542'), ('6.', "Love Don't Get You Nothing But The Blues", 'Stash ST-CD-542')]}, {'SESSION': 'Jay McShann And His Orchestra', 'PERSONNEL': 'Buddy Anderson, Bob Merrill, Orville Minor, trumpet; Lawrence Anderson, Joe Taswell Baird, trombone; John Jackson, Charlie Parker, alto sax; Fred Culliver, Bob Mabane, tenor sax; James Coe, baritone sax;  Jay McShann, piano; Leonard "Lucky" Enois, guitar; Gene Ramey, bass; Doc West, drums; Walter Brown, vocals #1,3; Al Hibbler, vocals #2.', 'LOCATION': 'NYC', 'DATE': 'July 2, 1942', 'ALBUM_RELEASE': ['MCA 1338; Jay McShann - The Early Bird Charlie Parker, 1941-1943 - Jazz Heritage Series', 'Decca ED 742; Jay McShann - no info', 'Decca 4387; Jay McShann - Lonely Boy Blues / Sepian Bounce', "Decca 4418; Coral 60034; Jay McShann - Get Me On Your Mind / The Jumpin' Blues"], 'TRACKS': [('1. 70993-A', 'Lonely Boy Blues', 'Decca 4387; MCA 1338'), ('2. 70994-A', 'Get Me On Your Mind', 'Decca 4418, ED 742; MCA 1338'), ('3. 70995-A', "The Jumpin' Blues", 'Decca 4418; MCA 1338'), ('4. 70996-A', 'Sepian Bounce', 'Decca 4387; MCA 1338')]}]


for entry in db["DISCO"]:

    releases = (" || ".join(entry["ALBUM_RELEASE"])).replace("&amp;", "&")

    session = Session.objects.get_or_create(
        title=entry["SESSION"],
        date=entry["DATE"],
        location=entry["LOCATION"],
        personnel=entry["PERSONNEL"],
        album_releases=releases
    )

    for track in entry["TRACKS"]:
        version = Version.objects.get_or_create(
            session=session[0],
            session_song_number=track[0],
            releases=track[2],
            version_title=track[1]
        )

db.close()

# cp_blues = ["cool blues", "now's the time", "buzzy", "au privave"]
#
# for version in Version.objects.all():
#     if "cool blues" in version.version_title[1].lower():
#         print(version.version_title)
#         songform = SongForm.objects.get_or_create(song_form="Blues")
#         song = Song.objects.get_or_create(
#                                         title=version.version_title,
#                                         song_form=songform[0]
#         )

# """Changes the '\n' in Ssession.album_releases"""
# for session in Session.objects.all():
#     session.album_releases = session.album_releases.replace("\n", " * ")
#     session.save()
#     # print(repr(session.album_releases))
