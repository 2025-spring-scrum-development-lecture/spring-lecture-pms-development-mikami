import tkinter as tk
from tkinter import ttk, messagebox
import tkinter.ttk as ttk
import calendar
import datetime
from mail import send_mail
import json

class AccoReservationSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("ホテル予約システム")
        self.root.geometry("800x600")
        
        # メインフレーム
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill="both", expand=True)
    
        # 各画面のフレームを格納する辞書
        self.frames = {}
        
        # 予約情報を保存する変数
        self.reservation_data = {
            "type": "accommodation",
            "plan": "",
            "room": "",
            "date": "",
            "guests": {"adults": 1, "children": 0},
            "options": [],
            "personal_info": {}
        }
        # 各画面を作成
        self.create_accommodation_plan_page()
        self.create_room_selection_page()
        self.create_calendar_page()
        self.create_options_page()
        self.create_personal_info_page()


        
            
        # 初期画面を表示
        self.show_frame("accommodation_plan_page")
        
    def create_accommodation_plan_page(self):
        frame = tk.Frame(self.main_frame)
        self.frames["accommodation_plan_page"] = frame
        
        # タイトル
        title_label = tk.Label(frame, text="宿泊プラン選択", font=("Arial", 20))
        title_label.pack(pady=30)
        
        # スクロール可能なプラン表示
        canvas = tk.Canvas(frame)
        scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        plans_frame = tk.Frame(canvas)
        
        canvas.create_window((0, 0), window=plans_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        
        plans = [
        {"name": "【朝食付き】 観光、ビジネス！一泊朝食プラン", "price": "8,500円〜", "description": "スタンダードな宿泊プランです。朝食付き。"},
        {"name": "【2025ゴールデンウィーク★プレミアムプラン】前沢牛の豪華会席", "price": "20,000円〜", "description": "広めのお部屋で快適に過ごせます。朝食・夕食付き。"},
        {"name": "【スタンダード】【HP特価】八幡平産杜仲茶ポークの和食膳プラン", "price": "14,600円〜", "description": "最上級のおもてなしを体験できます。オールインクルーシブ。"},
        {"name": "【八幡平の地ビール・ドラゴンアイビールで乾杯】", "price": "14,600円〜", "description": "最上級のおもてなしを体験できます。オールインクルーシブ。"},
        {"name": "【早期割90日前予約で15%割引】岩手山牛と八幡平産杜仲茶ポーク", "price": "13,260円〜", "description": "最上級のおもてなしを体験できます。オールインクルーシブ。"},
        {"name": "【北投石の岩盤浴】豊かな八幡平の自然と岩盤浴でリフレッシュ", "price": "15,800円〜", "description": "最上級のおもてなしを体験できます。オールインクルーシブ。"},
        {"name": "【イースター復活祭】×【女子旅】", "price": "13,800円〜", "description": "最上級のおもてなしを体験できます。オールインクルーシブ。"},
        {"name": "【早期割60日前予約で10%割引】岩手山牛と八幡平産杜仲茶ポーク", "price": "14,040円〜", "description": "最上級のおもてなしを体験できます。オールインクルーシブ。"},
        {"name": "【母の日プラン】カーネーションフラワーアレンジメント", "price": "14,500円〜", "description": "最上級のおもてなしを体験できます。オールインクルーシブ。"},
        {"name": "【岩手県産牛】岩手県産牛と八幡平産杜仲茶ポークを味わう", "price": "15,400円〜", "description": "最上級のおもてなしを体験できます。オールインクルーシブ。"},
        {"name": "【1泊2章のお子様3000円！】【2025春休み】家族旅行応援", "price": "15,600円〜", "description": "最上級のおもてなしを体験できます。オールインクルーシブ。"},
        {"name": "【早期割90日前予約で15%割引】前沢牛・伊勢海老・あわび・ズワイガニ", "price": "18,360円〜", "description": "最上級のおもてなしを体験できます。オールインクルーシブ。"},
        {"name": "【前沢牛】前沢牛の網焼きとロースト握り和食膳プラン", "price": "18,400円〜", "description": "最上級のおもてなしを体験できます。オールインクルーシブ。"},
        {"name": "【前沢牛】前沢牛のせいろ蒸しとロースト握り和食膳プラン", "price": "18,400円〜", "description": "最上級のおもてなしを体験できます。オールインクルーシブ。"},
        {"name": "【赤ちゃんプラン】お子様歓迎♪パパママも嬉しい12個の特典付き", "price": "18,800円〜", "description": "最上級のおもてなしを体験できます。オールインクルーシブ。"},
        {"name": "【赤ちゃんプラン・お食い初め】", "price": "18,800円〜", "description": "最上級のおもてなしを体験できます。オールインクルーシブ。"},
        {"name": "【8/13～8/15】2025お盆期間限定♪お子様歓迎！", "price": "19.000円〜", "description": "最上級のおもてなしを体験できます。オールインクルーシブ。"},
        {"name": "【早期割60日前予約で10%割引】前沢牛・伊勢海老・あわび・ズワイガニ", "price": "19.440円〜", "description": "最上級のおもてなしを体験できます。オールインクルーシブ。"},
        ]
        
        for plan in plans:
            plan_frame = tk.Frame(plans_frame, bd=2, relief=tk.GROOVE, bg="white")
            plan_frame.pack(pady=20, padx=10, fill="x", expand=True)
            
            name_label = tk.Label(plan_frame, text=plan["name"], font=("Arial", 12, "bold"), bg="white")
            name_label.pack(anchor="w", pady=5)
            
            price_label = tk.Label(plan_frame, text=plan["price"], font=("Arial", 10), bg="white", fg="green")
            price_label.pack(anchor="w", pady=5)
            
            desc_label = tk.Label(plan_frame, text=plan["description"], font=("Arial", 10), bg="white", wraplength=400)
            desc_label.pack(anchor="w", pady=5)
            
            select_button = tk.Button(plan_frame, text="選択", command=lambda p=plan["name"]: self.select_accommodation_plan(p))
            select_button.pack(anchor="e", padx=10, pady=5)

        plans_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    # 部屋選択画面の作成関数
    def create_room_selection_page(self):
        frame = tk.Frame(self.main_frame)
        self.frames["room_selection_page"] = frame
        
        # タイトル
        title_label = tk.Label(frame, text="部屋タイプ選択", font=("Arial", 20))
        title_label.pack(pady=30)
        
        # スクロール可能な部屋表示
        canvas = tk.Canvas(frame)
        scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        rooms_frame = tk.Frame(canvas)
        
        canvas.create_window((0, 0), window=rooms_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        
        rooms = [
            {"name": "本館 和室7.5畳間", "price": "追加料金無し", "description": "スタンダードな和室"},
            {"name": "岩手山側和室10畳間", "price": "追加料金無し", "description": "岩手山側の眺望がある和室"},
            {"name": "西館 和室10畳間", "price": "追加料金無し", "description": "西館側の和室"},
            {"name": "西館 洋室(ツイン) 禁煙", "price": "追加料金無し", "description": "西館側の洋室ツインベッド"},
            {"name": "西館 和洋室(バリアフリー/ツイン+和室7.5畳間)", "price": "追加料金無し", "description": "バリアフリー対応の和洋室"},
            {"name": "西館 和室28畳間", "price": "追加料金無し", "description": "広めの和室"},
            {"name": "岩手山展望露天風呂付き和室", "price": "2,000円", "description": "岩手山側の眺望と露天風呂付き"},
            {"name": "檜の内風呂付本館和洋室", "price": "3,000円", "description": "檜風呂付きの和洋室"},
            {"name": "別館姫神「黒倉の間」「源太の間」(温泉露天風呂付き)", "price": "13,500~円", "description": "別館の露天風呂付き高級客室"},
            {"name": "別館姫神「見返の間」(温泉内風呂付き)", "price": "16,500円", "description": "別館の温泉内風呂付き高級客室"},
            {"name": "別館姫神「茶臼の間」「七時雨の間」(檜の温泉内風呂付き)", "price": "16,500円", "description": "別館の檜温泉内風呂付き高級客室"},
            {"name": "別館姫神「貴賓室」(檜の温泉内風呂付き)", "price": "21,500円", "description": "皇室の方も宿泊した別館最高級客室"}
        ]
        
        for room in rooms:
            room_frame = tk.Frame(rooms_frame, bd=2, relief=tk.GROOVE, bg="white")
            room_frame.pack(pady=15, padx=10, fill="x", expand=True)
            
            name_label = tk.Label(room_frame, text=room["name"], font=("Arial", 12, "bold"), bg="white")
            name_label.pack(anchor="w", pady=5)
            
            details_frame = tk.Frame(room_frame, bg="white")
            details_frame.pack(fill="x", pady=5)
            
            price_label = tk.Label(room_frame, text=f"追加料金: {room['price']}", font=("Arial", 10), bg="white", fg="green")
            price_label.pack(anchor="w", pady=5, padx=10)
            
            desc_label = tk.Label(room_frame, text=room["description"], font=("Arial", 10), bg="white", wraplength=400)
            desc_label.pack(anchor="w", pady=5, padx=10)
            
            select_button = tk.Button(room_frame, text="選択", command=lambda r=room["name"]: self.select_room(r))
            select_button.pack(anchor="e", padx=10, pady=5)
        
        rooms_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        
        # 戻るボタン
        button_frame = tk.Frame(frame)
        button_frame.pack(side="bottom", fill="x", pady=20)
        
        back_button = tk.Button(
            button_frame, 
            text="戻る", 
            command=lambda: self.show_frame("accommodation_plan_page")
        )
        back_button.pack(side="left", padx=20)

    # 部屋選択関数
    def select_room(self, room):
        self.reservation_data["room"] = room
        self.show_frame("calendar_page")


    def create_calendar_page(self):
        frame = tk.Frame(self.main_frame)
        self.frames["calendar_page"] = frame
        
        # タイトル
        title_calendar_label = tk.Label(frame, text="予約日、人数選択", font=("Arial", 20))
        title_calendar_label.pack(pady=5)
        
        # カレンダーフレーム
        calendar_frame = tk.Frame(frame)
        calendar_frame.pack(pady=5)
        
        # 月選択
        now = datetime.datetime.now()
        months_frame = tk.Frame(calendar_frame)
        months_frame.pack(pady=5)
        
        tk.Label(months_frame, text="年月:", font=("Arial", 12)).grid(row=0, column=0)
        
        self.year_var = tk.StringVar(value=str(now.year))
        year_combo = ttk.Combobox(months_frame, textvariable=self.year_var, values=[str(now.year + i) for i in range(3)], width=6)
        year_combo.grid(row=0, column=1, padx=5)
        
        self.month_var = tk.StringVar(value=str(now.month))
        month_combo = ttk.Combobox(months_frame, textvariable=self.month_var, values=[str(i) for i in range(1, 13)], width=4)
        month_combo.grid(row=0, column=2, padx=5)
        
        # コンボボックスの値が変更されたときにカレンダーを更新
        year_combo.bind("<<ComboboxSelected>>", lambda e: self.update_calendar())
        month_combo.bind("<<ComboboxSelected>>", lambda e: self.update_calendar())
        
        # 更新ボタンは残してもよいですが、必須ではなくなります
        update_button = tk.Button(months_frame, text="更新", command=self.update_calendar)
        update_button.grid(row=0, column=3, padx=10)
        
        # カレンダー表示エリア
        self.cal_frame = tk.Frame(calendar_frame)
        self.cal_frame.pack(pady=10)
        
        # カレンダー表示エリア（既存のコード）
        self.cal_frame = tk.Frame(calendar_frame)
        self.cal_frame.pack(pady=10)
        
        self.update_calendar()
        
        # 人数選択フレーム（新規追加）
        guests_frame = tk.Frame(frame, bd=2, relief=tk.GROOVE)
        guests_frame.pack(pady=15, padx=50, fill="x")
        
        guests_label = tk.Label(guests_frame, text="宿泊人数", font=("Arial", 12, "bold"))
        guests_label.pack(anchor="w", pady=10, padx=10)
        
        # 大人の人数選択
        adults_frame = tk.Frame(guests_frame)
        adults_frame.pack(fill="x", pady=5, padx=20)
        
        tk.Label(adults_frame, text="大人:", width=10, anchor="w").pack(side="left")
        
        self.adults_var = tk.StringVar(value=str(self.reservation_data["guests"]["adults"]))
        adults_combo = ttk.Combobox(
            adults_frame, 
            textvariable=self.adults_var,
            values=[str(i) for i in range(1, 11)],  # 1〜10人
            width=5,
            state="readonly"
        )
        adults_combo.pack(side="left", padx=5)
        tk.Label(adults_frame, text="名").pack(side="left")
        
        # 子どもの人数選択
        children_frame = tk.Frame(guests_frame)
        children_frame.pack(fill="x", pady=5, padx=20)
        
        tk.Label(children_frame, text="子ども:", width=10, anchor="w").pack(side="left")
        
        self.children_var = tk.StringVar(value=str(self.reservation_data["guests"]["children"]))
        children_combo = ttk.Combobox(
            children_frame, 
            textvariable=self.children_var,
            values=[str(i) for i in range(11)],  # 0〜10人
            width=5,
            state="readonly"
        )
        children_combo.pack(side="left", padx=5)
        tk.Label(children_frame, text="名").pack(side="left")
        
        # コンボボックスの変更時にデータを更新するバインド
        adults_combo.bind("<<ComboboxSelected>>", lambda e: self.update_guests_count())
        children_combo.bind("<<ComboboxSelected>>", lambda e: self.update_guests_count())
        
        self.update_calendar()
        # 戻るボタン
        button_frame = tk.Frame(frame)
        button_frame.pack(side="bottom", fill="x", pady=20)
        
        back_button = tk.Button(
            button_frame, 
            text="戻る", 
            command=self.calendar_back_button_clicked
        )
        back_button.pack(side="left", padx=20)
        
        

    def create_options_page(self):
        frame = tk.Frame(self.main_frame)
        self.frames["options_page"] = frame
        
        # タイトル
        title_label = tk.Label(frame, text="オプション選択", font=("Arial", 20))
        title_label.pack(pady=2)
        
        # オプションフレーム
        options_frame = tk.Frame(frame)
        options_frame.pack(pady=20, fill="both", expand=True)
        
        # 宿泊オプション
        self.accommodation_options_frame = tk.Frame(options_frame)
        tk.Label(self.accommodation_options_frame, text="宿泊オプション", font=("Arial", 16)).pack(anchor="w", padx=50, pady=2)
        
        self.accommodation_options = [
        {"name": "姫神サーモンの釜飯", "price": "900円", "var": tk.IntVar(), "quantity_var": tk.StringVar(value="1人前")},
        {"name": "八幡平産杜仲茶ポークのホルモン鍋", "price": "1,100円", "var": tk.IntVar(), "quantity_var": tk.StringVar(value="1人前")},
        {"name": "岩手県産牛の串焼き", "price": "750円", "var": tk.IntVar(), "quantity_var": tk.StringVar(value="1人前")},
        {"name": "前沢牛の網焼きミニステーキ", "price": "3,600円", "var": tk.IntVar(), "quantity_var": tk.StringVar(value="1人前")},
        {"name": "前沢牛のせいろ蒸し", "price": "3,600円", "var": tk.IntVar(), "quantity_var": tk.StringVar(value="1人前")},
        {"name": "ズワイガニのしゃぶしゃぶ", "price": "2,100円", "var": tk.IntVar(), "quantity_var": tk.StringVar(value="1人前")},
        {"name": "ラジウム岩盤浴", "price": "1,500円", "var": tk.IntVar(), "quantity_var": tk.StringVar(value="1人前")},
        {"name": "温泉貸切風呂", "price": "2,500円", "var": tk.IntVar(), "quantity_var": tk.StringVar(value="1人前")}
    ]
    
        quantities = ['1人前', '2人前', '3人前', '4人前', '5人前', '6人前', '7人前', '8人前', '9人前', '10人前', '11人前', '12人前', '13人前', '14人前', '15人前']

        for option in self.accommodation_options:
            option_frame = tk.Frame(self.accommodation_options_frame)
            option_frame.pack(fill="x", padx=50, pady=5)
            
            tk.Checkbutton(option_frame, variable=option["var"], text=f"{option['name']} ({option['price']})").pack(side="left")
            
            # コンボボックスを変数に関連付け
            quantity_combo = ttk.Combobox(
                option_frame, 
                textvariable=option["quantity_var"],
                values=quantities, 
                width=7, 
                state='readonly'
            )
            quantity_combo.pack(side='right')
        # ボタンフレーム
        button_frame = tk.Frame(frame)
        button_frame.pack(side="bottom", fill="x", pady=20)
        
        back_button = tk.Button(
            button_frame, 
            text="戻る", 
            command=lambda: self.show_frame("calendar_page")
        )
        back_button.pack(side="left", padx=20)
        
        next_button = tk.Button(
            button_frame, 
            text="次へ", 
            command=self.options_next_button_clicked
        )
        next_button.pack(side="right", padx=20)
        
        
    def create_personal_info_page(self):
        frame = tk.Frame(self.main_frame)
        self.frames["personal_info_page"] = frame
        
        # タイトル
        title_label = tk.Label(frame, text="お客様情報入力", font=("Arial", 20))
        title_label.pack(pady=10)
        
        # 入力フォーム
        form_frame = tk.Frame(frame)
        form_frame.pack(pady=20, fill="both", expand=True)
        
        # 入力フィールド
        fields = [
            {"label": "お名前", "var": "name"},
            {"label": "フリガナ", "var": "name_kana"},
            {"label": "チェックイン時間", "var" : "checkin"},
            {"label": "電話番号", "var": "phone"},
            {"label": "メールアドレス", "var": "email"},
            {"label": "住所", "var": "address"}
        ]
        
        self.form_vars = {}
        
        for i, field in enumerate(fields):
            field_frame = tk.Frame(form_frame)
            field_frame.pack(fill="x", padx=50, pady=5)
            
            tk.Label(field_frame, text=field["label"], width=15, anchor="e").pack(side="left", padx=5)
            
            self.form_vars[field["var"]] = tk.StringVar()
            entry = tk.Entry(field_frame, textvariable=self.form_vars[field["var"]], width=40)
            entry.pack(side="left", padx=2)
        
        # 予約内容確認エリア
        summary_frame = tk.LabelFrame(frame, text="予約内容", font=("Arial", 12))
        summary_frame.pack(pady=20, padx=50, fill="x")
        
        self.summary_text = tk.Text(summary_frame, height=8, width=60, state="disabled")
        self.summary_text.pack(pady=10, padx=10)
        
        # メール送信の同意
        agreement_frame = tk.Frame(frame)
        agreement_frame.pack(pady=10)
        
        self.agreement_var = tk.IntVar()
        agreement_check = tk.Checkbutton(
            agreement_frame, 
            text="予約内容をメールで送信することに同意します", 
            variable=self.agreement_var
        )
        agreement_check.pack()
        
        # ボタンフレーム
        button_frame = tk.Frame(frame)
        button_frame.pack(side="bottom", fill="x", pady=20)
        
        back_button = tk.Button(
            button_frame, 
            text="戻る", 
            command=lambda: self.show_frame("options_page")
        )
        back_button.pack(side="left", padx=20)
        
        submit_button = tk.Button(
            button_frame, 
            text="予約確定", 
            command=self.submit_reservation
        )
        submit_button.pack(side="right", padx=20)
    
    def show_frame(self, frame_name):
        # すべてのフレームを非表示
        for frame in self.frames.values():
            frame.pack_forget()
        
        # 指定したフレームを表示
        self.frames[frame_name].pack(fill="both", expand=True)
        
        # オプション画面の場合、予約タイプに応じたオプションを表示
        if frame_name == "options_page":
            if self.reservation_data["type"] == "accommodation":
                self.accommodation_options_frame.pack(fill="both", expand=True)
            else:
                self.accommodation_options_frame.pack_forget()
        
        # 個人情報画面の場合、予約内容を表示
        if frame_name == "personal_info_page":
            self.update_reservation_summary()
    
    def update_guests_count(self):
        self.reservation_data["guests"]["adults"] = int(self.adults_var.get())
        self.reservation_data["guests"]["children"] = int(self.children_var.get())
    def update_calendar(self):
        # カレンダーフレームの子ウィジェットをクリア
        for widget in self.cal_frame.winfo_children():
            widget.destroy()
        
        # 年月を取得
        year = int(self.year_var.get())
        month = int(self.month_var.get())
        
        # カレンダーを取得
        cal = calendar.monthcalendar(year, month)
        
        # 曜日ラベル
        weekdays = ["月", "火", "水", "木", "金", "土", "日"]
        for i, day in enumerate(weekdays):
            tk.Label(self.cal_frame, text=day, width=5, font=("Arial", 10, "bold")).grid(row=0, column=i)
        
        # 日付ボタン
        now = datetime.datetime.now()
        current_day = now.day if year == now.year and month == now.month else 0
        
        for week_idx, week in enumerate(cal):
            for day_idx, day in enumerate(week):
                if day == 0:
                    # 空白セル
                    tk.Label(self.cal_frame, text="", width=5, height=2).grid(row=week_idx+1, column=day_idx)
                else:
                    # 過去の日付は無効化
                    disabled = (year < now.year or 
                               (year == now.year and month < now.month) or 
                               (year == now.year and month == now.month and day < current_day))
                    
                    day_button = tk.Button(
                        self.cal_frame,
                        text=str(day),
                        width=5,
                        height=2,
                        state="disabled" if disabled else "normal",
                        command=lambda y=year, m=month, d=day: self.select_date(y, m, d)
                    )
                    day_button.grid(row=week_idx+1, column=day_idx)
    
    def accommodation_button_clicked(self):
        self.reservation_data["type"] = "accommodation"
        self.show_frame("accommodation_plan_page")
    
        # プラン選択関数を変更
    def select_accommodation_plan(self, plan):
        self.reservation_data["plan"] = plan
        self.show_frame("room_selection_page")
        
    def select_date(self, year, month, day):
        date_str = f"{year}年{month}月{day}日"
        self.reservation_data["date"] = date_str
        
        # 予約データに人数情報を更新
        self.update_guests_count()
        
        messagebox.showinfo("日付選択", f"{date_str}が選択されました。人数を確認して「次へ」を押してください")
        # 自動で画面遷移しない
        # self.show_frame("options_page")
        
        # 次へボタンを追加
        next_button = tk.Button(
            self.cal_frame,
            text="次へ",
            command=lambda: self.show_frame("options_page")
        )
        next_button.grid(row=len(calendar.monthcalendar(year, month))+2, column=6)
    def calendar_back_button_clicked(self):
        if self.reservation_data["type"] == "accommodation":
            self.show_frame("accommodation_plan_page")

    
    def options_next_button_clicked(self):
        # 選択されたオプションを保存
        selected_options = []
    
        if self.reservation_data["type"] == "accommodation":
            for option in self.accommodation_options:
                if option["var"].get() == 1:
                    quantity = option["quantity_var"].get()
                    selected_options.append(f"{option['name']} ({option['price']}) - {quantity}")
        
        self.reservation_data["options"] = selected_options
        self.show_frame("personal_info_page")
    # クラス内に料金計算メソッドを追加
    def calculate_total_price(self):
        total = 0
        
        # 1. 基本料金（プランごとの料金）
        plan_prices = {
            "【朝食付き】 観光、ビジネス！一泊朝食プラン": 8500,
            "【2025ゴールデンウィーク★プレミアムプラン】前沢牛の豪華会席": 20000,
            "【スタンダード】【HP特価】八幡平産杜仲茶ポークの和食膳プラン": 14600,
            "【八幡平の地ビール・ドラゴンアイビールで乾杯】": 14600,
            "【早期割90日前予約で15%割引】岩手山牛と八幡平産杜仲茶ポーク": 13260,
            "【北投石の岩盤浴】豊かな八幡平の自然と岩盤浴でリフレッシュ": 15800,
            "【イースター復活祭】×【女子旅】": 13800,
            "【早期割60日前予約で10%割引】岩手山牛と八幡平産杜仲茶ポーク": 14040,
            "【母の日プラン】カーネーションフラワーアレンジメント": 14500,
            "【岩手県産牛】岩手県産牛と八幡平産杜仲茶ポークを味わう": 15400,
            "【1泊2章のお子様3000円！】【2025春休み】家族旅行応援": 15600,
            "【早期割90日前予約で15%割引】前沢牛・伊勢海老・あわび・ズワイガニ": 18360,
            "【前沢牛】前沢牛の網焼きとロースト握り和食膳プラン": 18400,
            "【前沢牛】前沢牛のせいろ蒸しとロースト握り和食膳プラン": 18400,
            "【赤ちゃんプラン】お子様歓迎♪パパママも嬉しい12個の特典付き": 18800,
            "【赤ちゃんプラン・お食い初め】": 18800,
            "【8/13～8/15】2025お盆期間限定♪お子様歓迎！": 19000,
            "【早期割60日前予約で10%割引】前沢牛・伊勢海老・あわび・ズワイガニ": 19440,
        }
        # 早期割引プランのリスト
        early_discount_plans = {
            "【早期割90日前予約で15%割引】岩手山牛と八幡平産杜仲茶ポーク": {"days": 90, "discount": 0.15},
            "【早期割60日前予約で10%割引】岩手山牛と八幡平産杜仲茶ポーク": {"days": 60, "discount": 0.10},
            "【早期割90日前予約で15%割引】前沢牛・伊勢海老・あわび・ズワイガニ": {"days": 90, "discount": 0.15},
            "【早期割60日前予約で10%割引】前沢牛・伊勢海老・あわび・ズワイガニ": {"days": 60, "discount": 0.10},
        }
        
        # 選択されたプランの料金を追加
        if self.reservation_data["plan"] in plan_prices:
            plan_price = plan_prices[self.reservation_data["plan"]]
            
            # 早期割引プランの場合、予約日と宿泊日の差を確認
            if self.reservation_data["plan"] in early_discount_plans:
                # 予約日（現在日）
                booking_date = datetime.datetime.now()
                
                # 宿泊日を文字列からdatetimeに変換（例："2025年4月10日" → datetime）
                try:
                    stay_date_str = self.reservation_data["date"]
                    year = int(stay_date_str.split("年")[0])
                    month = int(stay_date_str.split("年")[1].split("月")[0])
                    day = int(stay_date_str.split("月")[1].split("日")[0])
                    stay_date = datetime.datetime(year, month, day)
                    
                    # 日数差の計算
                    days_difference = (stay_date - booking_date).days
                    
                    # 必要な日数以上前に予約している場合、割引を適用
                    required_days = early_discount_plans[self.reservation_data["plan"]]["days"]
                    if days_difference >= required_days:
                        discount_rate = early_discount_plans[self.reservation_data["plan"]]["discount"]
                        plan_price = plan_price * (1 - discount_rate)
                        
                        # 割引適用メッセージをデバッグ用に出力（必要に応じて）
                        print(f"早期割引適用: {discount_rate*100}%割引")
                    else:
                        # 早期割引条件を満たしていない場合はメッセージを表示
                        messagebox.showinfo("割引条件", f"このプランは宿泊日の{required_days}日前までの予約で割引が適用されます。")
                        
                except Exception as e:
                    # 日付解析に失敗した場合は割引なし
                    print(f"日付解析エラー: {e}")
            
        # 人数分の料金計算
        total += plan_price * self.reservation_data["guests"]["adults"]
        
        # 子供料金は大人の70%と仮定
        total += (plan_price * 0.7) * self.reservation_data["guests"]["children"]
    
        # 2. 部屋タイプによる追加料金
        room_additional_fees = {
            "本館 和室7.5畳間": 0,
            "岩手山側和室10畳間": 0,
            "西館 和室10畳間": 0,
            "西館 洋室(ツイン) 禁煙": 0,
            "西館 和洋室(バリアフリー/ツイン+和室7.5畳間)": 0,
            "西館 和室28畳間": 0,
            "岩手山展望露天風呂付き和室": 2000,
            "檜の内風呂付本館和洋室": 3000,
            "別館姫神「黒倉の間」「源太の間」(温泉露天風呂付き)": 13500,
            "別館姫神「見返の間」(温泉内風呂付き)": 16500,
            "別館姫神「茶臼の間」「七時雨の間」(檜の温泉内風呂付き)": 16500,
            "別館姫神「貴賓室」(檜の温泉内風呂付き)": 21500
        }
        
        # 選択された部屋タイプの追加料金を加算
        if self.reservation_data["room"] in room_additional_fees:
            total += room_additional_fees[self.reservation_data["room"]]
        
        # 3. オプション料金
        option_prices = {
            "姫神サーモンの釜飯": 900,
            "八幡平産杜仲茶ポークのホルモン鍋": 1100,
            "岩手県産牛の串焼き": 750,
            "前沢牛の網焼きミニステーキ": 3600,
            "前沢牛のせいろ蒸し": 3600,
            "ズワイガニのしゃぶしゃぶ": 2100,
            "ラジウム岩盤浴": 1500,
            "温泉貸切風呂": 2500
        }
        
        # 選択されたオプションの料金を加算
        for option in self.reservation_data["options"]:
            # オプション名を抽出 - 例: "姫神サーモンの釜飯 (900円) - 2人前" から "姫神サーモンの釜飯" を取得
            option_name = option.split(" (")[0]
            # 数量を抽出 - 例: "- 2人前" から "2" を取得
            quantity_str = option.split("- ")[1].split("人前")[0]
            quantity = int(quantity_str)
            
            if option_name in option_prices:
                total += option_prices[option_name] * quantity
        
        return total
    def update_reservation_summary(self):
        # 総額を計算
        total_price = self.calculate_total_price()
        # 予約内容テキストを更新
        summary = f"【予約タイプ】: {'宿泊' if self.reservation_data['type'] == 'accommodation' else '宴会'}\n"
        summary += f"【プラン】: {self.reservation_data['plan']}\n"
        summary += f"【お部屋】: {self.reservation_data['room']}\n"
        summary += f"【日付】: {self.reservation_data['date']}\n"
        summary += f"【宿泊人数】: 大人 {self.reservation_data['guests']['adults']}名、子ども {self.reservation_data['guests']['children']}名\n"
        
        if self.reservation_data["options"]:
            summary += "【オプション】:\n"
            for option in self.reservation_data["options"]:
                summary += f"  • {option}\n"
        else:
            summary += "【オプション】: なし\n"
        # 料金情報を追加
        summary += f"\n【料金合計】: {total_price:,}円（税込）\n"
        # テキストウィジェットを更新
        self.summary_text.config(state="normal")
        self.summary_text.delete(1.0, tk.END)
        self.summary_text.insert(tk.END, summary)
        self.summary_text.config(state="disabled")
    
    def submit_reservation(self):
        # フォーム内容を取得
        for key, var in self.form_vars.items():
            self.reservation_data["personal_info"][key] = var.get()
        
        # 必須項目のチェック
        required_fields = ["name", "phone", "email"]
        missing_fields = [field for field in required_fields if not self.reservation_data["personal_info"].get(field)]
        
        if missing_fields:
            messagebox.showerror("入力エラー", "必須項目が入力されていません")
            return
        
        # メール送信の同意確認
        if self.agreement_var.get() != 1:
            messagebox.showerror("同意エラー", "メール送信の同意が必要です")
            return
        
        with open("宿泊.json", "w", encoding="utf-8") as f:
            json.dump(self.reservation_data, f, ensure_ascii=False, indent=4)
        # 予約確定処理
        messagebox.showinfo("予約完了", "予約が完了しました。ご入力いただいたメールアドレスに確認メールを送信しました。")
        to = self.reservation_data["personal_info"]["email"]
        subject = '予約内容のご確認'
        body = ""
        body =f"""
        予約内容の確認
        ====================

        【予約タイプ】: {'宿泊' if self.reservation_data['type'] == 'accommodation' else '宴会'}
        【プラン】: {self.reservation_data['plan']}
        【お部屋】: {self.reservation_data['room']}
        【日付】: {self.reservation_data['date']}
        【宿泊人数】: 大人 {self.reservation_data['guests']['adults']}名、子ども {self.reservation_data['guests']['children']}名

        【オプション】:
        """
        if self.reservation_data["options"]:
            for option in self.reservation_data["options"]:
                body += f"  • {option}\n"
        else:
            body += "なし\n"
        
        # 料金合計を計算して追加
        total_price = self.calculate_total_price()


        
        body += f"\n【料金合計】: {total_price:,}円（税込）\n"
        
        body += f"""
        【お客様情報】:
        お名前: {self.reservation_data['personal_info'].get('name', '')}
        フリガナ: {self.reservation_data['personal_info'].get('name_kana', '')}
        チェックイン時間: {self.reservation_data['personal_info'].get('checkin', '')}
        電話番号: {self.reservation_data['personal_info'].get('phone', '')}
        メールアドレス: {self.reservation_data['personal_info'].get('email', '')}
        住所: {self.reservation_data['personal_info'].get('address', '')}

        ====================
        ご予約ありがとうございます。ご質問等ございましたら当ホテルまでお問い合わせください。
            """
        
        
        send_mail(to, subject, body)
        
        # 予約データをリセット
        self.reservation_data = {
            "type": "",
            "plan": "",
            "date": "",
            "options": [],
            "personal_info": {}
        }
        self.window_destroy()
        
    def window_destroy(self):
        # トップページに戻る
        self.main_frame.destroy()
        from main import MainTop
        MainTop(self.root)
    
if __name__ == "__main__":
    root = tk.Tk()
    app = AccoReservationSystem(root)
    root.mainloop()