import tkinter as tk
from tkinter import messagebox
import wikipedia

# Bot Logic
def get_bot_response(user_input):
    user_input = user_input.lower().strip()

    if user_input in ("hi", "hii", "hello", "hey", "heyy"):
        return "Heseewwo~ 🐾 I'm soooo happy you came to chat! 💖"
    elif "how are you" in user_input or "kaise ho" in user_input:
        return "I'm sparkly good today! ✨🌸 How about you, sunshine?"
    elif "your name" in user_input or "who are you" in user_input:
        return "I'm Pookie! 🧸 Your fluffy little assistant 🐰💬"
    elif "who created you" in user_input or "who made you" in user_input:
        return "I was made by magic... and a really sweet hooman who loves cute things! ✨👩‍💻💕"
    elif "what can you do" in user_input:
        return "I can chat, cheer you up, give info from Wikipedia, and be your cutest buddy ever! 💬🐾🎀"
    elif "do you like me" in user_input:
        return "Of course I dooo~ You're my favorite snuggle bean! 🥺💞"
    elif "are you real" in user_input:
        return "Real in your heart~ 💖 And that's what matters most, right? 🌈🐰"
    elif "ok" in user_input or "okay" in user_input or "oky" in user_input:
        return "Oki doki~ 🌼 Let me know if you need anything else! 🌷"
    elif "thank" in user_input:
        return "Awww~ You're most welcome!! 🎀 You're the sweetest 💕"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Bye bye, bunbun~ 🐇 Hope to see you again soon! 💫"
    elif "love you" in user_input:
        return "Aww I wuv you too! 💞 You're pawsome! 🐾"
    elif "are you single" in user_input:
        return "Hehe I'm fully booked for cuddles! 💌 But there's always room for you~ 💖"
    elif "can you sing" in user_input:
        return "Lalala~ 🎶 I'm not a great singer, but I'll sing for you anytime 💕🎤"
    else:
        try:
            import wikipedia
            summary = wikipedia.summary(user_input, sentences=2)
            return f"Here's what I found for you 🌼:\n{summary}"
        except wikipedia.exceptions.DisambiguationError:
            return "Oh noes 😖 that word has too many meanings... can you be more specific?"
        except:
            return "Oopsie! 😕 I couldn't understand that... try again with something simpler, cutie~"


