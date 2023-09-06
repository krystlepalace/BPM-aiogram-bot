import eyed3


class TagsEditor:
    def __init__(self, filepath, song_name):
        self.file = eyed3.load(filepath)

        if not self.file.tag:
            self.file.initTag()
            self.file.tag.title = song_name

    async def change_cover(self, image):
        format = "jpeg" if image.endswith((".jpg", ".jpeg")) else "png"
        with open(image, "rb") as cover_art:
            self.file.tag.images.set(3, cover_art.read(), f"image/{format}")
