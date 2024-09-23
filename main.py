# Esse arquivo vai servi apenas para executar o programa

from fakepinterest import app


# Garantindo que so vou executar o site se for executado nesse arquivo
if __name__ == "__main__":
    # A vantagem de utilizar o parâmetro debug=True, é que não precisamos ficar executando o código toda vez que
    # fizermos auterações. Esse parâmetro reconhece a auteração e ao atulaizar a página, ja fica prontinho.
    app.run(debug=True)
           
           