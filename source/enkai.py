import tkinter as tk
from tkinter import ttk, messagebox
import calendar
import datetime
import json
import os

class HotelReservationSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("ホテル予約システム")
        self.root.geometry("800x600")
        
        self.reservation_data = {
            "type": "",  # "accommodation" または "banquet"
            "plan": "",
            "date": "",
            "options": [],
            "discounts": [],
            "personal_info": {},
            "total_price": 0,
            "adults": 2,   
            "children": 0,  
            "number_of_people": 2
        }
        
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill="both", expand=True)
        
        self.frames = {}
        
        self.create_accommodation_plan_page()
        self.create_calendar_page()
        self.create_options_page()
        self.create_personal_info_page()
        self.create_banquet_plan_page()
        self.create_banquet_room_page()
        
        
        self.show_frame("banquet_plan_page")
        
        with open("reservation.json", "w", encoding="utf-8") as f:
            json.dump(self.reservation_data, f, ensure_ascii=False, indent=4)
    
    def create_accommodation_plan_page(self):
        frame = tk.Frame(self.main_frame)
        self.frames["accommodation_plan_page"] = frame
        
        # タイトル
        title_label = tk.Label(frame, text="宿泊プラン選択", font=("Arial", 20))
        title_label.pack(pady=30)
        
        # プランリスト
        plans_frame = tk.Frame(frame)
        plans_frame.pack(pady=20, fill="both", expand=True)
        
        # サンプルプラン
        plans = [
            {"name": "スタンダードプラン", "price": "10,000円〜", "description": "スタンダードな宿泊プランです。朝食付き。"},
            {"name": "デラックスプラン", "price": "15,000円〜", "description": "広めのお部屋で快適に過ごせます。朝食・夕食付き。"},
            {"name": "プレミアムプラン", "price": "20,000円〜", "description": "最上級のおもてなしを体験できます。オールインクルーシブ。"}
        ]
        
        for i, plan in enumerate(plans):
            plan_frame = tk.Frame(plans_frame, bd=1, relief=tk.SOLID)
            plan_frame.pack(pady=10, padx=50, fill="x")
            
            name_label = tk.Label(plan_frame, text=plan["name"], font=("Arial", 16, "bold"))
            name_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)
            
            price_label = tk.Label(plan_frame, text=plan["price"], font=("Arial", 14))
            price_label.grid(row=0, column=1, sticky="e", padx=10)
            
            desc_label = tk.Label(plan_frame, text=plan["description"], font=("Arial", 12))
            desc_label.grid(row=1, column=0, columnspan=2, sticky="w", padx=10, pady=5)
            
            select_button = tk.Button(
                plan_frame, 
                text="選択", 
                command=lambda p=plan["name"]: self.select_accommodation_plan(p)
            )
            select_button.grid(row=2, column=1, sticky="e", padx=10, pady=5)
        
        back_button = tk.Button(
            frame, 
            text="戻る", 
            command=lambda: self.show_frame("top_page")
        )
        back_button.pack(side="left", padx=20, pady=20)
    
    def create_banquet_plan_page(self):
        frame = tk.Frame(self.main_frame)
        self.frames["banquet_plan_page"] = frame
        
        # タイトル
        title_label = tk.Label(frame, text="宴会プラン選択", font=("Arial", 20))
        title_label.pack(pady=30)
        
        # プランリスト
        plans_frame = tk.Frame(frame)
        plans_frame.pack(pady=20, fill="both", expand=True)
        
        # サンプルプラン
        plans = [
            {"name": "豪華(ごうか)コース", "price": "21,600円/人", "description": "前沢牛、伊勢海老、あわび、ズワイガニなどを使用した豪華な和食膳。大切な方と語らいながらちょっと贅沢なひとときを。"},
            {"name": "雅(みやび)コース", "price": "18,600円/人", "description": "岩手が誇るブランド前沢牛のせいろ蒸しとローストの握り、旬の野菜など地産の食材をふんだんに使用した和食膳をお楽しみください。"},
            {"name": "錦(にしき)コース", "price": "15,600円/人", "description": "岩手県産牛と八幡平市産杜仲茶ポークの２色せいろ蒸しがメインの和食膳です。素材の旨味と季節感を味わえる料理長自慢の創作料理です。"},
            {"name": "椿(つばき)コース", "price": "12,600円/人", "description": "柔らかく甘みが特徴のブランド豚「八幡平市産杜仲茶ポーク」を、しゃぶしゃぶにて出しポン酢でお召し上がりください。"}

        ]
        
        for i, plan in enumerate(plans):
            plan_frame = tk.Frame(plans_frame, bd=1, relief=tk.SOLID)
            plan_frame.pack(pady=10, padx=50, fill="x")
            
            name_label = tk.Label(plan_frame, text=plan["name"], font=("Arial", 16, "bold"))
            name_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)
            
            price_label = tk.Label(plan_frame, text=plan["price"], font=("Arial", 14))
            price_label.grid(row=0, column=1, sticky="e", padx=10)
            
            desc_label = tk.Label(plan_frame, text=plan["description"], font=("Arial", 12))
            desc_label.grid(row=1, column=0, columnspan=2, sticky="w", padx=10, pady=5)
            
            select_button = tk.Button(
                plan_frame, 
                text="選択", 
                command=lambda p=plan["name"]: self.select_banquet_plan(p)
            )
            select_button.grid(row=2, column=1, sticky="e", padx=10, pady=5)
        
        # 戻るボタン
        back_button = tk.Button(
            frame, 
            text="戻る", 
            command=lambda: self.show_frame("top_page")
        )
        back_button.pack(side="left", padx=20, pady=20)
        
        
    # 部屋選択画面の作成メソッド
    def create_banquet_room_page(self):
        frame = tk.Frame(self.main_frame)
        self.frames["banquet_room_page"] = frame
    
    # タイトル
        title_label = tk.Label(frame, text="宴会会場選択", font=("Arial", 20))
        title_label.pack(pady=30)
    
    # 会場リスト
        rooms_frame = tk.Frame(frame)
        rooms_frame.pack(pady=20, fill="both", expand=True)
    
    # サンプル会場
        rooms = [
            {"name": "岩手山展望露天風呂付き和室", "capacity": "20,400円", "description": "檜造りの専用露天風呂から望む岩手山の雄大な姿はこのお部屋ならではの景色です。", "image": "sakura.png"},
            {"name": "檜の内風呂付本館和洋室", "capacity": "21,400円", "description": "和室と、寝室用のベッドルームを備えた和洋室", "image": "diamond.png"},
            {"name": "岩手山側和室10畳間", "capacity": "18,400円", "description": "岩手山側の中庭が目の前に広がる開放感溢れる景色のお部屋です", "image": "pearl.png"},
            {"name": "本館　和室7.5畳間", "capacity": "18,400円", "description": "和室7.5畳のお部屋", "image": "starlight.png"}
        ]
    
        for i, room in enumerate(rooms):
            room_frame = tk.Frame(rooms_frame, bd=1, relief=tk.SOLID)
            room_frame.pack(pady=10, padx=50, fill="x")
        
            name_label = tk.Label(room_frame, text=room["name"], font=("Arial", 16, "bold"))
            name_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)
        
            capacity_label = tk.Label(room_frame, text=room["capacity"], font=("Arial", 14))
            capacity_label.grid(row=0, column=1, sticky="e", padx=10)
        
            desc_label = tk.Label(room_frame, text=room["description"], font=("Arial", 12))
            desc_label.grid(row=1, column=0, columnspan=2, sticky="w", padx=10, pady=5)
        
            select_button = tk.Button(
                room_frame, 
                text="選択", 
                command=lambda r=room["name"]: self.select_banquet_room(r)
                )
            select_button.grid(row=2, column=1, sticky="e", padx=10, pady=5)
    
    # 戻るボタン
        back_button = tk.Button(
            frame, 
            text="戻る", 
            command=lambda: self.show_frame("banquet_plan_page")
            )
        back_button.pack(side="left", padx=20, pady=20)

