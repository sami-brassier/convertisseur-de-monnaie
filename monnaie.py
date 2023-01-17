import tkinter as tk

def convert():
    try:
        amount = float(entry_amount.get())
        from_currency = from_var.get()
        to_currency = to_var.get()
        # taux de change fictif
        rates = {'USD': 1.0, 'EUR': 0.9, 'JPY': 105.0}
        if from_currency in rates and to_currency in rates:
            result = amount * rates[to_currency] / rates[from_currency]
            label_result.config(text=str(result))
            # sauvegarder l'historique des conversions
            history.append((amount, from_currency, to_currency, result))
        else:
            label_result.config(text="Devise non supportée")
    except ValueError:
        label_result.config(text="Valeur non valide")

def show_history():
    history_window = tk.Toplevel(root)
    history_window.title("Historique des conversions")
    for i, (amount, from_currency, to_currency, result) in enumerate(history):
        history_label = tk.Label(history_window, text=f"{i+1}. {amount} {from_currency} = {result} {to_currency}")
        history_label.pack()

root = tk.Tk()
root.title("Convertisseur de devises")

amount_frame = tk.Frame(root)
amount_frame.pack()
label_amount = tk.Label(amount_frame, text="Montant:")
label_amount.pack(side='left')
entry_amount = tk.Entry(amount_frame)
entry_amount.pack(side='left')

from_frame = tk.Frame(root)
from_frame.pack()
label_from = tk.Label(from_frame, text="De:")
label_from.pack(side='left')
from_var = tk.StringVar(value='USD')
from_dropdown = tk.OptionMenu(from_frame, from_var, 'USD', 'EUR', 'JPY')
from_dropdown.pack(side='left')

to_frame = tk.Frame(root)
to_frame.pack()
label_to = tk.Label(to_frame, text="À:")
label_to.pack(side='left')
to_var = tk.StringVar(value='EUR')
to_dropdown = tk.OptionMenu(to_frame, to_var, 'USD', 'EUR', 'JPY')
to_dropdown.pack(side='left')

convert_button = tk.Button(root, text="Convertir", command=convert)
convert_button.pack()

result_frame = tk.Frame(root)
result_frame.pack()
label_result = tk.Label(result_frame, text="")
label_result.pack()

history_button = tk.Button(root, text="Historique", command=show_history)
history_button.pack()

# historique des conversions
history = []

root.mainloop()