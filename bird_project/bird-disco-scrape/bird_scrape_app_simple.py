fin = open('bird_disco.html')
# fout = open('chunk_clean.txt', 'w')
# tracks = [(track_number, track_title, release_info)]


def clean(string):
    return string.replace(" &nbsp", "").replace("<i>", "").replace("</i>", "").replace("<p>", "").replace("</p>", "").replace("<br>", "")


def print_stuff():
    """For debugging"""
    print("SESSION:")
    print(session)
    print("PERSONNEL:")
    print(personnel)
    print("LOCATION:")
    print(location)
    print("DATE:")
    print(date)
    print("TRACKS")
    for track in tracks:
        print(track)
    print("ALBUM RELEASE:")
    print(album_release)

entry = {
    "SESSION": {"PERSONNEL" : personnel,
                "LOCATION" : location,
                "DATE" : date,
                "ALBUM_RELEASE" : album_release,
                "TRACKS": [],
    }
}

entries = []

# d = {"SESSION": session,
#     "PERSONNEL": personnel,
#     "LOCATIION": location,
#     "DATE": date,
#     "ALBUM_RELEASE": album_release,
#     "TRACKS": [tracks]}

session = ""
personnel = ""
location_and_date = ""
location = ""
date = ""
album_release = ""
tracks = []


for line in fin:
    if "<h3>" in line:
        # start of each entry + pulls session
        album_release = clean(album_release)
        personnel = clean(personnel).replace("\n","").replace('<span class="same">', "").replace('</span>', "")
        print_stuff()
        session = ""
        personnel = ""
        location_and_date = ""
        location = ""
        date = ""
        album_release = ""
        tracks = []

        first_occurence = line.find(">")
        second_occurence = line.find(">", first_occurence+1)
        final_marker = line.find("</a>")
        session = line[second_occurence+1:final_marker]
        continue

    if '<!-- id="discography-data" -->' in line:
        # signifies end of discography
        album_release = clean(album_release)
        personnel = clean(personnel).replace("\n","")
        print_stuff()
        break

    if "<p>" in line and not "*" in line:
        # these two conditional statements pull the personnel
        personnel += line[3:]
        continue
    if line[0] != "<" and line[0] != "*" and line[0] != "=":
        personnel += " " + line
        continue

    if 'class="date"' in line:
        # pulls the location and date
        first_index = line.find(">") + 1
        end_index = line.find("</p>")
        location_and_date = line[first_index:end_index].replace("&amp;", "&")
        if "unknown date" in line:
            date = "unknown date"
            location = location_and_date.split(", unknown date")[0]
            continue
        date = location_and_date.split(", ")[-2:]
        date = ', '.join(date)
        location = location_and_date.split(", ")[:-2]
        location = ', '.join(location)
        continue

    if line[0:7] == "<tbody>":
        # track number
        first_index = 27
        last_index = line.find("<", first_index)
        track_number = line[first_index:last_index]

        # track title
        first_index = last_index + 21
        last_index = line.find("<", first_index)
        track_title = line[first_index:last_index]

        # track release info
        first_index = last_index + 9
        track_release_info = line[first_index:].replace("\n", "")

        tracks.append((track_number, track_title, track_release_info))

    if line[0:5] == "</td>" and "</tbody>" not in line:
        # track number
        first_index = 18
        last_index = line.find("<", first_index)
        track_number = line[first_index:last_index]

        # track title
        first_index = last_index + 9
        last_index = line.find("<", first_index)
        track_title = line[first_index:last_index]

        # track release info
        first_index = last_index + 9
        track_release_info = line[first_index:].replace("\n", "")

        tracks.append((track_number, track_title, track_release_info))


    if "<p>*" in line:
        # these two conditional statements pull the album release details
        album_release += line[5:]
        continue
    if line[0] == "*" or line[0] == "=":
        album_release += line[2:]
        continue

# fout.close()

# check out:
    # "Massey Hall", Toronto, ON, Canada, May 15, 1953
       # it's got two different listings

# class Entry:
#     def __init__(self, session, personnel, location_and_date, tracks=None, album_release):
#         self.session = session
#         self.personnel = personnel
#         self.location_and_date = location_and_date
#         self.tracks = [] if tracks == None else tracks
#         self.album_release = album_release
#
#     def __str__(self):
#         return f"Session: {self.session} Location: {self.location_and_date}"

# for line in fin:
#     count = 0
#     string = ""
#     if line[:4] == "<h3>":
#         for i in range(len(line)):
#             if line[i] == ">":
#                 count += 1
#             if count == 2:
#                 if line[i] == "<":
#                     print(string)
#                     break
#                 string += line[i]
