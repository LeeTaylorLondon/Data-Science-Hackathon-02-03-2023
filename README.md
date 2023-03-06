# Company Activities Interpretation Tool
Develop a tool to report in realtime the activities of any given company.

## How to Use - Realtime Report
* Execute `main.py` or `Render.py` 
* Input a company name into the 'Company Name:' field

## `Render.py` Example Usage
![Image](/images/rm1.png)  
* The user inputs a company name
* The first google result is parsed for human friendly readable text
* This text is passed to text-davinci-003 as a prompt
* A bullet point list of activities conducted by the company is outputted

## Dataset
The 'elevate' website is a platform that contains information about 711 startups. 
I scraped the website, downloaded the HTML files for each startup, 
and extracted human-friendly readable text from these HTML files.

The dataset storing `.html` files can be found [here](/Greek%20Startups/Excel%20Files%20&%20Processing/soup_objects).  
The dataset storing the **'human-friendly-readable'** text can be found [here](/Greek%20Startups/Excel%20Files%20&%20Processing/soup_to_text).

## Author
* Lee Taylor
