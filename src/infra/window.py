from __future__ import annotations

import ctypes
from ctypes import wintypes
from dataclasses import dataclass


@dataclass(slots=True)
class WindowRect:
    left: int
    top: int
    right: int
    bottom: int

    @property
    def width(self) -> int:
        return self.right - self.left

    @property
    def height(self) -> int:
        return self.bottom - self.top


def find_window_by_title(title_substring: str) -> int:
    if not title_substring:
        raise ValueError("title_substring vazio.")

    user32 = ctypes.windll.user32
    user32.EnumWindows.argtypes = [
        ctypes.WINFUNCTYPE(ctypes.c_bool, wintypes.HWND, wintypes.LPARAM),
        wintypes.LPARAM,
    ]

    matches: list[int] = []

    @ctypes.WINFUNCTYPE(ctypes.c_bool, wintypes.HWND, wintypes.LPARAM)
    def callback(hwnd: int, _: int) -> bool:
        if not user32.IsWindowVisible(hwnd):
            return True

        length = user32.GetWindowTextLengthW(hwnd)
        if length <= 0:
            return True

        buffer = ctypes.create_unicode_buffer(length + 1)
        user32.GetWindowTextW(hwnd, buffer, length + 1)
        title = buffer.value
        if title_substring.lower() in title.lower():
            matches.append(hwnd)
        return True

    user32.EnumWindows(callback, 0)
    if not matches:
        raise RuntimeError(f"Nenhuma janela encontrada com titulo contendo: {title_substring}")
    return matches[0]


def get_window_rect(hwnd: int) -> WindowRect:
    rect = wintypes.RECT()
    ok = ctypes.windll.user32.GetWindowRect(hwnd, ctypes.byref(rect))
    if not ok:
        raise RuntimeError(f"Falha ao ler coordenadas da janela hwnd={hwnd}")
    return WindowRect(
        left=rect.left,
        top=rect.top,
        right=rect.right,
        bottom=rect.bottom,
    )


def get_cursor_pos() -> tuple[int, int]:
    point = wintypes.POINT()
    ok = ctypes.windll.user32.GetCursorPos(ctypes.byref(point))
    if not ok:
        raise RuntimeError("Falha ao ler posicao do cursor.")
    return point.x, point.y
