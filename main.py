from customtkinter import *

warn_label_user = None
warn_label_pass = None
widget_to_destroy = []

def destoy_all_widgets():
    for widgets in widget_to_destroy:
        widgets.destroy()
    widget_to_destroy.clear()

def key_gen(winmaster, user, password):
    virt_key_u = [0x42, 0x4C, 0x55, 0x53, 0x45]
    virt_key_p = [0x72, 0x69, 0x76, 0x76, 0x79]

    key_u = []
    key_p = []

    for char_u in virt_key_u:
        key_u.append(chr(char_u))
    key_u = ''.join(key_u)

    for char_p in virt_key_p:
        key_p.append(chr(char_p))
    key_p = ''.join(key_p)

    if key_u == user and key_p == password:
        fin_label = CTkLabel(
            winmaster,
            text = 'successfully loged in!',
            font = ('Helvetica', 16)
        )
        fin_label.place(relx = .5, rely = .5, anchor = CENTER)
    else:
        fin_label2 = CTkLabel(
            winmaster,
            text = 'Incorrect account information!',
            font = ('Helvetica', 16)
        )
        fin_label2.place(relx = .5, rely = .5, anchor = CENTER)

    destoy_all_widgets()

def Error_Handling(winmaster, user, password):
    global warn_label_user, warn_label_pass

    # Destroy existing labels if they exist
    if warn_label_user is not None:
        warn_label_user.destroy()
        warn_label_user = None
    if warn_label_pass is not None:
        warn_label_pass.destroy()
        warn_label_pass = None

    userget = user.get()
    passwordget = password.get()

    check1 = False
    check2 = False

    if not userget.strip():
        warn_label_user = CTkLabel(
            winmaster,
            text='Empty username not allowed!'
        )
        warn_label_user.pack()
    else:
        check1 = True

    if not passwordget.strip():
        warn_label_pass = CTkLabel(
            winmaster,
            text='Empty password not allowed!'
        )
        warn_label_pass.pack()
    else:
        check2 = True

    if check1 and check2:
        key_gen(winmaster, userget, passwordget)

def main_window():
    window = CTk()
    window.title('Application')
    window.geometry('400x300')
    window.resizable(False, False)

    def header_widgets(winmaster):
        hero_label = CTkLabel(
            winmaster,
            text = 'Log In',
            font = ('Helvetica', 21)
        )
        hero_label.pack(pady = (20, 5))
        widget_to_destroy.append(hero_label)

    def section_widgets(winmaster):

        # vars:
        user = StringVar()
        password = StringVar()

        # username input:
        user_label = CTkLabel(
            winmaster,
            text = 'Username:',
            font = ('Helvetica', 16)
        )
        user_label.pack()
        widget_to_destroy.append(user_label)

        username_entry = CTkEntry(
            winmaster,
            textvariable = user
        )
        username_entry.pack()
        widget_to_destroy.append(username_entry)

        # password input:
        pass_label = CTkLabel(
            winmaster,
            text = 'Password:',
            font = ('Arial', 16)
        )
        pass_label.pack(pady = (10, 0))
        widget_to_destroy.append(pass_label)

        password_entry = CTkEntry(
            winmaster,
            textvariable = password
        )
        password_entry.pack()
        widget_to_destroy.append(password_entry)

        return user, password

    def footer_widgets(winmaster, user, password):
        
        def destoy_widget():
            warn_label_user.destroy()
            warn_label_pass.destroy()

        fin_button = CTkButton(
            winmaster,
            text = 'Enter',
            command = lambda: Error_Handling(window, user, password)
        )
        fin_button.pack(pady = 20)
        widget_to_destroy.append(fin_button)
        
    header_widgets(window)
    user, password = section_widgets(window)
    footer_widgets(window, user, password)

    return window

if __name__ == "__main__": 
    window = main_window()

    window.mainloop()