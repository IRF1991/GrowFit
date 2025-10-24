from kivy.uix.screenmanager import Screen

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.build_ui()

    def build_ui(self):
        from kivy.uix.boxlayout import BoxLayout
        from kivy.uix.label import Label
        from kivy.uix.button import Button
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        layout.add_widget(Label(text="HOME", font_size=40))
        layout.add_widget(Button(text="New Routine", size_hint=(1, 0.2), on_press=self.go_to_new_routine))
        self.add_widget(layout)

    def go_to_new_routine(self, instance):
        from growfit.core.data_manager import DataManager
        dm = DataManager()
        dm.create_user_if_needed()
        self.manager.current = 'new_routine'
