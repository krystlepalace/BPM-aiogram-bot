import eyed3


class TagsEditor:
    def __init__(self, filepath):
        self.file = eyed3.load(filepath)

        if not self.file.tag:
            self.file.initTag()

    async def change_cover(self, image):
        format = image.split('.')[-1]
        with open(image, "rb") as cover_art:
            self.file.tag.images.set(3, cover_art.read(), f"image/{format}")
