# Author: Lee Taylor
from URL_Functions import *
from Analysis_LLM import *

if __name__ == '__main__':
    # Url to soup (text)
    soup = url_to_soup_obj("https://registry.elevategreece.gov.gr/company/"
                        "i-love-dyslexia-english-language-innovation-eli-ike/")

    # # Write soup object (text of website) to .html-file
    # with open("HTML Files/registry.elevategreece.gov.html", 'w', encoding='utf-8-sig') as f:
    #     f.write(str(soup))

    # Process .html for P's
    # ps = extract_elements(html_text)
    ps = extract_text(soup)  # Todo: fix outputting chars instead of strs

    # Debug (out paragraphs to console)
    for p in ps:
        print(p)

    # Pass paragraph text to LLM with
    prompt_ = create_prompt(ps)
    response = gen_response(prompt_)
    output = response_text(response)

    # Debug (out var output)
    print(output)

    # Mark end of if-name-main section
    pass
