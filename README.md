# Projeto de Segurança da Informação - Exercício de validação de hash SHA256 e MD5
Foram providas várias frases juntamente de códigos hash calculados, utilizando o código fonte o exercício se trata de comparar os códigos SHA256 e MD5 gerados com os códigos providos, verificando se eles estão corretos ou errados caso derem diferentes

# Tabela:
| Frase Original | HASH SHA256 exercício | HASH MD5 exercício | HASH SHA256 gerado | HASH MD5 gerado | SHA256 correto? | MD5 correto? |
| --- | --- | --- | --- | --- | --- | --- |
| A primeira das instituições criadas pelo Pe. Roberto Sabóia de Medeiros foi a antiga Escola Superior de Administração de Negócios de São Paulo - ESAN/SP. | d24de3ec3835115c576a55188a31761b73af93ed2c45a171c810bb66b24b08f9 | c850e1a34a6ed572e0758ccd9c615bda | d2150d688c337fc57e235adafd57f86d7aba0b8682c249b1006ba592706f88a0 | 1c4ecc238571333ae507f82ff6a5e9e4 | Correto | Correto |
| A FEI é uma instituição vinculada estatutariamente à Companhia de Jesus | 6979a3d7a19e5921ae00ca7db9b814e1b83831dcedfca33dbb72e761ca084337 | b710771da8d7521524f45233ea9dd9e1 | 6979a3d7a19e5921ae00ca7db9b814e1b83831dcedfca33dbb72e761ca084437 | b710771da8d7521524f45233ea9bb9e1 | Errado | Errado |
| Em 20 de janeiro de 1951 foi realizada a sessão solene da congregação para a Colação de Grau da primeira turma da Faculdade de Engenharia Industrial." | 6c582a993ba3ea454f11221a374878e534cfe666060c87ba03127de07f1ca4e6 | 55748c2cb669a9d9508677cb914cb025 | 6c582a993ba3ea454f11221a374878e534cfe666060c87ba03127de07f1ca4e6 | 55748c2cb669a9d9508677cb914cb025 | Correto | Correto |
| A Capela Santo Inácio de Loyola foi construída no ano de 1978, em concreto aparente. | 254e695d0f8835651bc231f9cf1b2a7a097b849648f05f79f1855a55f85b089e | f4a8a299fd4da2a5d70b374be2e48147 | 245e695d0f8835651bc231f9cf1b2a7a097b849648f05f79f1855a55f85b089e | f4a8a299fd4da2a5d70b374be2e48417 | Errado | Errado |
