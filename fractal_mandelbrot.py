from PIL import Image
from tqdm import tqdm
import math
W, H = 1024, 768  # размеры картинки
ITER = 1000  # максимальное число итераций, чтобы убедиться расходися или нет формула в данной точке
LIMIT = 2.0  # предельное значение, выше которого уже расходится
img = Image.new('RGB', (W, H))
# создадим палитру от числа итераций
palette = [
    (
        int(255 * math.sin(i / 50.0 + 1.0) ** 2),
        int(255 * math.sin(i / 50.0 + 0.5) ** 2),
        int(255 * math.sin(i / 50.0 + 1.7) ** 2)
    ) for i in range(ITER - 1)
]
palette.append((0, 0, 0))  # последняя итерация - значит мы внутри - черный
for px in tqdm(range(W)):
    for py in range(H):
        # преобразование координат
        x = px / W * 3 - 2  # x = -2..1
        y = py / H * 2 - 1  # y = -1..1
        c = x + 1j * y  # смещение из координат
        z = 0j  # начальная точка
        for n in range(ITER):
            z = z ** 2 + c
            if abs(z) > LIMIT:  # разошлось
                break
        img.putpixel((px, py), palette[n])
img.save('mand1.png')  # сохраним
img.show()  # покажем

"""
Для оптимизации производительности, вместо abs(z)
                if (z * z.conjugate()).real > 4.0:  # вместо abs(z) > 2.0!
                    break
"""