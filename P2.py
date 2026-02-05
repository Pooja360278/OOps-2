
class Camera:
    def __init__(self, camera_quality):
        self.camera_quality = camera_quality

    def display_camera_details(self):
        print("Camera Quality:", self.camera_quality)


class MusicPlayer:
    def __init__(self, sound_quality):
        self.sound_quality = sound_quality

    def display_music_details(self):
        print("Sound Quality:", self.sound_quality)


class Smartphone(Camera, MusicPlayer):
    def __init__(self, camera_quality, sound_quality, brand):
        Camera.__init__(self, camera_quality)
        MusicPlayer.__init__(self, sound_quality)
        self.brand = brand

    def display_phone_details(self):
        print("Brand:", self.brand)
        self.display_camera_details()
        self.display_music_details()


phone = Smartphone("64 MP", "Dolby Surround", "Samsung")
phone.display_phone_details()
