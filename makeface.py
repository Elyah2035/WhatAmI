

from thispersondoesnotexist import get_online_person, get_checksum_from_picture, Person
from thispersondoesnotexist import Person
from playsound import playsound
# Initialize with True to automatically get a person from the webpage
person = Person(fetch_online=True)
sound_file = 'iamdone.mp3'

for i in range(5000):
    print("i am at"+str(i))
    # Save to a file
    person.save("faces/person"+str(i)+".jpeg")
    # If no filename is provided, one will be generated using the checksum of the picture
    person.save()
    # Using object
    person = Person(fetch_online=True)
    checksum = person.get_checksum("md5")

    # Using function
    picture = get_online_person()
    checksum2 = get_checksum_from_picture(picture)  # Method is optional, defaults to "md5"


# Play the sound
for x in range(4):

    playsound(sound_file)
