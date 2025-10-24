# new_exercise_screen.py

from kivy.uix.screenmanager import Screen
import growfit.core.utils as uc

class NewExerciseScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.reps_counter = 12  # Initial value for repetitions
        self.sets_counter = 0  # Initial value for sets
        self.build_ui()

    def build_ui(self):
        from kivy.uix.boxlayout import BoxLayout
        from kivy.uix.label import Label
        from kivy.uix.button import Button
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.add_exercise_elements(layout)
        self.add_widget(layout)

    def add_exercise_elements(self, layout):
        from kivy.uix.label import Label
        from kivy.uix.button import Button
        self.sets_label = Label(text=f"Sets: {self.sets_counter}", font_size=30)
        layout.add_widget(self.sets_label)
        self.reps_label = Label(text=f"Repetitions: {self.reps_counter}", font_size=30)
        layout.add_widget(self.reps_label)
        layout.add_widget(Button(text="+1 Rep", size_hint=(1, 0.3), on_press=self.increment_reps))
        layout.add_widget(Button(text="-1 Rep", size_hint=(1, 0.3), on_press=self.decrement_reps))
        layout.add_widget(Button(text="Reset Reps", size_hint=(1, 0.3), on_press=self.reset_reps))
        layout.add_widget(Button(text="+1 Set", size_hint=(1, 0.3), on_press=self.increment_sets))
        layout.add_widget(Button(text="-1 Set", size_hint=(1, 0.3), on_press=self.decrement_sets))
        layout.add_widget(Button(text="Back", size_hint=(1, 0.3), on_press=self.go_back))

    def increment_reps(self, instance):
        self.reps_counter = uc.increment_counter(self.reps_counter)
        self.reps_label.text = f"Repetitions: {self.reps_counter}"

    def decrement_reps(self, instance):
        self.reps_counter = uc.reduce_counter(self.reps_counter)
        self.reps_label.text = f"Repetitions: {self.reps_counter}"

    def reset_reps(self, instance):
        self.reps_counter = 12
        self.reps_label.text = f"Repetitions: {self.reps_counter}"

    def increment_sets(self, instance):
        self.sets_counter += 1
        self.sets_label.text = f"Sets: {self.sets_counter}"

    def decrement_sets(self, instance):
        if self.sets_counter > 0:
            self.sets_counter -= 1
        self.sets_label.text = f"Sets: {self.sets_counter}"

    def go_back(self, instance):
        self.manager.current = 'new_routine'
