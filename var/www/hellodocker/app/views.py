from app import app

@app.route('/')
def home():
   return "Eu sou Full Cycle."