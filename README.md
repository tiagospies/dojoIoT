# Dojo sobre IoT
O repositório contém os códigos para a implementação dos exemplos apresentados no Dojo.
Os exemplos estão separados pelos protocolos, Sistemas Operacionais e módulos utilizados no Dojo.

## MQTT
Mensageiro para devices com alto desempenho de telemetria. No sistema há um servidor centralizado chamado de **broker**, o qual é responsável pelo envio das mensagens para o os grupos.
### Estrutura
`./` <br />
  `└─ Client` &nbsp;-> *Cliente em NodeJS para comunicar com o servidor MQTT e enviar uma mensagem de teste.* <br />
  `└─ Client-ESP8266` &nbsp;-> *Cliente MQTT em Micropython onde é feita a medida de luminosidade pelo valor A/D da porta onde está o LDR(sensor de luminosidade). Logo após a medida é enviada para o servidor* <br />
  `└─ Server` &nbsp;-> *Servidor MQTT construido com o Mosca MQTT para NodeJS servido como Broker MQTT.*

## IFTTT
Ferramenta para gerenciamento de ações entre serviços e dispositivos utilizando a simple operação *"IF"*.

### Estrutura
`./` <br />
  `└─ Client-ESP8266/door_open` &nbsp;-> *Cliente IFTTT em Micropython onde todas as vezes em que a interrupção externa da porta *"P0"* da *"ESP866"* é acionada, é enviada uma HTTPRequest para a URL do IFTTT, indicando que a porta está aberta.* <br />
  `└─ Client-ESP8266/luminosity` &nbsp;-> *Cliente IFTTT em Micropython onde ao anoitecer ou amanhecer, é enviada uma HTTPRequest para a URL do IFTTT, indicando que que este evento ocorreu, e qual o valor A/D de luminosidade registrado no momento.* <br />

## ZettaJS
Protocolo baseado em NodeJS, onde cada device é um servidor RESTFUL HTTP, para proporcionar a programação dita como *Reativa*. 
<br/>
É possivel com este protocolo criar **hubs** de comunicação, proporcionando uma estrura distribuida de servidores.
<br/>
Para comunicação com os sensores e periféricos de Hardware o ZettaJS conta com os drivers de comunicação, caso o driver que você precise não exista, você pode criar o seu. 
<br/>
Nos exemplos usamos a placa BeagleBone Black, e um driver para trabalhar com um LED, e também um driver de *Mock* para simular um LED.

### Estrutura
`./` <br />
  `└─ Hub` &nbsp;-> *Exemplo de **HUB** onde todas as requisições são **"centralizadas"**.* <br />
  `└─ Device01` &nbsp;-> *Exemplo de **"Device"**, que provê a funcionalidade de "toggle" no led virtual.* <br />
  `└─ Device01` &nbsp;-> *Exemplo de **"Device"**, que provê a funcionalidade de "toggle" no led da Beaglebone Black.*


## ESP8266
* MQTT - Exemplo utilizando um servidor com *NodeJS* utilizando o "Mosca" e um client rodando 
na *ESP8266* enviando os dados de luminosidade para o servidor.
