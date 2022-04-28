import spacy
from .entity_extractor import extract_email_addresses,extract_phone_numbers

# function for prediction
def predict(text):
    output={}
    nlp=spacy.load(r"C:\Projects\Resume\Django-app\working3\api\model1") # load the model

    # print('\n')
    doc = nlp(text)
    # print(text)
    

    for ent in doc.ents:
        # print(f'{ent.label_.upper():{30}}-{ent.text}')
        output[ent.label_.upper()]=ent.text
    # print(f"Mobile    -{' '.join(extract_phone_numbers(text))}")
    # print(f"Email     -{' '.join(extract_email_addresses(text))}")
            
    return output
        
