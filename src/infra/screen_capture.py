from __future__ import annotations

from dataclasses import dataclass

from PIL import Image

@dataclass(slots=True)
class Frame:
    width: int
    height: int
    source: str = "mock"


class ScreenCapture:
    """Adaptador de captura de tela via PIL."""

    def grab(self) -> Frame:
        return Frame(width=1920, height=1080)

    def grab_image(self, bbox: tuple[int, int, int, int]) -> Image.Image:
        # Import local para manter o modulo leve se imagem nao for usada.
        from PIL import ImageGrab

        return ImageGrab.grab(bbox=bbox)
