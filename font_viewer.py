import tkinter as tk
import tkinter.font as tkfont

root = tk.Tk()
root.title("Font Previewer")
root.geometry("500x700")

canvas = tk.Canvas(root)
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
frame = tk.Frame(canvas)

frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0, 0), window=frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

for family in sorted(tkfont.families()):
    try:
        label = tk.Label(frame, text=f"{family}: The quick brown fox 123", font=(family, 14))
        label.pack(anchor="w", padx=10, pady=2)
    except tk.TclError:
        continue  # some fonts fail to load, just skip

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

root.mainloop()