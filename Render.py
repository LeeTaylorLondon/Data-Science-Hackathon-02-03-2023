# Author: Lee Taylor
import tkinter as tk
import URL_Functions
import Analysis_LLM


def process_text(text_):
    # openai.error.InvalidRequestError: This model's maximum context length is 4097 tokens,
    #  however you requested 6042 tokens (4042 in your prompt; 2000 for the completion).
    #  Please reduce your prompt; or completion length.
    if len(text_) > 3000:
        text_ = text_[1000:3000]
    else:
        try:
            text_ = text_[:2000]
        except IndexError:
            pass
    return text_


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
    text = process_text(text)  # Shortens and focuses text
    prompt_  = Analysis_LLM.create_prompt(paragraphs=text,
                                          suffix='Also start your response with '
                                                 'a word classifying the company.')
    response = Analysis_LLM.gen_response(prompt_)
    output   = Analysis_LLM.response_text(response)
    print(output.strip())
    # Enable the text fields
    entry1.config(state="normal")
    # entry2.config(state="normal")
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
    entry2.config(state="disable")

    # Create submit button
    button = tk.Button(root, text="Submit", command=on_enter, width=40)
    button.pack(pady=20)

    # Bind the `<Return>` key to the `on_enter` function
    root.bind("<Return>", on_enter)

    # Run window
    root.mainloop()
