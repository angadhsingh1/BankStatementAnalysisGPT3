# Command: python3 bankAnalysisPDF.py

import sys
import openai
from PyPDF2 import PdfReader

# --------------------------- References ----------------------- #
# https://www.geeksforgeeks.org/extract-text-from-pdf-file-using-python/

# --------------------------- API Call ------------------------- #
openai.api_key = os.getenv("OPENAI_API_KEY")
sys.path.append('/usr/local/lib/python2.7/site-packages')

# ------------------------ Functions --------------------------- #

def pdfReader(filename):
    """_summary_
    Args:
        args (_type_): _description_
        images (_type_): _description_

    Returns:
        _type_: _description_
    """

    # creating a pdf reader object
    reader = PdfReader(filename)

    # printing number of pages in pdf file
    print(len(reader.pages))

    # getting a specific page from the pdf file
    page = reader.pages[0]

    # extracting text from page
    text = page.extract_text()
    print(text)
    
    return text

def gptAPICall(dataRead):
	"""
 	Summary: GPT API Call
	Args:
		dataRead (_type_): stores the data read form image
	Returns:
		_type_: Nothing
	"""
	response = openai.Completion.create(
	model="text-davinci-003",
	prompt = "can you analyze the account activity and categorize \
				transactions into categories"+ "\n" + dataRead + "\n The return response\
				Should be in the follwoing format: \
				Grocery: \
				09/10/2021 GIANT FOOD I $78.22 \
				09/14/2021 MD GIANT FOOD $15.40 \
				Fitness: \
				09/10/2021 LA FITNESS $15.",
	temperature=0.6,
	max_tokens=100,
	top_p=1.0,
	frequency_penalty=0.0,
	presence_penalty=0.0
	)
	print("GPT response")
	print(response.choices[0].text)

def main():
    filename = 'February 2023 e-Statement.pdf'
	# Reading Data from image  
    dataRead = pdfReader(filename)
	
 	# Calling GPT API
	# categorizedData = gptAPICall(dataRead)
 
if __name__ == '__main__':
    main()
		 
     
 
	
