import tkinter as tk

root = tk.Tk()
root.title("Case Converter")


def convert_to_snake_case(frame, non_camel_cased_str):
    txt = [
        "_" + char.lower() if char.isupper()
        else char
        for char in non_camel_cased_str
    ]

    tk.Label(frame, text=''.join(txt).strip("_"), font=("Arial", 18)).grid(row=1, column=1, padx=10, pady=10)


def layout():
    main_frame = tk.Frame(root).grid(row=0, column=0)
    font_text = ("Arial", 18)
    font_button = ("Arial", 16)
    padding_x = 10
    padding_y = 10

    # Label
    tk.Label(main_frame, text="Enter Text: ", font=font_text).grid(row=0, column=0, padx=padding_x, pady=padding_y)
    tk.Label(main_frame, text="Snake Case: ", font=font_text).grid(row=1, column=0, padx=padding_x, pady=padding_y)

    # Entry
    entry = tk.Entry(main_frame, font=font_text, justify="center")
    entry.grid(row=0, column=1, padx=padding_x, pady=padding_y)

    # Button
    tk.Button(main_frame, command= lambda: convert_to_snake_case(main_frame, entry.get()), text="Convert", font=font_button).grid(row=2, column=1, padx=padding_x, pady=padding_y)

    root.mainloop()


def main():
    layout()


if __name__ == "__main__":
    main()