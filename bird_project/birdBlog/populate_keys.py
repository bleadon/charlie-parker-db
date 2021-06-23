import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'birdBlog.settings')

import django
django.setup()

from blog.models import Key

keys = [
    'Ab Major', 'A Major', 'Bb Major', 'B Major', 'C Major', 'Db Major', 'D Major', 'Eb Major', 'E Major', 'F Major', 'Gb Major', 'G Major',
    'A Minor', 'Bb Minor', 'B Minor', 'C Minor', 'C# Minor', 'D Minor', 'Eb Minor', 'E Minor', 'F Minor', 'F# Minor', 'G Minor', 'G# Minor'
]

for k in keys:
    new_key = Key.objects.get_or_create(key=k)[0]
    print(new_key)
