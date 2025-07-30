import tkinter as tk
from tkinter import Canvas, Frame, Scrollbar, Entry, Button
from assistant_core import responder_pergunta_loja

class ChatBubble(Frame):
    def __init__(self, master, text, is_user=False, wraplength=400, **kwargs):
        super().__init__(master, bg=master['bg'], **kwargs)
        bubble_color = "#DCF8C6" if is_user else "#FFFFFF"
        text_color = "#000000"
        anchor_align = "e" if is_user else "w"
        bubble_padx = (60, 10) if is_user else (10, 60)
        max_bubble_width = 400

        self.label = tk.Label(
            self,
            text=text,
            bg=bubble_color,
            fg=text_color,
            wraplength=wraplength,
            justify='left',
            anchor='w',
            font=("Segoe UI", 10),
            padx=10,
            pady=7
        )
        self.label.pack(
            anchor=anchor_align,
            padx=bubble_padx,
            pady=(2, 2),
            fill='both',
            expand=True
        )
        self.label.config(relief="flat", bd=0)

    def set_wraplength(self, wraplength):
        self.label.config(wraplength=wraplength)

class ChatInterface(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Assistente TrueTec")
        self.geometry("400x700")
        self.resizable(False, False)
        self.configure(bg="#E5DDD5")

        self.canvas = Canvas(self, bg="#E5DDD5", highlightthickness=0)
        self.scrollbar = Scrollbar(self.canvas, orient="vertical", command=self.canvas.yview)
        self.chat_frame = Frame(self.canvas, bg="#E5DDD5")
        self.chat_frame.bind("<Configure>", self._on_frame_configure)
        self.chat_frame_id = self.canvas.create_window((0, 0), window=self.chat_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side="top", fill="both", expand=True, padx=0, pady=(0, 5))
        self.scrollbar.pack(side="right", fill="y")

        input_frame = Frame(self, bg="#E5DDD5")
        input_frame.pack(side="bottom", fill="x", padx=10, pady=10)

        self.entry = Entry(input_frame, font=("Segoe UI", 11), bd=1, relief="solid", highlightbackground="#CCCCCC", highlightthickness=1)
        self.entry.pack(side="left", fill="x", expand=True, padx=(0, 5))
        self.entry.bind("<Return>", self.enviar_pergunta)

        self.send_button = Button(
            input_frame,
            text="Enviar",
            font=("Segoe UI", 10, "bold"),
            bg="#25D366",
            fg="white",
            activebackground="#1DA851",
            activeforeground="white",
            relief="flat",
            command=self.enviar_pergunta
        )
        self.send_button.pack(side="right")

        self.conversation_history = []
        self.bubbles = []

        self.adicionar_mensagem("Olá! Bem-vindo(a) à TrueTec, sua assistente virtual aqui em Teresina. Como posso ajudar hoje?", is_user=False)

    def _on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def _on_canvas_configure(self, event):
        canvas_width = event.width
        self.canvas.itemconfig(self.chat_frame_id, width=canvas_width)
        wrap = max(220, min(canvas_width - 70, 380))
        for bubble in self.bubbles:
            bubble.set_wraplength(wrap)

    def adicionar_mensagem(self, mensagem, is_user):
        canvas_width = self.canvas.winfo_width() or 400
        wrap = max(220, min(canvas_width - 70, 380))
        bubble = ChatBubble(self.chat_frame, mensagem, is_user, wraplength=wrap)
        bubble.pack(anchor="e" if is_user else "w", fill="x", expand=True, pady=2, padx=5)
        self.bubbles.append(bubble)
        self.canvas.update_idletasks()
        self.canvas.yview_moveto(1.0)

    def enviar_pergunta(self, event=None):
        pergunta = self.entry.get().strip()
        if not pergunta:
            return
        self.adicionar_mensagem(pergunta, is_user=True)
        self.entry.delete(0, tk.END)
        if pergunta.lower() == 'sair':
            self.adicionar_mensagem("Obrigado por entrar em contato com a TrueTec. Esperamos vê-lo(a) novamente!", is_user=False)
            self.after(1500, self.destroy)
            return
        digitando_bubble = ChatBubble(self.chat_frame, "Digitando...", is_user=False, wraplength=380)
        digitando_bubble.pack(anchor="w", fill="x", expand=True, pady=2, padx=5)
        self.bubbles.append(digitando_bubble)
        self.canvas.update_idletasks()
        self.canvas.yview_moveto(1.0)
        self.conversation_history.append({"role": "user", "parts": [{"text": pergunta}]})
        resposta = responder_pergunta_loja(pergunta, self.conversation_history)
        digitando_bubble.destroy()
        self.bubbles.remove(digitando_bubble)
        self.adicionar_mensagem(resposta, is_user=False)
        self.conversation_history.append({"role": "model", "parts": [{"text": resposta}]})

if __name__ == "__main__":
    app = ChatInterface()
    app.mainloop()