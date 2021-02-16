from tkinter import *
from tkinter import ttk


# Формула чтобы перевести градусы Цельсия в Фарингейт
def c_to_f(*args):
    try:
        value = float(c_degrees.get())
        f_degrees.set(int((value - 32) * 5.0/9.0))
    except ValueError:
        pass


root = Tk()
root.title('Temperature Convertor')

content = ttk.Frame(root, padding='5 5 10 10')
content.grid(column=0, row=0, sticky=(N, W, E, S))

# Создаем метку Celsius
c_degrees = StringVar()
celsius_label = ttk.Label(content, text='Celsius:')
celsius_label.grid(row=0, column=0, padx=(5), sticky=(EW))

# Создаем поле ввода температуры
temp_entry = ttk.Entry(content, textvariable=c_degrees)
temp_entry.grid(row=0, column=1, sticky=(EW), pady=5, padx=5, columnspan=2)
temp_entry.focus()

# Создаем метку Fahrenheit
f_degrees = StringVar()
fahrenheit_label = ttk.Label(content, text='In  Fahrenheit')
fahrenheit_label.grid(row=1, column=0, pady=5, padx=5, sticky=(EW))

# Создаем кнопку конвертации
convert_button = ttk.Button(content, text='Convert', command=c_to_f)
convert_button.grid(row=2, pady=5, padx=5, columnspan=3)

# Создаем метку с результатом
ttk.Label(content, text='equals').grid(column=1, row=1, sticky=(W), pady=5)
ttk.Label(content, textvariable=f_degrees).grid(column=1, row=1, sticky=(E), pady=5, padx=0)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=3)
content.columnconfigure(1, weight=3)
content.columnconfigure(2, weight=3)
content.columnconfigure(3, weight=1)
content.columnconfigure(4, weight=1)
content.rowconfigure(1, weight=1)

root.mainloop()
