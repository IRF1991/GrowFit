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
from kivy.uix.screenmanager import ScreenManager
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window

# Import screens from the new modular structure
from growfit.ui.screens.main_screen import MainScreen
from growfit.ui.screens.new_exercise_screen import NewExerciseScreen
from growfit.ui.screens.new_routine_screen import NewRoutineScreen


# General settings
reps_reset_value = 12
# Initialize DataManager and start a thread to check for testing mode and generate device_id
dm = DataManager()
dm.start_device_id_thread()

class MyScreenManager(ScreenManager):
    """ Manages the different screens of the application """
    pass

class MyApp(App):
    """ Main application class """

    def build(self):
        sm = MyScreenManager()
        # Set a dark purple dynamic background color

        with sm.canvas.before:
            self.bg_color = Color(0.2, 0.0, 0.4, 1)  # Dark purple
            self.bg_rect = Rectangle(size=Window.size, pos=(0, 0))
            
        Window.bind(size=self.update_background)

        self.add_screens(sm)
        return sm

    def update_background(self, *args):
        """Update the background size and position dynamically."""
        self.bg_rect.size = Window.size
        self.bg_rect.pos = (0, 0)

    def add_screens(self, sm):
        """ Add all screens to the ScreenManager """
        sm.add_widget(MainScreen(name='main_screen'))
        sm.add_widget(NewExerciseScreen(name='new_exercise'))
        sm.add_widget(NewRoutineScreen(name='new_routine'))

# Run the app
def run_app():
    """ Entry point to run the application """
    MyApp().run()

if __name__ == "__main__":
    run_app()