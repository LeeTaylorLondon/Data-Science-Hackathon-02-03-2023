# Author: Lee Taylor
import tkinter as tk
import URL_Functions
import Analysis_LLM


def on_enter(event=None):
    # Get the values of the two text fields
    company_name = entry1.get()
    company_url = entry2.get()
    # Disable the text fields so they can no longer accept input
    entry1.config(state="disable")
    entry2.config(state="disable")
    # URL and .html processing and storage (for later)
    urls = URL_Functions.google_search(search_str=company_name)
    soup = URL_Functions.url_to_soup_obj(urls[0])
    text = URL_Functions.extract_text(soup, headers=False)
    # Analysis - pass .html text to LLM
    prompt_  = Analysis_LLM.create_prompt(text[1000:3000])
    # Todo: openai.error.InvalidRequestError: This model's maximum context length is 4097 tokens,
    #  however you requested 6042 tokens (4042 in your prompt; 2000 for the completion).
    #  Please reduce your prompt; or completion length.
    response = Analysis_LLM.gen_response(prompt_)
    output   = Analysis_LLM.response_text(response)
    print(output)
    # Enable the text fields
    entry1.config(state="normal")
    entry2.config(state="normal")
    # Mark EOF
    pass


if __name__ == '__main__':
    # Define window application
    root = tk.Tk()
    root.title("Blank Window")
    root.geometry("600x400")
    root.title("CAR-01")  # CAR = Companies Activities Report

    # Create text input for company name
    label1 = tk.Label(text='Company Name:')
    entry1 = tk.Entry(root, width=50)
    label1.pack()
    entry1.pack()

    # Create text input for company webpage URL
    label2 = tk.Label(text='Company WebPage URL:')
    entry2 = tk.Entry(root, width=50)
    label2.pack()
    entry2.pack()

    # Create submit button
    button = tk.Button(root, text="Submit", command=on_enter)
    button.pack()

    # Bind the `<Return>` key to the `on_enter` function
    root.bind("<Return>", on_enter)

    # Run window
    root.mainloop()
