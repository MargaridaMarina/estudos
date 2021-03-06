from impostos import ISS, ICMS

class CalculadorDeImpostos:
  def realiza_calculo(self, orcamento, imposto):
    imposto_calculado = imposto.calcula(orcamento)
    print(imposto_calculado)

if __name__ == '__main__':
    from orcamento import Orcamento

    calculador = CalculadorDeImpostos()
    orcamento = Orcamento(500)
    calculador.realiza_calculo(orcamento, ISS())
    calculador.realiza_calculo(orcamento, ICMS())
