import flet as ft
import requests

class StandardEnglish:
    def __init__(self,text_to_convert):
        self.text_to_convert = text_to_convert
        
    def convert(self):
        response = requests.post('http://localhost:5000/correct', json={'text': self.text_to_convert})
        if response.status_code==200:
            return response.json()['corrected']
        else:
            return "Error in correction"