from pessoafisica import PessoaFisica
from pessoajuridica import PessoaJuridica

print('*'*8, 'Pessoa Fisica', '*'*8)
pessoa_fisica = PessoaFisica('Márcio Lourenço', '031.060.172-01', 1000.0)
print(pessoa_fisica)

print('*'*8, 'Pessoa Fisica/Alterações', '*'*8)
pessoa_fisica.segundo_titular = 'Evan Lucas\n'
print(pessoa_fisica.segundo_titular)

print('*'*8, 'Pessoa Juridica', '*'*8)
pessoa_juridica = PessoaJuridica('Quero-tudo-Que-é-Seu', '59.4569.0001-10', 100000.0)
print(pessoa_juridica)

print('*'*8, 'Pessoa Juridica/Alterações', '*'*8)
pessoa_juridica.segundo_titular = 'LulaNaro'
print(pessoa_juridica.segundo_titular)
