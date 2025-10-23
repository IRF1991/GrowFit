from growfit.core.data_manager import DataManager
import growfit.core.utils as uc
import time

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


# General settings
reps_reset_value = 12
dm = DataManager()
# Iniciar hilo para preguntar por consola si es testing y generar device_id
dm.start_device_id_thread()

# Screen Manager class
class MyScreenManager(ScreenManager):
    pass


# Main App class
class MyApp(App):

    def build(self):
        sm = MyScreenManager()
        sm.add_widget(MainScreen(name='main_screen'))
        sm.add_widget(NewExcercise(name='new_excercise'))
        sm.add_widget(NewRoutine(name='new_routine'))
        return sm

# Main Screen class
class MainScreen(Screen):
    """ Pantalla principal de inicio """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        layout.add_widget(Label(text="INICIO", font_size=40))
        layout.add_widget(Button(text="Nueva Rutina", size_hint=(1, 0.2), on_press=self.go_to_new_routine))
        self.add_widget(layout)


    def go_to_new_routine(self, instance):
        # crea device_id si no existe
        dm.create_user_if_needed()
        # va a nueva rutina
        self.manager.current = 'new_routine'


# Nueva Rutina
class NewRoutine(Screen):
    """ Pantalla para crear una nueva rutina """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.routine(layout)
        self.add_widget(layout)

    def routine(self, layout):
        layout.add_widget(Label(text="NUEVA RUTINA", font_size=40))
        layout.add_widget(Button(text="Nuevo Ejercicio", size_hint=(1, 0.2), on_press=self.go_to_new_excercise))
        layout.add_widget(Button(text="Atrás", size_hint=(1, 0.2), on_press=self.go_to_main_screen))

    def go_to_new_excercise(self, instance):
        self.manager.current = 'new_excercise'

    def go_to_main_screen(self, instance):
        self.manager.current = 'main_screen'


# Nuevo Ejercicio
class NewExcercise(Screen):
    """ Pantalla del contador de repeticiones """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.counter = reps_reset_value  # valor inicial

        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.reps(layout)
        self.add_widget(layout)

    def sets(self, layout):
        """ Configuración de botones y etiqueta de sets """

        self.label = Label(text=f"Sets: {self.counter}", font_size=30)
        layout.add_widget(self.label)

        # Botón +1
        btn = Button(text="+1", size_hint=(1, 0.3))
        btn.bind(on_press=self.on_increment)
        layout.add_widget(btn)

        # Botón -1
        btn2 = Button(text="-1", size_hint=(1, 0.3))
        btn2.bind(on_press=self.on_decrement)
        layout.add_widget(btn2)


    def reps(self, layout):
        """ Configuración de botones y etiqueta de repeticiones """

        self.label = Label(text=f"Repeticiones: {self.counter}", font_size=30)
        layout.add_widget(self.label)

        # Botón +1
        btn = Button(text="+1", size_hint=(1, 0.3))
        btn.bind(on_press=self.on_increment)
        layout.add_widget(btn)

        # Botón -1
        btn2 = Button(text="-1", size_hint=(1, 0.3))
        btn2.bind(on_press=self.on_decrement)
        layout.add_widget(btn2)

        # Botón Reset
        btn3 = Button(text="Reset", size_hint=(1, 0.3))
        btn3.bind(on_press=self.on_reset)
        layout.add_widget(btn3)


    def on_increment(self, instance):
        self.counter = uc.increment_counter(self.counter)
        self.label.text = f"Repeticiones: {self.counter}"

    def on_decrement(self, instance):
        self.counter = uc.reduce_counter(self.counter)
        self.label.text = f"Repeticiones: {self.counter}"

    def on_reset(self, instance):
        self.counter = reps_reset_value
        self.label.text = f"Repeticiones: {self.counter}"

    def go_back(self, instance):
        self.manager.current = 'new_routine'


# Ejecutar app
def run_app():
    MyApp().run()

if __name__ == "__main__":
    run_app()