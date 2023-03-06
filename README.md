# Company Activities Interpretation Tool
Develop a tool to report in realtime the activities of any given company.

## How to Use - Realtime Report
* Create a python file called `api_key.py` add a string: 
```python
API_KEY = '<YOUR API KEY HERE>'
```
* Generate an OpenAI key [here](https://platform.openai.com/account/api-keys).
* Execute `main.py` or `Render.py` 
* Input a company name into the 'Company Name:' field

## `Render.py` Example Usage
![Image](/images/rm1.png)  
* The user inputs a company name
* The first google result is parsed for human friendly readable text
* This text and the objective is passed to [OpenAIs LLM text-davinci-003](https://platform.openai.com/docs/guides/completion) as a prompt
* A bullet point list of activities conducted by the company is outputted

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
