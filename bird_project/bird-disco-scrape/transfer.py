from . models import Session, Version, Song

for entry in entries:

    session = Session()
    session.title = entry["SESSION"] + " - " + entry["DATE"] # add something to differentiate sessions?
    session.date = entry["DATE"]
    session.location = entry["LOCATION"]
    session.personnel = entry["PERSONNEL"]
    for release in entry["ALBUM_RELEASE"]:
        session.album_releases += release + "\n"

    for track in entry["TRACKS"]:
        version = Version()
        # version.song = ?
        version.version_title = track[1]
        version.session = session # add something to differentiate sessions? --> this includes date
        version.session_song_number = track[0]
        version.releases = track[2]


# class Version(): # add to django models to include extra extract info from jazzdisco
#     def __init__(self, title, song, session, session_song_number, releases):
#         version.title = title
#         version.song = song
#         version.session = session
#         version.session_song_number = session_song_number
#         version.releases = releases
