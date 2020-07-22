# CursoPythonFlask
 Curso de Flask


# Fpw Sindicato

Origem: *Oracle*
Destino: *BigQuery*

## Processo

Processo tem como origem o *Oracle*
1. Fazemos uma query que busca da tabela `ZONA_INTERMED.VWSINDICATO`
2. É feito as tratativas iniciais no Wrangler e feita a inclusao dos Campos de controle para a Stage
3. Logo em seguinda os dados sao incluidos dentro do *BigQuery* como uma Stage
4. Agora no proximo passo temos uma query em que vamos fazer um check
   - Verificar se dado ja existe dentro da Tabela Final
   - Caso exista vamos fazer a alteração nos campos DataValidadeFim(Data da Alteração) e VigenciaCtrl(0)
   - Sera feito a Inclusao do campo atualizado(No formato de novo registro)
5. Apos isso vamos incluir na tabela Final **DimSindicato**
