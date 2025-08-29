class Carro:
    def __init__(self,marca, modelo, cor, Placa, ano):
        self.marca = marca
        self.modelo = modelo
        self. ano = ano
        self.cor = cor
        self._garantia = True
        self._ligado = False
        self._seguro = False
        self.placa = Placa
        self.reboque = False

    def ligar(self):
        if self._ligado :
            print(f"\n\t [Erro] ja esta ligado \n")
        else:
             print(f"\n\t [ok] O carro esta ligado \n")
             self._ligado=True
        
    def desligar(self):
        if self._ligado:
            self._ligado=False
            print(f"\n\t [ok] O carro esta desligado \n")
        else:
            print(f"\n\t [Erro] ja esta desligado \n")
    
    def contratar(self):
        if self._seguro:
            print(f"\n\t [Erro] Segurro nao foi contratado\n")
        else: 
            print(f"\n\t [ok] Segurro Contratado \n")
            self._seguro = True
    
    def cancelar(self):
        if self._seguro:
            self._seguro= False
            print(f"\n\t [ok] Segurro cancelado\n")
    
    def instalar(self):
        if self.reboque:
            self.reboque = True
            print(f"\n\t [ok] Reboque instalado\n")

    def desinstalar(self):
        if self.reboque:
             print(f"\n\t [ok] Reboque desintalado\n")
    
    def emplacar(self):
        if self.placa:
            print(f"\n\t [ok] Carro  Emplacado\n")
        
    def exibir_info(self):
        status = ""
        status_seguro = ""
        placa = ""
        reboque= ""
        if self._ligado:
            status = "Ligado"
        else   :
            status = "desligado"
        if self._seguro:
            status_seguro ="Com seguro"
        else:
            status_seguro = "sem seguro"
        if self.placa:
            placa = self.placa
        else :
            placa = "sem Placa"
        if self.reboque:
            reboque = "Instalado"
        else:
            reboque = "Desinstalar"

        
        print(f'Carro: {self.marca} - {self.modelo} \n Ano: {self.ano} Cor: {self.cor} \n Placa: {placa} \n Seguro: {status_seguro} \n Reboque: {reboque} \n Status: {status}')

        pass

meu_carro = Carro("WV", "Gol", "Verde", "XWZ123", 2013)
meu_carro2 = Carro("fiat", "Mub", "Preto", "DDD555", 2024)
meu_carro3 = Carro("citroen", "c3", "vermelho", "fff852", 2025)

garagem={}

garagem[meu_carro.placa] = meu_carro 
garagem[meu_carro2.placa] = meu_carro2
garagem[meu_carro3.placa] = meu_carro3


garagem







print(meu_carro)

meu_carro.exibir_info()





#meu_carro.contratar()

#meu_carro.exibir_info()

#meu_carro.cancelar()

#meu_carro.exibir_info()

#meu_carro.desligar()

#meu_carro.ligar()

#meu_carro.exibir_info()
