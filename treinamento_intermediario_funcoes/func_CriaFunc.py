#Exercicio -> criar uma função que duplique, triplique ou duadriplique um valor recebido pelo parâmetro


def increase_value(num):
    def multiplier(multi):
        value = num * multi
        return value
    return multiplier



number = int(input("Insira um número para duplicar, triplicar duadriplicar e quintuplicar : "))

increase_value_v = increase_value(number)

print(increase_value_v(2))
print(increase_value_v(3))
print(increase_value_v(4))
print(increase_value_v(5))

