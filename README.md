# Company Activities Interpretation Tool
Develop a tool to report in realtime the activities of any given company.

## How to Use
`Render.py` creates a GUI application using tkinter in python, 
which allows the user to enter the name of a company and its 
webpage URL. When the user presses the "Submit" button or the 
"Return" key, the `on_enter` function is called. The function uses 
the entered company name to perform a Google search and retrieves 
the first URL in the results. It then uses the `url_to_soup_obj` and 
`extract_text functions` from the URL_Functions module to retrieve the 
HTML content of the webpage and extract the human-readable text from 
it, respectively. This text is then passed to the `create_prompt`, 
`gen_response`, and `response_text` functions from the Analysis_LLM 
module to generate an output, which is then printed to the console. 

## `Render.py` Example Usage
![Image](/images/rm1.png)