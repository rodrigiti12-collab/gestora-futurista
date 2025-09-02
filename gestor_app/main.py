from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button

class GestorApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

        # Logo
        layout.add_widget(Image(source="assets/logo.png"))

        # Funciones
        layout.add_widget(Label(text="🚀 Bienvenido a la Gestora Futurista", font_size=22))
        layout.add_widget(Button(text="📂 Gestionar Archivos"))
        layout.add_widget(Button(text="🧮 Herramientas"))
        layout.add_widget(Button(text="⚙️ Configuración"))

        return layout

if __name__ == '__main__':
    GestorApp().run()
