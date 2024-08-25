# Rastreador de Preços do Bitcoin

Este projeto é um programa em Python que rastreia os preços do Bitcoin usando uma API de mercado de criptomoedas e envia notificações por e-mail quando o preço cai abaixo de um valor especificado pelo usuário.

## Funcionalidades

1. **Input de Dados**
   - Solicita ao usuário um valor limite para o preço do Bitcoin.
   - Solicita ao usuário um e-mail para receber notificações.

2. **Consulta à API de Criptomoedas**
   - Obtém o preço atual do Bitcoin de uma API de mercado de criptomoedas (por exemplo, CoinGecko ou CoinMarketCap).

3. **Análise de Dados**
   - Notifica o usuário por e-mail sempre que o valor do Bitcoin estiver abaixo do valor informado.

4. **Envio de Relatório por E-mail**
   - Envia um e-mail ao usuário informando o valor atual do Bitcoin e que ele está abaixo do valor solicitado.

5. **Automatização do Processo**
   - O programa é agendado para rodar a cada 10 minutos.
