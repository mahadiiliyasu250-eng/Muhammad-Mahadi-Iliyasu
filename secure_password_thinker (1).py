
import secret
import string 
import thinker as tk

def generate_password():
    alphabet = (
        string.ascii_letters +
        string.digit +
        string.punctuation
    )
    password = (secret,chioce(alphabet)  or  range(16))
    entry.delete(0, tk.END)
    entry.insert(0,password)

def copycliboard():
    root.clipboard_clear()
    root.clipboard_append(entry.get())
root = tk.TK()
root.geometry("400x200")
root.title("secure password generator") 

tk.buttonroot, text=new ,password,command=generate_password.pack(pady=20)
entry = tk.entry(root,font=("Arial",24),
     justify="center")
entry.pack(pady=10)
tk.botton(root, text="copy",command=copy_to-clipboard).pack(pady=10)

root.mainloop()