# 宴会プラン選択後に部屋選択画面に遷移するメソッド
    def select_banquet_plan(self, plan):
        self.reservation_data["plan"] = plan
        self.show_frame("banquet_room_page")  # カレンダーの前に部屋選択へ

# 部屋を選択した後にカレンダー画面に遷移するメソッド
    def select_banquet_room(self, room):
        self.reservation_data["room"] = room
        self.show_frame("calendar_page")

# calendar_back_button_clickedメソッドも更新
    def calendar_back_button_clicked(self):
        if self.reservation_data["type"] == "accommodation":
            self.show_frame("accommodation_plan_page")
        else:
            self.show_frame("banquet_room_page")  
            # 宴会の場合は部屋選択画面に戻る

# 予約内容のサマリー更新メソッドも修正
    def update_reservation_summary(self):
    # 既存のコード...
        summary = f"【予約タイプ】: {'宿泊' if self.reservation_data['type'] == 'accommodation' else '宴会'}\n"
        summary += f"【プラン】: {self.reservation_data['plan']}\n"
    
    # 宴会の場合は会場情報を追加
        if self.reservation_data["type"] == "banquet" and self.reservation_data["room"]:
            summary += f"【会場】: {self.reservation_data['room']}\n"
    
        summary += f"【日付】: {self.reservation_data['date']}\n"    
        
    
    def create_calendar_page(self):
        frame = tk.Frame(self.main_frame)
        self.frames["calendar_page"] = frame
        
        # タイトル
        title_label = tk.Label(frame, text="予約日選択", font=("Arial", 20))
        title_label.pack(pady=20)
        
        # カレンダーフレーム
        calendar_frame = tk.Frame(frame)
        calendar_frame.pack(pady=20)
        
        # 月選択
        now = datetime.datetime.now()
        months_frame = tk.Frame(calendar_frame)
        months_frame.pack(pady=10)
        
        tk.Label(months_frame, text="年月:", font=("Arial", 12)).grid(row=0, column=0)
        
        self.year_var = tk.StringVar(value=str(now.year))
        year_combo = ttk.Combobox(months_frame, textvariable=self.year_var, values=[str(now.year + i) for i in range(3)], width=6)
        year_combo.grid(row=0, column=1, padx=5)
        
        self.month_var = tk.StringVar(value=str(now.month))
        month_combo = ttk.Combobox(months_frame, textvariable=self.month_var, values=[str(i) for i in range(1, 13)], width=4)
        month_combo.grid(row=0, column=2, padx=5)
        
        update_button = tk.Button(months_frame, text="更新", command=self.update_calendar)
        update_button.grid(row=0, column=3, padx=10)
        
        # カレンダー表示エリア
        self.cal_frame = tk.Frame(calendar_frame)
        self.cal_frame.pack(pady=10)
        
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
        
        title_label = tk.Label(frame, text="オプションと割引選択", font=("Arial", 20))
        title_label.pack(pady=20)
        
        options_frame = tk.Frame(frame)
        options_frame.pack(pady=10, fill="both", expand=True)
        
        self.accommodation_options_frame = tk.Frame(options_frame)
        tk.Label(self.accommodation_options_frame, text="宿泊オプション", font=("Arial", 16)).pack(anchor="w", padx=50, pady=10)
        
        self.accommodation_options = [
            {"name": "朝食アップグレード", "price": "2,000円", "var": tk.IntVar()},
            {"name": "夕食アップグレード", "price": "3,000円", "var": tk.IntVar()},
            {"name": "スパ利用券", "price": "5,000円", "var": tk.IntVar()},
            {"name": "レイトチェックアウト", "price": "3,000円", "var": tk.IntVar()}
        ]
        
        for option in self.accommodation_options:
            option_frame = tk.Frame(self.accommodation_options_frame)
            option_frame.pack(fill="x", padx=50, pady=5)
            
            tk.Checkbutton(option_frame, variable=option["var"], text=f"{option['name']} ({option['price']})").pack(side="left")
        
        # 宴会オプション
        self.banquet_options_frame = tk.Frame(options_frame)
        tk.Label(self.banquet_options_frame, text="宴会オプション", font=("Arial", 16)).pack(anchor="w", padx=50, pady=10)
        
        self.banquet_options = [
            {"name": "姫神サーモンの釜飯", "price": "700円", "var": tk.IntVar(), "servings": "1人前"},
            {"name": "八幡平牛ロースのしゃぶしゃぶ", "price": "4,000円", "var": tk.IntVar()},
            {"name": "大更ホルモン鍋", "price": "1,100円", "var": tk.IntVar()},
            {"name": "前沢牛の網焼きミニステーキ", "price": "3,800円", "var": tk.IntVar()},
            {"name": "岩手県産牛の串焼き", "price": "750円", "var": tk.IntVar()},
            {"name": "前沢牛のせいろ蒸し", "price": "3,600円", "var": tk.IntVar()},
            {"name": "ズワイガニのしゃぶしゃぶ", "price": "2,100円", "var": tk.IntVar()},
            {"name": "飲ん兵衛コース。プラス2,800円(税込)で2時間飲み放題！", "price": "2,800円", "var": tk.IntVar()},
        ]
        
        for option in self.banquet_options:
            option_frame = tk.Frame(self.banquet_options_frame)
            option_frame.pack(fill="x", padx=50, pady=5)
            
            tk.Checkbutton(option_frame, variable=option["var"], text=f"{option['name']} ({option['price']})").pack(side="left")
        
        # 割引セクション追加
        discount_section = tk.LabelFrame(frame, text="割引選択", font=("Arial", 16))
        discount_section.pack(pady=10, padx=50, fill="x")
        
        # 宿泊割引
        self.accommodation_discount_frame = tk.Frame(discount_section)
        self.accommodation_discounts = [
            {"name": "シーズンオフ割引", "discount": "10%オフ", "var": tk.IntVar()},
            {"name": "連泊割引（3泊以上）", "discount": "15%オフ", "var": tk.IntVar()},
            {"name": "会員特典", "discount": "2,000円引き", "var": tk.IntVar()},
            {"name": "早期予約割引", "discount": "5%オフ", "var": tk.IntVar()}
        ]
        
        for discount in self.accommodation_discounts:
            discount_frame = tk.Frame(self.accommodation_discount_frame)
            discount_frame.pack(fill="x", pady=5)
            
            tk.Checkbutton(
                discount_frame, 
                variable=discount["var"], 
                text=f"{discount['name']} ({discount['discount']})"
            ).pack(side="left")
        
        # 宴会割引
        self.banquet_discount_frame = tk.Frame(discount_section)
        self.banquet_discounts = [
            {"name": "早期割90日までご予約で15％割引", "discount": "15%オフ", "var": tk.IntVar()},
            {"name": "早期割60日までご予約で10％割引", "discount": "10%オフ", "var": tk.IntVar()},
        ]
        
        for discount in self.banquet_discounts:
            discount_frame = tk.Frame(self.banquet_discount_frame)
            discount_frame.pack(fill="x", pady=5)
            
            tk.Checkbutton(
                discount_frame, 
                variable=discount["var"], 
                text=f"{discount['name']} ({discount['discount']})"
            ).pack(side="left")
        
        # 割引クーポンコード入力
        coupon_frame = tk.Frame(discount_section)
        coupon_frame.pack(fill="x", pady=10)
        
        tk.Label(coupon_frame, text="クーポンコード：").pack(side="left", padx=5)
        self.coupon_var = tk.StringVar()
        coupon_entry = tk.Entry(coupon_frame, textvariable=self.coupon_var, width=20)
        coupon_entry.pack(side="left", padx=5)
        
        validate_button = tk.Button(
            coupon_frame, 
            text="確認", 
            command=self.validate_coupon
        )
        validate_button.pack(side="left", padx=5)
        
        # 割引適用状況表示
        self.discount_status_var = tk.StringVar(value="割引は選択されていません")
        discount_status = tk.Label(discount_section, textvariable=self.discount_status_var, fg="blue")
        discount_status.pack(pady=10)
        
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
        title_label.pack(pady=20)
    
    # 2段レイアウト用のメインコンテンツフレーム
        main_content = tk.Frame(frame)
        main_content.pack(fill="both", expand=True, padx=20)
    
    # 左側：入力フォーム
        form_frame = tk.Frame(main_content)
        form_frame.pack(side="left", fill="both", expand=True, padx=10)
    
    # 入力フィールド
        fields = [
            {"label": "お名前", "var": "name"},
            {"label": "フリガナ", "var": "name_kana"},
            {"label": "チェックイン時間", "var": "check_in_time"},
            {"label": "電話番号", "var": "phone"},
            {"label": "メールアドレス", "var": "email"},
            {"label": "住所", "var": "address"},
            ]
    
        self.form_vars = {}
    
        for i, field in enumerate(fields):
            field_frame = tk.Frame(form_frame)
            field_frame.pack(fill="x", pady=3)
        
            tk.Label(field_frame, text=field["label"], width=15, anchor="e").pack(side="left", padx=5)
        
            self.form_vars[field["var"]] = tk.StringVar()
            entry = tk.Entry(field_frame, textvariable=self.form_vars[field["var"]], width=30)
            entry.pack(side="left", padx=5)
    
    # 人数入力部分（大人・子供別）
        people_frame = tk.LabelFrame(form_frame, text="宿泊人数", padx=10, pady=5)
        people_frame.pack(fill="x", pady=5)
    
    # 大人人数
        adult_frame = tk.Frame(people_frame)
        adult_frame.pack(fill="x", pady=2)
    
        tk.Label(adult_frame, text="大人 (12歳以上):", width=15, anchor="e").pack(side="left", padx=5)
    
        self.form_vars["adults"] = tk.StringVar(value=str(self.reservation_data["adults"]))
        adult_spinbox = tk.Spinbox(adult_frame, from_=1, to=10, textvariable=self.form_vars["adults"], width=5)
        adult_spinbox.pack(side="left", padx=5)
        self.form_vars["adults"].trace_add("write", self.on_people_count_change)
    
    # 子供人数
        child_frame = tk.Frame(people_frame)
        child_frame.pack(fill="x", pady=2)
    
        tk.Label(child_frame, text="子供 (12歳未満):", width=15, anchor="e").pack(side="left", padx=5)
    
        self.form_vars["children"] = tk.StringVar(value=str(self.reservation_data["children"]))
        child_spinbox = tk.Spinbox(child_frame, from_=0, to=10, textvariable=self.form_vars["children"], width=5)
        child_spinbox.pack(side="left", padx=5)
        self.form_vars["children"].trace_add("write", self.on_people_count_change)
    
    # 右側：予約内容サマリー
        summary_frame = tk.LabelFrame(main_content, text="予約内容", font=("Arial", 12))
        summary_frame.pack(side="right", fill="both", expand=True, padx=10)
    
    # サマリーテキストのサイズを大きくする
        self.summary_text = tk.Text(summary_frame, height=18, width=50, state="disabled")
        self.summary_text.pack(pady=10, padx=10, fill="both", expand=True)
    
    # メール送信の同意
        agreement_frame = tk.Frame(frame)
        agreement_frame.pack(pady=5)
    
        self.agreement_var = tk.IntVar()
        agreement_check = tk.Checkbutton(
            agreement_frame, 
            text="予約内容をメールで送信することに同意します", 
            variable=self.agreement_var
        )
        agreement_check.pack()
    
    # ボタンフレーム
        button_frame = tk.Frame(frame)
        button_frame.pack(side="bottom", fill="x", pady=10)
    
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

