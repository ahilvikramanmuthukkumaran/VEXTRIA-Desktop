
import tkinter as tk
from tkinter import ttk
from system_info import get_sys_info


def main():
    root = tk.Tk()
    root.title("VEXTRIA Desktop")
    root.geometry("360x300")
    root.attributes("-topmost", True)
    root.resizable(False, False)

    title = ttk.Label(
        root,
        text="VEXTRIA",
        font=("Segoe UI", 16, "bold")
    )
    title.pack(pady=(15, 5))

    subtitle = ttk.Label(
        root,
        text="System Information",
        font=("Segoe UI", 10)
    )
    subtitle.pack(pady=5)

    info = get_sys_info()

    details = ttk.Frame(root, padding=12)
    details.pack(fill="both", expand=True)

    for key, value in info.items():
        row = ttk.Frame(details)
        row.pack(fill="x", pady=3)

        ttk.Label(
            row,
            text=f"{key}:",
            font=("Segoe UI", 9, "bold")
        ).pack(side="left")

        ttk.Label(
            row,
            text=str(value),
            font=("Segoe UI", 9),
            wraplength=210
        ).pack(side="right")

    root.mainloop()


if __name__ == "__main__":
    main()