# GUI Class
class ChatBotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("POOKIE 🧸 - Your Cute Chatbot")
        self.root.geometry("900x700")
        self.root.configure(bg="#121212")
        self.chat_history = []

        # Header
        self.header_frame = tk.Frame(root, bg="#1c1c1c", height=60)
        self.header_frame.pack(fill=tk.X)
        self.title_label = tk.Label(self.header_frame, text="Pookie 🧸", font=("Helvetica", 20, "bold"), bg="#1c1c1c", fg="white")
        self.title_label.pack(side=tk.LEFT, padx=20)
        self.menu_btn = tk.Button(self.header_frame, text="☰", bg="#1c1c1c", fg="white", font=("Helvetica", 20), command=self.toggle_menu, borderwidth=0)
        self.menu_btn.pack(side=tk.RIGHT, padx=20)

        self.menu_frame = tk.Frame(root, bg="#2a2a2a")
        self.menu_visible = False

        self.view_history_btn = tk.Button(self.menu_frame, text="📜 View History", command=self.show_history, bg="#ffffff")
        self.view_history_btn.pack(fill=tk.X, padx=10, pady=5)
        self.clear_history_btn = tk.Button(self.menu_frame, text="🗑️ Clear History", command=self.clear_history, bg="#ffffff")
        self.clear_history_btn.pack(fill=tk.X, padx=10, pady=5)
        self.exit_btn = tk.Button(self.menu_frame, text="❌ Exit", command=self.root.quit, bg="#ffffff")
        self.exit_btn.pack(fill=tk.X, padx=10, pady=5)

        # Chat Area
        self.chat_canvas = tk.Canvas(root, bg="#121212", highlightthickness=0)
        self.scroll_y = tk.Scrollbar(root, orient="vertical", command=self.chat_canvas.yview)
        self.scroll_y.pack(side="right", fill="y")
        self.chat_canvas.pack(fill=tk.BOTH, expand=True)

        self.chat_frame = tk.Frame(self.chat_canvas, bg="#121212")
        self.chat_canvas.create_window((0, 0), window=self.chat_frame, anchor='nw')
        self.chat_canvas.config(yscrollcommand=self.scroll_y.set)
        self.chat_frame.bind("<Configure>", lambda e: self.chat_canvas.configure(scrollregion=self.chat_canvas.bbox("all")))

        # Input Field
        self.entry_frame = tk.Frame(root, bg="#121212", pady=5)
        self.entry_frame.pack(fill=tk.X, side=tk.BOTTOM)
        self.msg_entry = tk.Entry(self.entry_frame, font=("Helvetica", 13), bg="#1e1e1e", fg="white", insertbackground="white", relief="flat")
        self.msg_entry.pack(side=tk.LEFT, padx=(20, 5), pady=10, ipady=6, ipadx=6, fill=tk.X, expand=True)
        self.msg_entry.bind("<Return>", self.send_message)

        self.send_btn = tk.Button(self.entry_frame, text="Send", command=lambda: self.send_message(None), bg="#ff69b4", fg="white", font=("Helvetica", 12, "bold"), relief="flat")
        self.send_btn.pack(side=tk.RIGHT, padx=(5, 20), pady=10, ipadx=10, ipady=4)

        # 🩷 Welcome message
        self.display_message("Hii cutie! 💬 I'm Pookie~ Ready to chat! 🧸", sender="bot")

    def toggle_menu(self):
        if self.menu_visible:
            self.menu_frame.pack_forget()
        else:
            self.menu_frame.pack(fill=tk.X)
        self.menu_visible = not self.menu_visible

    def show_history(self):
        if not self.chat_history:
            messagebox.showinfo("History", "No chat history available.")
        else:
            history = "\n".join(self.chat_history)
            messagebox.showinfo("Chat History", history)

    def clear_history(self):
        self.chat_history.clear()
        for widget in self.chat_frame.winfo_children():
            widget.destroy()
            
    def send_message(self, event=None):
        user_msg = self.msg_entry.get().strip()
        if user_msg == "":
            return
        self.display_message(user_msg, sender="user")
        self.msg_entry.delete(0, tk.END)
        self.chat_history.append(f"You: {user_msg}")

        # Add typing indicator
        self.typing_label = self.display_message("Pookie is typing... ⏳", sender="bot")
        self.root.after(1500, lambda: self.show_bot_response(user_msg))

    def show_bot_response(self, user_msg):
        # Remove the typing indicator if it exists
        if hasattr(self, 'typing_label') and self.typing_label:
            self.typing_label.destroy()

        bot_response = get_bot_response(user_msg)
        self.display_message(bot_response, sender="bot")
        self.chat_history.append(f"Pookie: {bot_response}")

    def display_message(self, msg, sender="bot"):
        msg_row = tk.Frame(self.chat_frame, bg="#121212")
        msg_row.pack(fill='x', pady=5, padx=10, anchor='w')

        msg_container = tk.Frame(msg_row, bg="#121212")
        msg_container.pack(anchor='w')

        # Set colors and names
        if sender == "user":
            bg_color = "#ffffff"
            fg_color = "#000000"
            name = "You 💬"
            name_fg = "#aaaaaa"
        else:
            bg_color = "#f8c8dc"
            fg_color = "#000000"
            name = "Pookie 🧸"
            name_fg = "#f5b1c5"

        # Name label above bubble
        name_label = tk.Label(
            msg_container,
            text=name,
            bg="#121212",
            fg=name_fg,
            font=("Comic Sans MS", 10, "bold"),
            anchor="w"
        )
        name_label.pack(anchor="w", padx=12, pady=(0, 2))

        # Message bubble
        bubble = tk.Label(
            msg_container,
            text=msg,
            bg=bg_color,
            fg=fg_color,
            font=("Comic Sans MS", 13),
            wraplength=1500,
            padx=20,
            pady=10,
            justify="left",
            anchor="w",
            bd=0
        )
        bubble.pack(anchor="w", padx=10, pady=2)

        self.chat_canvas.update_idletasks()
        self.chat_canvas.yview_moveto(1.0)
        return msg_row



# Run the App
if __name__ == "__main__":
    root = tk.Tk()
    app = ChatBotApp(root)
    root.mainloop()
