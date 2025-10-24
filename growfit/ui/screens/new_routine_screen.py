# new_routine_screen.py

from kivy.uix.screenmanager import Screen

class NewRoutineScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.build_ui()

    def build_ui(self):
        from kivy.uix.boxlayout import BoxLayout
        from kivy.uix.label import Label
        from kivy.uix.button import Button
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.add_routine_elements(layout)
        self.add_widget(layout)

    def add_routine_elements(self, layout):
        from kivy.uix.label import Label
        from kivy.uix.button import Button
        layout.add_widget(Label(text="NEW ROUTINE", font_size=40))
        layout.add_widget(Button(text="New Exercise", size_hint=(1, 0.2), on_press=self.go_to_new_exercise))
        layout.add_widget(Button(text="Back", size_hint=(1, 0.2), on_press=self.go_to_main_screen))

    def go_to_new_exercise(self, instance):
        self.manager.current = 'new_exercise'

    def go_to_main_screen(self, instance):
        self.manager.current = 'main_screen'
