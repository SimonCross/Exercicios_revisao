"""

# Tipos de variaveis

int(5)
float(3.9)
str("Beta" 'Beta')
bool(true)
print("Ola mundo")
print(input(Insira a palavra chave))

mensagem = str(input("Fala serio"))
print(mensagem)

# Variaveis Aritimeticas
(+) (-) (/) (//) (*) (**)


print(1+1)
print(1-1)
print(2*2)
print(4/2)
print(5//2)
print(2**4)
print(5%2)
print(2>1)
print(2<1)
print(2==2)
print(2!=2)
"""

"""

nome = str(input(f"Favor inserir o codigo do funcionario: "))
funcionario = "nao"  # Nesse caso tive que dar um valor pre determinado para 
                     # variavel porque o O bloco if funcionario == "sim": está fora do 
                     # bloco if nome == "1234":, então se o código do funcionário não for "1234",
                     # a variável funcionario 
                     # não será definida, e quando o programa tentar acessá-la no bloco 
                     # if funcionario == "sim":, ocorrerá um erro.

if nome == "1234":
    print("Matheus Gatti França")
    funcionario = (input(f"Voce deseja em aumentar o salario do funcionario código: {nome}\n"))

if funcionario == "sim":
    salA = 2000
    aumento = salA*10/100
    desconto =  salA * 5/100
    atual = (salA + aumento) - desconto

    print(f"O salario anterior era: {salA}")
    print(f"O aumento é: {aumento}")
    print(f"O desconto é : {desconto}")
    print(f"O valor atual é: {atual} ")

else:
    print("Erro 404 operção não pode ser realizada")

"""

nome = input("Favor digite seu nome: ")
nota1 = float(input(f"favor digitar sua nota do 1 bimestre: "))
nota2 = float(input(f"favor digitar sua nota do 2 bimestre: "))
nota3 = float(input(f"favor digitar sua nota do 3 bimestre: "))
nota4 = float(input(f"favor digitar sua nota do 4 bimestre: "))

media = (nota1 + nota2 + nota3 + nota4)/4

print(f"Sua media final foi : {media}")