# 人数変更時のコールバック関数
    def on_people_count_change(self, *args):
        try:
            adults = int(self.form_vars["adults"].get())
            children = int(self.form_vars["children"].get())
        
        # 値を設定
            self.reservation_data["adults"] = adults
            self.reservation_data["children"] = children
            self.reservation_data["number_of_people"] = adults + children
        
        # 料金更新
            self.update_total_price()
        except ValueError:
        # 数値以外の入力の場合はデフォルト値に設定
            self.form_vars["adults"].set("2")
            self.form_vars["children"].set("0")
            self.reservation_data["adults"] = 2
            self.reservation_data["children"] = 0
            self.reservation_data["number_of_people"] = 2
            self.update_total_price()

    
    def show_frame(self, frame_name):
        # すべてのフレームを非表示
        for frame in self.frames.values():
            frame.pack_forget()
        
        # 指定したフレームを表示
        self.frames[frame_name].pack(fill="both", expand=True)
        
        # オプション画面の場合、予約タイプに応じたオプションと割引を表示
        if frame_name == "options_page":
            if self.reservation_data["type"] == "accommodation":
                self.banquet_options_frame.pack_forget()
                self.banquet_discount_frame.pack_forget()
                self.accommodation_options_frame.pack(fill="both", expand=True)
                self.accommodation_discount_frame.pack(fill="both", expand=True)
            else:
                self.accommodation_options_frame.pack_forget()
                self.accommodation_discount_frame.pack_forget()
                self.banquet_options_frame.pack(fill="both", expand=True)
                self.banquet_discount_frame.pack(fill="both", expand=True)
        
        # 個人情報画面の場合、予約内容を表示
        if frame_name == "personal_info_page":
            self.update_reservation_summary()
    
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
    
    def banquet_button_clicked(self):
        self.reservation_data["type"] = "banquet"
        self.show_frame("banquet_plan_page")
    
    def select_accommodation_plan(self, plan):
        self.reservation_data["plan"] = plan
        self.show_frame("calendar_page")
    
    
    def select_date(self, year, month, day):
        date_str = f"{year}年{month}月{day}日"
        self.reservation_data["date"] = date_str
        messagebox.showinfo("日付選択", f"{date_str}が選択されました")
        self.show_frame("options_page")
    
    def calendar_back_button_clicked(self):
        if self.reservation_data["type"] == "accommodation":
            self.show_frame("accommodation_plan_page")
        else:
            self.show_frame("banquet_plan_page")
    
    def validate_coupon(self):
        coupon_code = self.coupon_var.get()
        # サンプルのクーポンコード検証
        valid_coupons = {
            "WELCOME10": "10%オフ",
            "SUMMER20": "20%オフ",
            "SPECIAL5000": "5,000円引き"
        }
        
        if coupon_code in valid_coupons:
            discount = valid_coupons[coupon_code]
            self.discount_status_var.set(f"クーポン '{coupon_code}' が適用されました: {discount}")
            return True
        else:
            self.discount_status_var.set("無効なクーポンコードです")
            return False
    
    def options_next_button_clicked(self):
        # 選択されたオプションを保存
        selected_options = []
        selected_discounts = []
        
        self.reservation_data["options"] = selected_options
        self.reservation_data["discounts"] = selected_discounts
    
    # 料金計算を初期化
        self.update_total_price()
    
        self.show_frame("personal_info_page")
        
        if self.reservation_data["type"] == "accommodation":
            # オプション
            for option in self.accommodation_options:
                if option["var"].get() == 1:
                    selected_options.append(f"{option['name']} ({option['price']})")
            
            # 割引
            for discount in self.accommodation_discounts:
                if discount["var"].get() == 1:
                    selected_discounts.append(f"{discount['name']} ({discount['discount']})")
        else:
            # オプション
            for option in self.banquet_options:
                if option["var"].get() == 1:
                    selected_options.append(f"{option['name']} ({option['price']})")
            
            # 割引
            for discount in self.banquet_discounts:
                if discount["var"].get() == 1:
                    selected_discounts.append(f"{discount['name']} ({discount['discount']})")

        coupon_code = self.coupon_var.get()
        if coupon_code and self.validate_coupon():
            valid_coupons = {
                "WELCOME10": "10%オフ",
                "SUMMER20": "20%オフ",
                "SPECIAL5000": "5,000円引き"
            }
            selected_discounts.append(f"クーポン '{coupon_code}' ({valid_coupons[coupon_code]})")
        
        self.reservation_data["options"] = selected_options
        self.reservation_data["discounts"] = selected_discounts
        self.show_frame("personal_info_page")
        
    def update_total_price(self):
        base_price = 0
        
    
    # 宿泊プランの基本料金
        accommodation_prices = {
            "スタンダードプラン": 10000,
            "デラックスプラン": 15000,
            "プレミアムプラン": 20000
        }
    
    # 宴会プランの一人当たり料金
        banquet_prices = {
            "豪華(ごうか)コース": 21600,
            "雅(みやび)コース": 18600,
            "錦(にしき)コース": 15600,
            "椿(つばき)コース": 12600
        }
    
    # 人数を取得
        try:
            adults = int(self.form_vars.get("adults", "2").get())
            children = int(self.form_vars.get("children", "0").get())
            self.reservation_data["adults"] = adults
            self.reservation_data["children"] = children
            self.reservation_data["number_of_people"] = adults + children
        except ValueError:
            adults = 2
            children = 0
            
        plan = self.reservation_data["plan"]    
        
        if self.reservation_data["type"] == "accommodation":
        # 宿泊の場合
            if plan in accommodation_prices:
            # 基本料金は大人一人の料金×大人の人数、子供は70%計算
                adult_price = accommodation_prices[plan] * adults
                child_price = int(accommodation_prices[plan] * 0.7) * children
                base_price = adult_price + child_price
        else:




        # 宴会の場合
            if plan in banquet_prices:
            # 大人は通常料金、子供は50%料金として計算
                adult_price = banquet_prices[plan] * adults
                child_price = int(banquet_prices[plan] * 0.5) * children
                base_price = adult_price + child_price
        
        # オプション料金を追加（一部は人数分）
            for option in self.reservation_data.get("options", []):
                price_str = option.split("(")[1].split(")")[0].replace("円", "").replace(",", "")
                try:
                    option_price = int(price_str)
                # 飲み放題などの一人当たりオプションは人数分
                    if "飲み放題" in option:
                        base_price += option_price * (adults + children)
                    else:
                        base_price += option_price
                except ValueError:
                    pass
    
    # 割引を適用
        for discount in self.reservation_data.get("discounts", []):
            if "%" in discount:
            # 割合での割引
                percentage = int(discount.split("%")[0].split("(")[1].strip())
                base_price = base_price * (1 - percentage / 100)
            elif "円引き" in discount or "円オフ" in discount:
            # 固定額の割引
                amount = int(discount.split("円")[0].split("(")[1].strip().replace(",", ""))
                base_price = max(0, base_price - amount)
    
    # 合計金額を更新
        self.reservation_data["total_price"] = int(base_price)
    
    # 予約サマリーを更新
        if hasattr(self, 'summary_text'):
            self.update_reservation_summary()
    
    def update_reservation_summary(self):
        summary = f"【予約タイプ】: {'宿泊' if self.reservation_data['type'] == 'accommodation' else '宴会'}\n"
        summary += f"【プラン】: {self.reservation_data['plan']}\n"
    
    # 宴会の場合は会場情報を追加
        if self.reservation_data["type"] == "banquet" and "room" in self.reservation_data:
           summary += f"【会場】: {self.reservation_data['room']}\n"

        summary += f"【日付】: {self.reservation_data['date']}\n"
    
    # 人数と合計金額を追加
        adults = self.reservation_data.get("adults", 2)
        children = self.reservation_data.get("children", 0)
        total_price = self.reservation_data.get("total_price", 0)
    
        if self.reservation_data["type"] == "accommodation":
            summary += f"【宿泊人数】: 大人 {adults}人、子供 {children}人\n"
        else:
            summary += f"【宴会人数】: 大人 {adults}人、子供 {children}人\n"
    
        summary += f"【合計金額】: {total_price:,}円\n"
    
        if self.reservation_data["options"]:
            summary += "【オプション】:\n"
            for option in self.reservation_data["options"]:
                summary += f"  • {option}\n"
        else:
            summary += "【オプション】: なし\n"
    
        if self.reservation_data["discounts"]:
            summary += "【適用割引】:\n"
            for discount in self.reservation_data["discounts"]:
                summary += f"  • {discount}\n"
        else:
            summary += "【適用割引】: なし\n"
    
        self.summary_text.config(state="normal")
        self.summary_text.delete(1.0, tk.END)
        self.summary_text.insert(tk.END, summary)
        self.summary_text.config(state="disabled")
    
    def submit_reservation(self):
        for key, var in self.form_vars.items():
            self.reservation_data["personal_info"][key] = var.get()
        
        required_fields = ["name", "phone", "email"]
        missing_fields = [field for field in required_fields if not self.reservation_data["personal_info"].get(field)]
        
        if missing_fields:
            messagebox.showerror("入力エラー", "必須項目が入力されていません")
            return
        
        if self.agreement_var.get() != 1:
            messagebox.showerror("同意エラー", "メール送信の同意が必要です")
            return
        
        import json
        with open("reservation.json", "w", encoding="utf-8") as f:
            json.dump(self.reservation_data, f, ensure_ascii=False, indent=4)
        
        
        messagebox.showinfo("予約完了", "予約が完了しました。ご入力いただいたメールアドレスに確認メールを送信しました。")
        
        try:
            import smtplib
            from email.mime.text import MIMEText
            from email.mime.multipart import MIMEMultipart
            from email.header import Header
    
    # メール設定（実際の環境に合わせて変更してください）
            sender_email = "y.furudate.sys24@morijyobi.ac.jp"
            PASSWORD=os.environ['MAIL_PASS']  # 実際のアプリではセキュリティ対策が必要
            smtp_server = "smtp.gmail.com"
            smtp_port = 587
    
    # 受信者のメールアドレス
            recipient_email = self.reservation_data["personal_info"]["email"]
    
    # メールの作成
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = recipient_email
            msg['Subject'] = Header(f"【予約確認】{self.reservation_data['type']}のご予約ありがとうございます", 'utf-8')
    
    # メール本文
            body = f"""
        {self.reservation_data['personal_info'].get('name', '')} 様

        この度は、当ホテルをご予約いただき誠にありがとうございます。
        以下の内容でご予約を承りましたのでご確認ください。

        ======== ご予約内容 ========
        【予約タイプ】: {'宿泊' if self.reservation_data['type'] == 'accommodation' else '宴会'}
        【プラン】: {self.reservation_data['plan']}
        """
        
        # 宴会の場合は会場情報を追加
            if self.reservation_data["type"] == "banquet" and "room" in self.reservation_data:
                body += f"【会場】: {self.reservation_data['room']}\n"
        
            body += f"""【日付】: {self.reservation_data['date']}
        【人数】: 大人 {self.reservation_data['adults']}人、子供 {self.reservation_data['children']}人
        【合計金額】: {self.reservation_data['total_price']:,}円
        """
        
            if self.reservation_data["options"]:
                body += "【オプション】:\n"
                for option in self.reservation_data["options"]:
                    body += f"  • {option}\n"
            else:
                body += "【オプション】: なし\n"
        
            if self.reservation_data["discounts"]:
                body += "【適用割引】:\n"
                for discount in self.reservation_data["discounts"]:
                    body += f"  • {discount}\n"
            else:
                body += "【適用割引】: なし\n"
        
            body += """
        ===========================

        ご予約に関するお問い合わせは、こちらのメールにご返信いただくか、
        お電話（XXX-XXX-XXXX）にてお気軽にお問い合わせください。

        ご来館を心よりお待ちしております。

        ---------------------------
        ホテル〇〇〇〇
        〒XXX-XXXX
        ○○県○○市○○町1-2-3
        TEL: XXX-XXX-XXXX
        Email: hotel@example.com
        ---------------------------
        """
        
        # メール本文をUTF-8で設定
            msg.attach(MIMEText(body, 'plain', 'utf-8'))
        
        # SMTPサーバーに接続してメール送信
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()  # TLS暗号化
                server.login(sender_email, PASSWORD)
                server.send_message(msg)
        
            print(f"予約確認メールを {recipient_email} に送信しました")
        except Exception as e:
            print(f"メール送信エラー: {e}")
            messagebox.showwarning("メール送信エラー", "予約は完了しましたが、確認メールの送信に失敗しました。")
        
        self.reservation_data = {
            "type": "",
            "plan": "",
            "date": "",
            "options": [],
            "discounts": [],
            "personal_info": {},
            "total_price": 0,
            "adults": 2,        
            "children": 0,      
            "number_of_people": 2
            }
    
        self.window_destroy()
        
    def window_destroy(self):
        # トップページに戻る
        self.main_frame.destroy()
        from main import MainTop
        MainTop(self.root)
        
if __name__ == "__main__":
    root = tk.Tk()
    app = HotelReservationSystem(root)
    root.mainloop()