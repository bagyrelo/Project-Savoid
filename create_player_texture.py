from pathlib import Path
import struct
import zlib


def write_png(path: Path, width: int, height: int, pixels: list[int]) -> None:
    def chunk(chunk_type: bytes, data: bytes) -> bytes:
        return (
            struct.pack(">I", len(data))
            + chunk_type
            + data
            + struct.pack(">I", zlib.crc32(chunk_type + data) & 0xFFFFFFFF)
        )

    raw = bytearray()
    for y in range(height):
        raw.append(0)
        for x in range(width):
            i = (y * width + x) * 4
            raw.extend(pixels[i : i + 4])

    png = bytearray(b"\x89PNG\r\n\x1a\n")
    png.extend(chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 6, 0, 0, 0)))
    png.extend(chunk(b"IDAT", zlib.compress(bytes(raw), 9)))
    png.extend(chunk(b"IEND", b""))
    path.write_bytes(png)


width, height = 32, 32
pixels = []
for y in range(height):
    for x in range(width):
        if 6 <= x <= 25 and 6 <= y <= 25:
            pixels.extend([255, 0, 0, 255])
        else:
            pixels.extend([0, 0, 0, 0])

# eyes
for x, y in [(10, 10), (20, 10)]:
    idx = (y * width + x) * 4
    pixels[idx : idx + 4] = [255, 255, 255, 255]

# mouth
for x in range(12, 19):
    idx = (18 * width + x) * 4
    pixels[idx : idx + 4] = [0, 0, 0, 255]

write_png(Path("assets/player.png"), width, height, pixels)
print("player texture regenerated")
