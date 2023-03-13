# Company Activities Interpretation Tool
**Objective:** Develop a tool to report in realtime the activities of any given company.

### Approach

Firstly the `URL_Functions` module is used to perform a Google search using 
the `company_name` as the search string. It obtains the first URL from 
the search results, converts it into a soup object, and extracts the text 
content of the URL.

The `extract_text` function is a web scraping function that takes in a 
`soup` object, which is generated from an HTML page, and a boolean value 
`headers`, which determines whether or not to include headers in the 
extracted text. The function first finds all HTML elements that contain 
the main content of the page, depending on the value of `headers` 
the elements could be `p`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `a`, 
`li`, `span`, `strong`, and `em` elements. Then, it concatenates the
text from all these content elements and removes non-human friendly 
empty spaces, and sentences with keywords such as "site", "cookie", 
"sign in", "instagram", and "contact us". Finally, it removes any 
code elements and returns the resulting text as a string.

The extracted text is then passed to the `process_text` function,
which processes the text to shorten and focus it. This processed 
text is then passed to the `Analysis_LLM` module to create a prompt 
for OpenAI's language model. The language model is then used to 
generate a response based on the prompt. The generated response 
is then processed by the `response_text` function to obtain the 
final output.

## How to Use - Realtime Report
1. Create a python file called `api_key.py` add a string: 
```python
API_KEY = '<YOUR API KEY HERE>'
```
2. Generate an OpenAI key [here](https://platform.openai.com/account/api-keys).
3. Execute `main.py` or `Render.py` 
4. Input a company name into the 'Company Name:' field

## `Render.py` Example Usage
![Image](/images/rm1.png)  
1. The user inputs a company name
2. The first google result is parsed for human friendly readable text
3. This text and the objective is passed to [OpenAIs LLM text-davinci-003](https://platform.openai.com/docs/guides/completion) as a prompt
4. A bullet point list of activities conducted by the company is outputted

## Dataset & Data Collection
The 'elevate' website is a platform that contains information about 711 startups. 
I scraped the website, downloaded the HTML files for each startup, 
and extracted human-friendly readable text from these HTML files.

Please note these datasets and `Render.py` are not integrated together.  
`Render.py` could accept a directory to a text file for scraped text. (Not implemented as of yet)

* The dataset storing `.html` files can be found [here](/Greek%20Startups/Excel%20Files%20&%20Processing/soup_objects).  
* The dataset storing the **'human-friendly-readable'** text can be found [here](/Greek%20Startups/Excel%20Files%20&%20Processing/soup_to_text).

## Suggested Improvements
* Implement different NLP techniques to generate the desired output (such as POS-tagging with grammatical rules, ...)
* Improve the `Render.py` web crawler to not take the first Google result but instead all results
  on the first page then scrape all of them for relevance to the company (as the first result may not 
  be the company's website).
* From a list of 711 startups only ~480 were scraped, to improve this scrape all 711.
* For analysis, generate multiple reports from the same text then combine them all and remove duplicates.
* Build an intelligent web crawler to locate and scrape data from their social medias (such as 
  Instagram, Facebook, LinkedIn, ...).
* Add more input fields to the `Render.py` to dynamically add to the prompt to refine the output.
* For data collection create an **interactive data visualization** component(s).
* Project code and files could be reorganised.

## Requirements
To run the project the following libraries are required please run the following command below to install each package.
```commandline
pip install PACKAGE_NAME
```
* os
* openai
* pandas 
* csv
* tkinter
* bs4

## Author
* Lee Taylor
