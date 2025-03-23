from pydub import AudioSegment

audio_file = "deshields_voice.mp3"

interview = AudioSegment.from_mp3(audio_file)

two_minutes = 1000 * 60 * 2  # 1000 ms * 60 secs * 2 mins
first_two_minutes = interview[:two_minutes]
first_two_minutes.export("deshields-voice-2mins.mp3", format="mp3")

five_minutes = 1000 * 60 * 5  # 1000 ms * 60 secs * 2 mins
first_five_minutes = interview[:five_minutes]
first_five_minutes.export("deshields-voice-5mins.mp3", format="mp3")

ten_minutes = 1000 * 60 * 10  # 1000 ms * 60 secs * 2 mins
first_ten_minutes = interview[:ten_minutes]
first_ten_minutes.export("deshields-voice-10mins.mp3", format="mp3")

twenty_minutes = 1000 * 60 * 20  # 1000 ms * 60 secs * 2 mins
first_twenty_minutes = interview[:twenty_minutes]
first_twenty_minutes.export("deshields-voice-20mins.mp3", format="mp3")

thirty_minutes = 1000 * 60 * 30  # 1000 ms * 60 secs * 2 mins
first_thirty_minutes = interview[:thirty_minutes]
first_thirty_minutes.export("deshields-voice-30mins.mp3", format="mp3")
print("Done!")
