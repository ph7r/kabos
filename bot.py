from flask import Flask
import random
app=Flask(__name__)
@app.route('/')
def kabos():
 A = 'shzsh_.kaavzogwoygwi7bstewacjuwhh'
 s = ['1122334455', '1111122222', '1234512345', '1234554321', '1212121212']
 N = str(''.join(random.choice(s) for i in range(1)))
 V = str(''.join(random.choice(A) for i in range(4)))
 return 'User : '+V+' | '+'Pass : '+N+' | xDeV : @NnKoNn .'
app.run()
