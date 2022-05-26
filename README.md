# WhatsPy
 
### Automação simples para envio de mesagens no Whatsapp.
 
Essa automação permite que mensagens sejam enviadas para o Whatsapp de várias pessoas de uma lista de contatos.
 
O código lê uma planilha no Excel que é preenchida pelo usuário. Essa planilha deve conter o Nome do destinatário, o número de telefone com o +55 e o DDD e a mensagem desejada.

![image](https://user-images.githubusercontent.com/65752974/170583747-13190b8a-96f5-40d4-89ca-e5f2e2ce8c1a.png)


Toda mensagem começa com um "Oi {Nome da Pessoa}", o que personaliza a mensagem para cada contato, evitando aquelas listas de transmissões. Leve isso em consideração na hora de criar suas mensagens!

## Pontos de Atenção

**Apesar de ser um script simples, ele é bem eficente em enviar mensagens, logo o número de pessoas que você pode alcançar é muito grande.
Paradoxalmente, o Whatsapp não gosta de automações em sua plataforma, então é bom evitar de enviar mensagem para uma quantidade massiva de pessoas.**

**O código funciona em um ritmo lento propositalmente, ele é feito para imitar o comportamento humano de envio de mensagens e com isso passar despercebido pelo algoritmo do Whatsapp.**

## Sobre o Código e instruções adicionais

Essa automação é desenvolvida completamente em python!

Usei bibliotecas como `pandas`, `selenium`, `urllib` e `time`. O código foi desenvolvido no `Jupyter Notebook`. 

O que ele faz basicamente é modificar aquela URL que é criada pelo whatsapp para o envio de mensagens:

```
link = f'https://web.whatsapp.com/send?phone={numero}&text={texto}'
```

Ao percorrer a planilha preenchida ele substitui os valores {numero} e {texto}, depois ele entra nesse link, o que faz com que ele seja redirecionado direto para o chat da pessoa desejada.

*A mensagem já é formatada com os padrões da url pela biblioteca urllib, então pode escrever sem se preocupar com isso*

Toda vez que o código é iniciado você deverá ler o qrcode do whatsapp, uma vez que ele sempre rodará em guia anônima.

Disponibilizei o arquivo [WhatsPy.zip](WhatsPy.zip) para o download, com ele você poderá rodar o código sem ter python em seu computador.

Esse é o executável que estará dentro da pasta: 

![image](https://user-images.githubusercontent.com/65752974/170585231-921ec9ed-ebca-49ba-872c-2d1b76f2d2fa.png)

Antes de iniciar, verifique sua versão do Chrome, esse código foi feito na versão 101.0.4951.67 so Chrome (Leve em consideração o 101.0 somente).
Caso seu Chrome seja de uma versão inferior ou superior, você deve substituir o seguinte arquivo com um compativel com a sua versão do navegador:

![image](https://user-images.githubusercontent.com/65752974/170585527-dc2791c5-0e2b-477c-8bc1-731ec27e7b5a.png)

Você pode encontrar esse arquivo para download no site oficial do [Chrome](https://chromedriver.chromium.org/downloads)

A planilha de envio também está dentro da pasta, recomendo que crie um atalho para ela e para o executavel do programa na área de trabalho: 

![image](https://user-images.githubusercontent.com/65752974/170586014-a839ee0a-faea-4e9c-8d9a-a4dec437ffd1.png)

Use com moderação!

