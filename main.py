import tkinter as tk
from tkinter import messagebox

class Cuenta:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def actualizar_saldo(self):
        """Actualiza el saldo según las condiciones dadas."""
        if self.saldo < 10000.00:
            self.saldo *= (1 + 0.03)
        else:
            self.saldo *= (1 + 0.04)

    def obtener_saldo(self):
        """Devuelve el saldo actualizado."""
        return self.saldo

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora de Saldo")
        self.geometry("300x200")

        # Etiqueta y campo de entrada para el saldo inicial
        tk.Label(self, text="Dame saldo actual:").pack(pady=10)
        self.saldo_entry = tk.Entry(self)
        self.saldo_entry.pack(pady=5)

        # Botón para calcular el saldo final
        tk.Button(self, text="Calcular Saldo", command=self.calcular_saldo).pack(pady=10)

        # Etiqueta para mostrar el resultado
        self.resultado_label = tk.Label(self, text="Saldo final será mostrado aquí")
        self.resultado_label.pack(pady=10)

    def calcular_saldo(self):
        """Obtiene el saldo inicial del campo de entrada, calcula el saldo final y muestra el resultado."""
        try:
            saldo_inicial = float(self.saldo_entry.get())
            cuenta = Cuenta(saldo_inicial)
            cuenta.actualizar_saldo()
            saldo_final = cuenta.obtener_saldo()
            self.resultado_label.config(text=f"Saldo final es {saldo_final:5.2f}")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese un valor numérico válido.")

if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()
