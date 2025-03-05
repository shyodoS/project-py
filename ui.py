from tkinter import *
from tkinter import ttk, messagebox
import ctypes
from database import Database


class CrudInterface:
    def __init__(self):
        self.db = Database()
        self.root = Tk()
        self.root.title("CRUD ALUNO")
        self.root.geometry(self.centralizar_janela(self.root, 650, 500))
        self.root.resizable(False, False)
        self.root.config(bg='black')

        self.root.update_idletasks()
        hwnd = ctypes.windll.user32.GetParent(self.root.winfo_id())
        ctypes.windll.dwmapi.DwmSetWindowAttribute(hwnd, 35, ctypes.byref(ctypes.c_int(1)), ctypes.sizeof(ctypes.c_int))

        self.var_id = StringVar()
        self.var_id.set('?')

        self.containers()
        self.itens_container01()
        self.itens_container02()  # Corrigido para chamar o método correto
        self.preencher_tabela()
        self.root.mainloop()

    def containers(self):
        self.fr_container01 = Frame(self.root, height=200, width=650, bg='#002333')
        self.fr_container02 = Frame(self.root, height=300, width=650, bg='#002333')

        self.fr_container01.propagate(0)
        self.fr_container02.propagate(0)
        self.fr_container01.pack()
        self.fr_container02.pack()

    def itens_container01(self):
        self.fr_container_title = Frame(self.fr_container01, bg=self.fr_container01.cget('bg'))
        self.fr_container_infos_user = Frame(self.fr_container01, bg=self.fr_container01.cget('bg'))
        self.fr_container_buttons = Frame(self.fr_container01, bg=self.fr_container01.cget('bg'))

        self.lb_title = Label(
            self.fr_container_title,
            text='Sistema de cadastro de alunos',
            font='Calibri 19 bold',
            fg="white",
            bg=self.fr_container_title.cget('bg')
        )

        self.lb_id_aluno = Label(self.fr_container_infos_user, text='Id do aluno:', font='Calibri 11 bold', fg='white', bg=self.fr_container_infos_user.cget('bg'))
        self.lb_id_aluno_value = Label(self.fr_container_infos_user, textvariable=self.var_id, font='Calibri 11 bold', fg='white', bg=self.fr_container_infos_user.cget('bg'))

        self.lb_nome_aluno = Label(self.fr_container_infos_user, text='Nome do aluno:', font='Calibri 11 bold', fg='white', bg=self.fr_container_infos_user.cget('bg'))
        self.en_nome_aluno = Entry(self.fr_container_infos_user, width=30, font='Calibri 11', bd=0, fg='white', insertbackground='white', highlightthickness=1, highlightbackground='grey', highlightcolor='#159A9C', bg=self.fr_container_infos_user.cget('bg'))

        self.lb_email_aluno = Label(self.fr_container_infos_user, text='Email do aluno:', font='Calibri 11 bold', fg='white', bg=self.fr_container_infos_user.cget('bg'))
        self.en_email_aluno = Entry(self.fr_container_infos_user, width=30, font='Calibri 11', bd=0, fg='white', insertbackground='white', highlightthickness=1, highlightbackground='grey', highlightcolor='#159A9C', bg=self.fr_container_infos_user.cget('bg'))

        self.lb_curso_aluno = Label(self.fr_container_infos_user, text='Curso do aluno:', font='Calibri 11 bold', fg='white', bg=self.fr_container_infos_user.cget('bg'))
        self.en_curso_aluno = Entry(self.fr_container_infos_user, width=30, font='Calibri 11', bd=0, fg='white', insertbackground='white', highlightthickness=1, highlightbackground='grey', highlightcolor='#159A9C', bg=self.fr_container_infos_user.cget('bg'))

        self.lb_valor_aluno = Label(self.fr_container_infos_user, text='Valor do curso:', font='Calibri 11 bold', fg='white', bg=self.fr_container_infos_user.cget('bg'))
        self.en_valor_aluno = Entry(self.fr_container_infos_user, width=30, font='Calibri 11', bd=0, fg='white', insertbackground='white', highlightthickness=1, highlightbackground='grey', highlightcolor='#159A9C', bg=self.fr_container_infos_user.cget('bg'))

        self.btn_adicionar = Button(self.fr_container_buttons, text='ADD', bg='#298073', cursor="hand2", command=self.adicionar_registro)
        self.btn_update = Button(self.fr_container_buttons, text='UPDATE', bg='#184C78', command=self.update_registro)
        self.btn_delete = Button(self.fr_container_buttons, text='DELETE', bg='#8C1F28', activebackground=self.fr_container01.cget("bg"), cursor="hand2", command=self.excluir_registro)

        self.fr_container_title.pack(anchor=W)
        self.fr_container_infos_user.pack(anchor=W)
        self.fr_container_buttons.pack(anchor=W, padx=215, pady=5)

        self.lb_title.pack()

        self.lb_id_aluno.grid(row=0, column=0, sticky=W)
        self.lb_id_aluno_value.grid(row=0, column=1, sticky=W)
        self.lb_nome_aluno.grid(row=1, column=0, sticky=W)
        self.en_nome_aluno.grid(row=1, column=1, sticky=W)
        self.lb_email_aluno.grid(row=2, column=0, sticky=W)
        self.en_email_aluno.grid(row=2, column=1, sticky=W)
        self.lb_curso_aluno.grid(row=3, column=0, sticky=W)
        self.en_curso_aluno.grid(row=3, column=1, sticky=W)
        self.lb_valor_aluno.grid(row=4, column=0, sticky=W)
        self.en_valor_aluno.grid(row=4, column=1, sticky=W)

        self.btn_adicionar.grid(row=0, column=0, sticky=W)
        self.btn_update.grid(row=0, column=1, sticky=W)
        self.btn_delete.grid(row=0, column=2, sticky=W)

    def itens_container02(self):
        self.treeview = ttk.Treeview(self.fr_container02, columns=('id', 'nome', 'email', 'curso', 'valor'), show='headings')
        self.treeview.heading('id', text='ID')
        self.treeview.heading('nome', text='Nome')
        self.treeview.heading('email', text='Email')
        self.treeview.heading('curso', text='Curso')
        self.treeview.heading('valor', text='Valor')

        self.treeview.bind('<Double-1>', self.captar_registros)  # Agora chamando o método captar_registros
        self.treeview.pack(fill='both', expand=True, padx=10, pady=10)

    def captar_registros(self, event):
        item = self.treeview.selection()[0]  # Captura o item selecionado
        dados = self.treeview.item(item, 'values',)
        
        # Preenche os campos com os dados do aluno
        self.var_id.set(dados[0])
        self.en_nome_aluno.delete(0, END)
        self.en_nome_aluno.insert(0, dados[1])
        self.en_email_aluno.delete(0, END)
        self.en_email_aluno.insert(0, dados[2])
        self.en_curso_aluno.delete(0, END)
        self.en_curso_aluno.insert(0, dados[3])
        self.en_valor_aluno.delete(0, END)
        self.en_valor_aluno.insert(0, dados[4])

    def adicionar_registro(self):
        if self.var_id.get() == '?':
            if self.validar_entrys():
                try:
                    self.db.execute_query(
                        "INSERT INTO aluno (nome, email, curso, valor) VALUES (%s, %s, %s, %s)",
                        (self.en_nome_aluno.get(), self.en_email_aluno.get(), self.en_curso_aluno.get(), self.en_valor_aluno.get())
                    )
                    self.resetar_entrys()
                    self.preencher_tabela()
                except Exception as e:
                    messagebox.showerror("Erro", f"Erro ao adicionar registro: {e}")
            else:
                messagebox.showinfo("","Existem campos vazios, por favor preencha")

    def update_registro(self):
        id_aluno = self.var_id.get()
        if id_aluno != '?':
            confirmed = messagebox.askyesno("Confirmação","Deseja atualizar registro?")
            if confirmed:
                try:
                    self.db.execute_query(
                        "UPDATE aluno SET nome = %s, email = %s, curso = %s, valor = %s WHERE id = %s",
                        (self.en_nome_aluno.get(), self.en_email_aluno.get(), self.en_curso_aluno.get(), self.en_valor_aluno.get(), id_aluno)
                    )
                    messagebox.showinfo("", f"Registro {id_aluno} Atualizado com sucesso!")
                    self.resetar_entrys()
                    self.preencher_tabela()
                except Exception as e:
                    messagebox.showerror("Erro", f"Erro ao atualizar registro: {e}")

    def excluir_registro(self):
        id_aluno = self.var_id.get()
        if id_aluno != '?':
            confirmed = messagebox.askyesno("Confirmação", "Deseja excluir registro?")
            if confirmed:
                try:
                    self.db.execute_query("DELETE FROM aluno WHERE id = %s", (id_aluno,))
                    messagebox.showinfo("", f"Registro {id_aluno} Excluído com sucesso!")
                    self.resetar_entrys()
                    self.preencher_tabela()
                except Exception as e:
                    messagebox.showerror("Erro", f"Erro ao excluir registro: {e}")

    def preencher_tabela(self):
        registros = self.db.fetchall('SELECT * FROM aluno')
        for i in self.treeview.get_children():
            self.treeview.delete(i)
        for registro in registros:
            self.treeview.insert("", "end", values=registro)

    def resetar_entrys(self):
        self.var_id.set('?')
        self.en_nome_aluno.delete(0, END)
        self.en_email_aluno.delete(0, END)
        self.en_curso_aluno.delete(0, END)
        self.en_valor_aluno.delete(0, END)

    def validar_entrys(self):
        if self.en_nome_aluno.get() == "" or self.en_email_aluno.get() == "" or self.en_curso_aluno.get() == "" or self.en_valor_aluno.get() == "":
            return False
        return True

    def centralizar_janela(self, janela, largura, altura):
        largura_screen = janela.winfo_screenwidth()
        altura_screen = janela.winfo_screenheight()

        posx = largura_screen / 2 - largura / 2
        posy = altura_screen / 2 - altura / 2

        centro = '%dx%d+%d+%d' % (largura, altura, posx, posy)
        return centro
