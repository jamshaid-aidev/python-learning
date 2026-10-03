letter ='''Dear <|NAME|>,
You are selected!   
         <|Date|>'''
print(letter.replace("<|NAME|>", input("Enter your name: ")).replace("<|Date|>", "24 OCT 2024"))