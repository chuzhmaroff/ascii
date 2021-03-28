from tkinter import *
from tkinter import scrolledtext
from tkinter import filedialog
import generator_ascii as generator

import os


def print_status_choose_mode_to_console(status):
    global console_text
    info_text.insert(INSERT, "\nSelected mode: {}".format(status))


def print_status_choose_color_to_console(status):
    global console_text
    info_text.insert(INSERT, "\nSelected color: {}".format(status))


def get_directory():
    global path_to_image
    global console_text
    path_to_image = str(filedialog.askopenfilename())
    if path_to_image != "":
        info_text.insert(INSERT,
                         "\nNew path to image: {}".format(path_to_image))
    if path_to_image == "":
        info_text.insert(INSERT, "\nYou didn't select image")
    return path_to_image


def select_branch_code(status_choose_mode, status_choose_color_mode,
                       set_scale_factor, path_to_image):
    if status_choose_mode == options_1[0]:
        generator.simple_ascii_art(path_to_image)
    if status_choose_mode == options_1[1]:
        if status_choose_color_mode == options_0[0]:
            fill = 0
            generator.color_ascii_art(set_scale_factor, fill, path_to_image)
        if status_choose_color_mode == options_0[1]:
            fill = 1
            generator.color_ascii_art(set_scale_factor, fill, path_to_image)


def start_create_ascii_art():
    if path_to_image == "":
        info_text.insert(INSERT, "\nYou didn't select image")
        return

    status_choose_mode = choose_mode_ascii.get()
    status_choose_color_mode = choose_color_on_ascii.get()
    set_scale_factor = object_spin_scale_factor.get()

    if status_choose_mode == options_1[0]:
        info_text.insert(INSERT,
                         "\nСоздание Ascii Art с настройками:\nРежим: {}\n".
                         format(
                             status_choose_mode))
    if status_choose_mode == options_1[1]:
        info_text.insert(INSERT,
                         "\nСоздание Ascii Art с настройками:\nРежим: {}"
                         "\nColor: {}\nScale Factor: {}\n".format(
                             status_choose_mode, status_choose_color_mode,
                             set_scale_factor))

    select_branch_code(status_choose_mode, status_choose_color_mode,
                       set_scale_factor, path_to_image)
    op = os.path.dirname(os.path.abspath(__file__))
    if status_choose_mode == options_1[0]:
        info_text.insert(INSERT,
                         "\nAscii Art готов! Находится тут - {}".format(
                            op + " \Ascii_art.txt"))
    if status_choose_mode == options_1[1]:
        info_text.insert(INSERT,
                         "\nAscii Art готов! Находится тут - {}".format(
                            op + " \Ascii_art.png"))


def create_new_art():
    f_window_select_mode = Frame()
    f_window_select_setting_for_pro_mode_1 = Frame()
    f_window_select_setting_for_pro_mode_2 = Frame()

    get_path_to_image = Button(window,text="Укажите путь до файла для преобразования",command=get_directory)
    get_path_to_image.pack(side=TOP, pady=20)

    table_info_change_filter = Label(f_window_select_mode,text="Выберите фильтр: ")
    table_info_change_filter.pack(side=LEFT)
    table_change_mod = OptionMenu(f_window_select_mode, choose_mode_ascii,*options_1,command=print_status_choose_mode_to_console)
    table_change_mod.pack(side=RIGHT, padx=50)
    f_window_select_mode.pack()

    table_info_who_setting = Label(window,text='Настройки только для режима Продвинутый Ascii Art:')
    table_info_who_setting.pack(side=TOP, pady=30)

    info_for_change_color = Label(f_window_select_setting_for_pro_mode_1,text='Цвет Ascii Art: ')
    info_for_change_color.pack(side=LEFT)
    table_change_color_mode = OptionMenu(f_window_select_setting_for_pro_mode_1, choose_color_on_ascii,*options_0, command=print_status_choose_color_to_console)
    table_change_color_mode.pack(side=RIGHT)
    f_window_select_setting_for_pro_mode_1.pack()

    info_for_change_scale_factor = Label(f_window_select_setting_for_pro_mode_2,text='Масштабный коэффициент: ')
    info_for_change_scale_factor.pack(side=LEFT)

    global object_spin_scale_factor
    object_spin_scale_factor = Spinbox(f_window_select_setting_for_pro_mode_2,
                                       from_=0, to=0.50, width=5,
                                       increment=0.01,
                                       textvariable=default_scale_factor,
                                       state='readonly')
    object_spin_scale_factor.pack(side=RIGHT)
    f_window_select_setting_for_pro_mode_2.pack()

    start_ascii = Button(window, text="Старт", command=start_create_ascii_art)
    start_ascii.pack(side=BOTTOM, pady=20)


font_for_window = ("Times New Roman", 9)

options_1 = [
    "Простой Ascii Art из множествa символов",
    "Продвинутый Ascii Art с интрументами"
]

options_0 = [
    "Черно-белый",
    "Цветной"
]
path_to_image = ""
console_text = 'Ascii Art 2020 [Version: 1.0]'
var_s = ""

window = Tk()
window.title("Ascii Art")
window.geometry('900x600+100+10')
window.resizable(0, 0)
info_text = scrolledtext.ScrolledText(window, width=100, height=20,
                                      font=font_for_window)
info_text.pack()
info_text.insert(INSERT, console_text)

object_spin_scale_factor = ""
default_scale_factor = StringVar()
default_scale_factor.set("0.09")

choose_color_on_ascii = StringVar(window)
choose_color_on_ascii.set(options_0[0])
choose_mode_ascii = StringVar(window)
choose_mode_ascii.set(options_1[0])
create_new_art()

window.mainloop()
#официальная атрибутика и свободный spin