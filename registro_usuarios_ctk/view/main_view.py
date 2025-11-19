class MainView:
    def __init__(self, master):
        self.master = master

        master.grid_columnconfigure(0, weight=1)
        master.grid_columnconfigure(1, weight=2)

