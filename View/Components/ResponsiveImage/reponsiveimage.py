from kivymd.uix.fitimage import FitImage
from kivy.properties import ListProperty


class ResponsiveImage(FitImage):
    image_ratio = ListProperty([4, 3])
    """
    Image Aspect ratio.
    """
    
    def __init__(self):
        super().__init__()
        self.bind(size=self.adjust_image_size)

    def adjust_image_size(self, *args) -> None:
        w_ratio, h_ratio = self.image_ratio
        self.height = h_ratio / w_ratio * self.width