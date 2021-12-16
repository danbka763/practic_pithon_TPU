import numpy as np
import matplotlib.pyplot as plt
#  cbook - модуль "всяких полезностей":
import matplotlib.cbook as cbook
import matplotlib.font_manager as fm

# -----------------------------------------------------------------

# Создаем графики для дальнейшего заполнения
fig, axes = plt.subplots(
    nrows=2,
    ncols=3
)
ax1, ax2, ax3, ax4, ax5, ax6 = axes.flatten()

# ----------------------------1.1----------------------------------

#  Конструкция "with ... as" гарантирует, что файл
#  будет закрыт после прочтения:
with cbook.get_sample_data('ada.png') as image_file:
    image = plt.imread(image_file)

ax1.imshow(image)
ax1.set_title("Ada")

ax1.xaxis.set_major_formatter(plt.NullFormatter())
ax1.yaxis.set_major_formatter(plt.NullFormatter())

fig.set_figwidth(10)    #  ширина и
fig.set_figheight(10)    #  высота "Figure"

# ----------------------------1.2----------------------------------

# Создаем переменную с текстом из файла file_date.txt
file_date = open('file_date.txt', 'r')
text = file_date.read()
file_date.close()

# Переписываем значения из строки в ячейки массива mass[]
mass = [float(x) for x in text.split()]


# Создаем функцию для заполнения массивов elem_x и elem_y
def filling2(value, numb_sist, j, t=0):
    while t < j:
        value = np.append(value, numb_sist(mass[t]))
        t = t + 1
    return value


elem_x = filling2(np.array([]), int, 27)
elem_y = filling2(np.array([]), float, 108, 81)

# Создаем график
ax2.fill_between(elem_x, elem_y, color='yellow', where=elem_y > 0,
                 interpolate=True)
ax2.fill_between(elem_x, elem_y, color='green', where=elem_y < 0,
                 interpolate=True)
ax2.set_title("Стандартный график с заливкой", fontname='Tahoma',
              style='italic', size=14, weight='normal', c='#4f4f4f')
ax2.set_ylabel("Температура")
ax2.set_xlabel("Время")
ax2.set_facecolor('b')
ax2.patch.set_alpha(0.45)
ax2.grid(True)

# Значения для осей ox & oy
oy = [-15, -12.5, -10, -7.5, -5, -2.5, 0, 2.5, 5]
ox = [-5, 0, 5, 10, 15, 20, 25, 30, 35]

ax2.set_xticklabels(ox, fontname='Comic Sans MS', rotation='60', fontsize=11)
ax2.set_yticklabels(oy, fontname='Comic Sans MS', rotation='60', fontsize=11)

# ----------------------------1.3----------------------------------

# Создаем переменную с текстом из файла fig8.txt
fig8 = open('fig8.txt', 'r')
text2 = fig8.read()
fig8.close()

# Переписываем значения из строки в ячейки массива mass[]
mass = [int(x) for x in text2.split()]


# Функция поиска первого и последнего числа из txt
def first_and_last_digit(k, r=2, t=0, j=0):
    while j != k:
        if mass[t] > 71:
            t = t + r
            j = j + 1
        else:
            t = t + 1
    return t


n_min = first_and_last_digit(3) - 2
n_max = first_and_last_digit(4, 0, (n_min + 2)) - 1

# Создаем массив с диапазоном значений для оси абсцисс
g = mass[n_min]
diapazon = []
while g <= mass[n_min + 1]:
    diapazon.append(g)
    g = g + 1

# Создаем массив со значениями для оси ординат
i = n_min + 2
elem_y3 = []
while i <= n_max:
    elem_y3.append(mass[i])
    i = i + 1

# Заполняем столбчатую диаграмму
ax3.bar(diapazon, elem_y3, color='#028d96')
ax3.set_title("Диаграмма с аннотацией")
ax3.set_facecolor('y')
ax3.patch.set_alpha(0.2)
ax3.grid(True)

ax3.annotate('Очень важно!!', xy=(585, 31), xytext=(562, 30),
             arrowprops={'facecolor': 'y'})

# ----------------------------1.4----------------------------------

# Высчитываем значения для графиков
x = np.arange(-2*np.pi, 2*np.pi, 0.1)
y1 = np.sin(3 * x - np.pi / 6) - np.sin(2 * x + np.pi / 6)
y2 = -0.15*y1

# Заполняем график
ax4.set_xlabel('Аргумент')
ax4.set_ylabel('Функция')
ax4.grid(True)
ax4.set_title('Несколько графиков')

font = fm.FontProperties(family= 'Times New Roman',
                         weight='bold',
                         style='normal',
                         size=16)

ax4.plot(x, y1, label='Первое выражение')
ax4.plot(x, y2, label='Второе выражение')
ax4.legend(loc="best", prop=font)

# Значения для осей ox & oy
oy = [-2.5, -2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2.0]
ox = [-7.5, -5, -2.5, 0, 2.5, 5, 7.5]

ax4.set_xticklabels(ox, fontname='Comic Sans MS', rotation='45', fontsize=11)
ax4.set_yticklabels(oy, fontname='Comic Sans MS', rotation='45', fontsize=11)

# ----------------------------1.5----------------------------------

# Создаем массивы со случайными координатами для точек
x = np.random.rand(300)
y1 = np.random.pareto(3.2, size=300)
y2 = (1 - (-1)) * np.random.random_sample(size=300) - 1
y3 = np.random.gamma(2, size=300)

# Заполняем график случайными точками
ax5.scatter(x, y1, s=2, c=[[0.227, 0.11, 0.195]])
ax5.scatter(x+1, y2, s=1, c='b')
ax5.scatter(x+2, y3, s=1, c='#daeb26')
ax5.set_facecolor('black')
ax5.set_title('Диаграмы рассеяния')

# ----------------------------1.6----------------------------------

h = np.linspace(0, 2 * np.pi, 100)

ax6.set_title('Лиссанжу')
ax6.yaxis.grid(color='#0330fc')
ax6.xaxis.grid(color='#0330fc')
ax6.plot(10 * np.sin(4 * h + np.pi / 3), 4 * np.sin(6 * h))
ax6.fill_between(10 * np.sin(4 * h + np.pi / 3), 4 * np.sin(6 * h))
ax6.set_aspect(1)
ax6.grid(True)

# -----------------------------------------------------------------

plt.show()
# fig.savefig('result.png', dpi=240)
