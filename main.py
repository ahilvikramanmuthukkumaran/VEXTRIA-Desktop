from datetime import datetime
import tkinter as tk
from tkinter import ttk
from system_info import get_sys_info


def main():
    root = tk.Tk()
    root.title("VEXTRIA Desktop")
    root.geometry("380x340")
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

    details = ttk.Frame(root, padding=12)
    details.pack(fill="both", expand=True)

    info_labels = {}

    def refresh_info():
        info = get_sys_info()

        for widget in details.winfo_children():
            widget.destroy()

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
                wraplength=220
            ).pack(side="right")

        current_time = datetime.now().strftime("%I:%M:%S %p")

        status_label.config(
        text=f"Last updated: {current_time}"
        )

    refresh_button = ttk.Button(
        root,
        text="Refresh",
        command=refresh_info
    )
    refresh_button.pack(pady=5)
    minimize_button = ttk.Button(
    root,
    text="Minimize",
    command=root.iconify
)

    minimize_button.pack(pady=5)

    status_label = ttk.Label(
        root,
        text="Ready",
        font=("Segoe UI", 8)
    )
    status_label.pack(pady=(0, 10))
    
    close_button = ttk.Button(
    root,
    text="Exit VEXTRIA",
    command=root.destroy
    )

    close_button.pack(pady=5)


    refresh_info()

    root.mainloop()


if __name__ == "__main__":
    main()
