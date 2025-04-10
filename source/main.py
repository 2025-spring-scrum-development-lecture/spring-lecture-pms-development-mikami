import tkinter as tk
from accoReservation import AccoReservationSystem
from enkai import HotelReservationSystem
class MainTop(tk.Frame): #master ← ウィンドウ
    def __init__ (self, master):
        super().__init__(master)
        self.master = master
        self.pack()
        
        master.geometry('800x600')
        master.title('ホテル予約システム')
        
        self.create_widgets()
        
    # ウィジェットを配置して画面を作るメソッド
    def create_widgets(self):
        # タイトル
        title_label = tk.Label(self, text="ホテル予約システム", font=("Arial", 24))
        title_label.grid(row=0, column=0, pady=50, columnspan=3)
        
        # 宿泊ボタン
        accommodation_button = tk.Button(
            self, 
            text="宿泊予約", 
            font=("Arial", 16),
            width=15, 
            height=2,
            command=self.acco_button_click
        )
        accommodation_button.grid(row=1, column=0, padx=20, pady=20)
        
        # 宴会ボタン
        banquet_button = tk.Button(
            self, 
            text="宴会予約", 
            font=("Arial", 16),
            width=15, 
            height=2,
            command=self.bunq_button_click
        )
        banquet_button.grid(row=1, column=1, padx=20, pady=20)
    
    def acco_button_click(self):
        self.destroy()
        AccoReservationSystem(self.master)
    
    def bunq_button_click(self):
        self.destroy()
        HotelReservationSystem(self.master)
        
if __name__ == '__main__':
    root = tk.Tk()
    app = MainTop(root)
    app.mainloop()
