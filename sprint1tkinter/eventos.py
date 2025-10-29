import tkinter as tk

def dibujar_circulo(event):
    x, y = event.x, event.y
    canvas.create_oval(x-15, y-15, x+15, y+15, fill="blue")

def limpiar_canvas(event):
    canvas.delete("all")

root = tk.Tk()
root.title("Ejercicio 13 - Eventos")
root.geometry("400x400")

canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

canvas.bind("<Button-1>", dibujar_circulo)
canvas.bind_all("<Key-c>", limpiar_canvas)

root.mainloop()
