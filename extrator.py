import re

class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitizar_url(url)
        self.validar_url()
    
    def sanitizar_url(self, url):
        if type(url) == str:   
            return url.strip()
        else:
            return ""
    
    def validar_url(self):
        if not self.url:
            raise ValueError("A URL está vazia")
        
        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)

        if not match:
            raise ValueError("A URL não é válida")
        
    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros
    
    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_divisor = self.get_url_parametros().find('&', indice_valor)

        if (indice_divisor == -1):
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_divisor]

        return valor
    
    def __len__ (self):
        return len(self.url)
    
    def __str__(self):
        return f'{self.url}\nURL Base: {self.get_url_base()}\nParâmetros: {self.get_url_parametros()}'
    
    def __eq__(self, other):
        return self.url == other.url
        
teste = ExtratorURL("https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100")
valor = teste.get_valor_parametro('quantidade')