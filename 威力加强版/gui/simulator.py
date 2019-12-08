from tkinter import messagebox
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Scrollbar, Checkbutton, Label, Button
import os


class Algorithm_Simulator(Tk):
    icon_res = []
    file_name = None

    def __init__(self):
        super().__init__()
        self._set_window_()
        self._create_menu_bar_()
        self._create_shortcut_bar_()
        self._create_body_()

    # set the window configuration
    def _set_window_(self):
        self.title("基于混合群智能算法的物流分配系统")
        scn_width, scn_height = self.maxsize()
        wm_val = '750x450+%d+%d' % ((scn_width - 750) / 2, (scn_height - 450) / 2)
        self.geometry(wm_val)  # window size
        self.iconbitmap("img/simulator.ico")  # icon
        self.protocol('WM_DELETE_WINDOW', self.exit_simulator)  # exit

    # create the menu bar
    def _create_menu_bar_(self):
        menu_bar = Menu(self)

        # choose excel file bar
        operate_menu = Menu(menu_bar, tearoff=0)
        operate_menu.add_command(label='打开文件', accelerator='Ctrl+O', command=self.open_file)
        operate_menu.add_command(label='运行算法', accelerator='Ctrl+R', command=self.run)
        operate_menu.add_command(label='导出结果', accelerator='Ctrl+S', command=self.save_file)
        operate_menu.add_separator()
        operate_menu.add_command(label='Exit', accelerator='Alt+F4', command=self.exit_simulator)

        # relate the label with the menu
        menu_bar.add_cascade(label='运行选项', menu=operate_menu)

        # about_menu
        about_menu = Menu(menu_bar, tearoff=0)
        about_menu.add_command(label='帮助', command=lambda: self.show_messagebox('帮助'))
        about_menu.add_command(label='关于', command=lambda: self.show_messagebox('关于'))
        menu_bar.add_cascade(label='关于', menu=about_menu)

        self["menu"] = menu_bar  # show

    def _create_shortcut_bar_(self):
        shortcut_bar = Frame(self, height=25, bg='#20b2aa')
        shortcut_bar.pack(fill='x')

        # open file shortcut
        tool_icon = PhotoImage(file='img/open_file.gif')
        tool_btn = Button(shortcut_bar, image=tool_icon, command=self.shortcut_action('open_file'))
        tool_btn.pack(side='left')
        self.icon_res.append(tool_icon)

        # run the algorithm
        tool_icon = PhotoImage(file='img/find_text.gif')
        tool_btn = Button(shortcut_bar, image=tool_icon, command=self.shortcut_action('run'))
        tool_btn.pack(side='left')
        self.icon_res.append(tool_icon)

        # save the result
        tool_icon = PhotoImage(file='img/save.gif')
        tool_btn = Button(shortcut_bar, image=tool_icon, command= self.shortcut_action('save'))
        tool_btn.pack(side='left')
        self.icon_res.append(tool_icon)

        # about info
        tool_icon = PhotoImage(file='img/about.gif')
        tool_btn = Button(shortcut_bar, image=tool_icon, command=self.shortcut_action('about'))
        tool_btn.pack(side='left')
        self.icon_res.append(tool_icon)

        # exit
        tool_icon = PhotoImage(file='img/exit.png')
        tool_btn = Button(shortcut_bar, image=tool_icon, command=self.shortcut_action('exit'))
        tool_btn.pack(side='left')
        self.icon_res.append(tool_icon)

    # the main frame
    def _create_body_(self):
        # alpha frame
        alpha_frame = Frame(self, height=50)
        alpha_frame.pack()

        # input the parameter alpha
        alpha_label = Label(alpha_frame, text='优化系数')
        alpha_label.pack(side=LEFT, anchor=W)
        alpha_range = StringVar()
        alpha_range.set(0)
        alpha_entry = Spinbox(alpha_frame, textvariable=alpha_range, from_=1, to=10)
        alpha_entry.pack(side=LEFT, anchor=W)

        # empty
        empty_frame = Frame(self, height=50)
        empty_frame.pack()

        # input the parameter beta
        beta_frame = Frame(self, height=50)
        beta_frame.pack()
        beta_label = Label(beta_frame, text='已知量影响')
        beta_label.pack(side=LEFT, anchor=W)
        beta_range = StringVar()
        beta_range.set(0)
        beta_entry = Spinbox(beta_frame, textvariable=beta_range, from_=1, to=10)
        beta_entry.pack(side=LEFT, anchor=W)

        empty_frame.pack()

        # rho frame
        rho_frame = Frame(self, height=50)
        rho_frame.pack()
        rho_label = Label(rho_frame, text='挥发浓度(默认为0.2)')
        rho_label.pack(side=LEFT, anchor=W)
        rho_entry = Entry()
        rho_entry.pack(side=LEFT, anchor=W)



        # run button
        run_button = Button(alpha_frame, text='运行', command=self.run)


    def open_file(self):
        pass

    def run(self):
        pass

    def save_file(self):
        pass

    def show_messagebox(self, type):
        pass

    def shortcut_action(self, type):
        pass

    def exit_simulator(self):
        if messagebox.askokcancel("退出？", "确定退出吗？"):
            self.destroy()


if __name__ == "__main__":
    app = Algorithm_Simulator()
    app.mainloop()
