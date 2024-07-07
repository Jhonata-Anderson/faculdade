from Pessoa import pessoa
from PessoaFisica import PessoaFisica
from PessoaJuridica import PessoaJuridica

# Instanciando um objeto da classe Pessoa e imprimindo os valores
pessoa = pessoa("João", "12345-6", "2023-01-01", True)
print("Valores da instância da classe Pessoa:")
pessoa.imprimir_valores()

# Instanciando um objeto da classe PessoaFisica e imprimindo os valores
pessoa_fisica = PessoaFisica("Maria", "54321-0", "2022-12-31", False,
                             "1990-05-15", "000.111.222-33", "987654321")
print("\nValores da instância da classe PessoaFisica:")
pessoa_fisica.imprimir_valores()

# Instanciando um objeto da classe PessoaJuridica e imprimindo os valores
pessoa_juridica = PessoaJuridica("Empresa XYZ", "99999-9", "2024-01-01", True,
                                 "2010-01-01", "00.123.456/0001-00")
print("\nValores da instância da classe PessoaJuridica:")
pessoa_juridica.imprimir_valores()

# Alterando valores usando setters e validando CPF e CNPJ
print("\nAlterando valores e validando CPF e CNPJ:")

# Alterando valores para a classe Pessoa
pessoa.nome = "Pedro"
pessoa.numero_conta = "65432-1"
pessoa.data_abertura_conta = "2023-02-01"
pessoa.status = False
pessoa.imprimir_valores()

# Alterando valores para a classe PessoaFisica
try:
    pessoa_fisica.cpf = "123.456.789-00"  # CPF inválido
except ValueError as e:
    print(f'Erro ao tentar definir CPF: {e}')
pessoa_fisica.cpf = "111.222.333-44"  # CPF válido
pessoa_fisica.nome = "Ana"
pessoa_fisica.imprimir_valores()

# Alterando valores para a classe PessoaJuridica
try:
    pessoa_juridica.cnpj = "12345678000100"  # CNPJ inválido
except ValueError as e:
    print(f'Erro ao tentar definir CNPJ: {e}')
pessoa_juridica.cnpj = "99.876.543/0001-21"  # CNPJ válido
pessoa_juridica.nome = "Nova Empresa"
pessoa_juridica.imprimir_valores()
