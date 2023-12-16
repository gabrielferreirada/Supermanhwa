from flask import Flask, render_template

app = Flask(__name__)

@app.route('/homepage')
def homepage():
    return render_template('homepage.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')
    
@app.route('/mangas')
def mangas():
    return render_template('manga.html')
    
@app.route('/novel')
def novel():
    return render_template('novel.html') 
    
@app.route('/recomendações')
def recomendacoes():
    return render_template('recomendações.html')
    
@app.route('/manhwa')
def manhwa():
    return render_template('manhwa.html')
    
@app.route('/manhua')
def manhua():
    return render_template('manhua.html')    
     
if __name__ == '__main__':
    app.run(debug=True)
