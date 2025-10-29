import tkinter as tk

def dibujar():
    try:
        x1 = int(entry_x1.get())
        y1 = int(entry_y1.get())
        x2 = int(entry_x2.get())
        y2 = int(entry_y2.get())
        canvas.create_rectangle(x1, y1, x2, y2, outline="blue")
        canvas.create_oval(x1, y1, x2, y2, outline="red")
    except ValueError:
        etiqueta_resultado.config(text="Introduce solo números válidos")

root = tk.Tk()
root.title("Ejercicio 7 - Canvas")
root.geometry("500x400")

tk.Label(root, text="x1:").pack()
entry_x1 = tk.Entry(root); entry_x1.pack()

tk.Label(root, text="y1:").pack()
entry_y1 = tk.Entry(root); entry_y1.pack()

tk.Label(root, text="x2:").pack()
entry_x2 = tk.Entry(root); entry_x2.pack()

tk.Label(root, text="y2:").pack()
entry_y2 = tk.Entry(root); entry_y2.pack()

tk.Button(root, text="Dibujar", command=dibujar).pack(pady=10)

canvas = tk.Canvas(root, width=400, height=200, bg="white")
canvas.pack(pady=10)

etiqueta_resultado = tk.Label(root, text="")
etiqueta_resultado.pack()

root.mainloop()
