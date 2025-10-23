"""
GrowFit Application

This file defines the main structure and flow of the GrowFit application using Kivy.

General Structure:
1. Screens and Navigation:
   - The application uses a ScreenManager (MyScreenManager) to manage different screens.
   - Each screen (e.g., MainScreen, NewRoutine, NewExercise) is a class inheriting from Screen and contains its own UI and logic.

2. Main Screens:
   - MainScreen: The home screen. Contains a button to navigate to the routines screen.
   - NewRoutine: Displays options related to routines, such as creating a new routine or returning to the main screen.
   - NewExercise: Manages repetitions and sets, with buttons to increment, decrement, and reset counters.

3. Modular Design:
   - Each screen has a build_ui method to construct its graphical interface.
   - Helper methods like add_routine_elements or add_exercise_elements organize visual elements (buttons, labels, etc.) to keep the code clean.

Application Flow:
1. Startup:
   - The application starts with the MyApp class, which creates a ScreenManager and adds the screens (MainScreen, NewRoutine, NewExercise).

2. Navigation:
   - Buttons on each screen call methods like go_to_new_routine or go_back to switch between screens using the ScreenManager.

3. Interaction:
   - Buttons on the screens have associated functions (e.g., incrementing repetitions or sets) that update the corresponding labels.

Key Points:
- Separation of Responsibilities:
  - Each screen has its own class and logic, making the code organized and maintainable.
- Scalability:
  - The current structure allows for adding new screens or features without affecting the rest of the code.
- Simplicity:
  - The code is designed to be easy to understand and modify, even for those new to Kivy.
"""

from growfit.core.data_manager import DataManager
import growfit.core.utils as uc

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


# General settings
reps_reset_value = 12
# Initialize DataManager and start a thread to check for testing mode and generate device_id
dm = DataManager()
dm.start_device_id_thread()

# Screen Manager class
class MyScreenManager(ScreenManager):
    """ Manages the different screens of the application """
    pass

# Main App class
class MyApp(App):
    """ Main application class """

    def build(self):
        sm = MyScreenManager()
        self.add_screens(sm)
        return sm

    def add_screens(self, sm):
        """ Add all screens to the ScreenManager """
        sm.add_widget(MainScreen(name='main_screen'))
        sm.add_widget(NewExercise(name='new_excercise'))
        sm.add_widget(NewRoutine(name='new_routine'))

# Main Screen class
class MainScreen(Screen):
    """ Main screen of the application """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.build_ui()

    def build_ui(self):
        """ Build the user interface for the main screen """
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        layout.add_widget(Label(text="HOME", font_size=40))
        layout.add_widget(Button(text="New Routine", size_hint=(1, 0.2), on_press=self.go_to_new_routine))
        self.add_widget(layout)

    def go_to_new_routine(self, instance):
        """ Navigate to the New Routine screen """
        dm.create_user_if_needed()
        self.manager.current = 'new_routine'

# New Routine Screen
class NewRoutine(Screen):
    """ Screen for creating a new routine """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.build_ui()

    def build_ui(self):
        """ Build the user interface for the new routine screen """
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.add_routine_elements(layout)
        self.add_widget(layout)

    def add_routine_elements(self, layout):
        """ Add elements to the routine screen layout """
        layout.add_widget(Label(text="NEW ROUTINE", font_size=40))
        layout.add_widget(Button(text="New Exercise", size_hint=(1, 0.2), on_press=self.go_to_new_excercise))
        layout.add_widget(Button(text="Back", size_hint=(1, 0.2), on_press=self.go_to_main_screen))

    def go_to_new_excercise(self, instance):
        """ Navigate to the New Exercise screen """
        self.manager.current = 'new_excercise'

    def go_to_main_screen(self, instance):
        """ Navigate back to the Main screen """
        self.manager.current = 'main_screen'

# New Exercise Screen
class NewExercise(Screen):
    """ Screen for managing repetitions and sets """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.reps_counter = reps_reset_value  # Initial value for repetitions
        self.sets_counter = 0  # Initial value for sets
        self.build_ui()

    def build_ui(self):
        """ Build the user interface for the new exercise screen """
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.add_exercise_elements(layout)
        self.add_widget(layout)

    def add_exercise_elements(self, layout):
        """ Add elements to the exercise screen layout """
        # Sets label
        self.sets_label = Label(text=f"Sets: {self.sets_counter}", font_size=30)
        layout.add_widget(self.sets_label)

        # Repetitions label
        self.reps_label = Label(text=f"Repetitions: {self.reps_counter}", font_size=30)
        layout.add_widget(self.reps_label)

        # Buttons for repetitions
        layout.add_widget(Button(text="+1 Rep", size_hint=(1, 0.3), on_press=self.increment_reps))
        layout.add_widget(Button(text="-1 Rep", size_hint=(1, 0.3), on_press=self.decrement_reps))
        layout.add_widget(Button(text="Reset Reps", size_hint=(1, 0.3), on_press=self.reset_reps))

        # Buttons for sets
        layout.add_widget(Button(text="+1 Set", size_hint=(1, 0.3), on_press=self.increment_sets))
        layout.add_widget(Button(text="-1 Set", size_hint=(1, 0.3), on_press=self.decrement_sets))

        # Back button
        layout.add_widget(Button(text="Back", size_hint=(1, 0.3), on_press=self.go_back))

    def increment_reps(self, instance):
        """ Increment the repetitions counter """
        self.reps_counter = uc.increment_counter(self.reps_counter)
        self.reps_label.text = f"Repetitions: {self.reps_counter}"

    def decrement_reps(self, instance):
        """ Decrement the repetitions counter """
        self.reps_counter = uc.reduce_counter(self.reps_counter)
        self.reps_label.text = f"Repetitions: {self.reps_counter}"

    def reset_reps(self, instance):
        """ Reset the repetitions counter to the default value """
        self.reps_counter = reps_reset_value
        self.reps_label.text = f"Repetitions: {self.reps_counter}"

    def increment_sets(self, instance):
        """ Increment the sets counter """
        self.sets_counter += 1
        self.sets_label.text = f"Sets: {self.sets_counter}"

    def decrement_sets(self, instance):
        """ Decrement the sets counter """
        if self.sets_counter > 0:
            self.sets_counter -= 1
        self.sets_label.text = f"Sets: {self.sets_counter}"

    def go_back(self, instance):
        """ Navigate back to the New Routine screen """
        self.manager.current = 'new_routine'

# Run the app
def run_app():
    """ Entry point to run the application """
    MyApp().run()

if __name__ == "__main__":
    run_app()