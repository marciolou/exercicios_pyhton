from produto import Produto

produto1 = Produto(id=1, nomeproduto='Leitinho', valor='R$17', quantidade='10cx')
produto2 = Produto(id=2, nomeproduto='Açucar', valor='R$05', quantidade='10pc')
produto3 = Produto(id=3, nomeproduto='ovo', valor='R$19', quantidade='15cb')

print(produto1.id, produto1.nomeproduto, produto1.quantidade, produto1.valor)
print(produto2.id, produto2.nomeproduto, produto2.quantidade, produto2.valor)
print(produto3.id, produto3.nomeproduto, produto3.quantidade, produto3.valor)
