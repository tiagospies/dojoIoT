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

Esquema do exemplo utilizando a ESP8266:
[![1](https://halckemy.s3.amazonaws.com/uploads/attachments/353971/cayenne_ldr_zOtjgsiGbu.png)](https://halckemy.s3.amazonaws.com/uploads/attachments/353971/cayenne_ldr_zOtjgsiGbu.png)

## IFTTT
Ferramenta para gerenciamento de ações entre serviços e dispositivos utilizando a simple operação *"IF"*.

### Estrutura
`./` <br />
  `└─ Client-ESP8266/door_open` &nbsp;-> *Cliente IFTTT em Micropython onde todas as vezes em que a interrupção externa da porta *"P0"* da *"ESP866"* é acionada, é enviada uma HTTPRequest para a URL do IFTTT, indicando que a porta está aberta.* <br />
  `└─ Client-ESP8266/luminosity` &nbsp;-> *Cliente IFTTT em Micropython onde ao anoitecer ou amanhecer, é enviada uma HTTPRequest para a URL do IFTTT, indicando que que este evento ocorreu, e qual o valor A/D de luminosidade registrado no momento.* <br />

Esquema do módulo com o sensor de magnetismo RedSwitch:
Esquema do exemplo utilizando a ESP8266:
[![2](https://horaciobouzas.files.wordpress.com/2015/07/screen-shot-2015-07-31-at-4-03-43-pm.png)](https://horaciobouzas.files.wordpress.com/2015/07/screen-shot-2015-07-31-at-4-03-43-pm.png)

## ZettaJS
Protocolo baseado em NodeJS, onde cada device é um servidor RESTFUL HTTP, para proporcionar a programação dita como *Reativa*. 
<br/>
É possivel com este protocolo criar **hubs** de comunicação, proporcionando uma estrura distribuida de servidores.
<br/>
Para comunicação com os sensores e periféricos de Hardware o ZettaJS conta com os drivers de comunicação, caso o driver que você precise não exista, você pode criar o seu. 
<br/>
Nos exemplos usamos o módulo BeagleBone Black, e um driver para trabalhar com um LED, e também um driver de *Mock* para simular um LED.

### Estrutura
`./` <br />
  `└─ Hub` &nbsp;-> *Exemplo de **HUB** onde todas as requisições são **"centralizadas"**.* <br />
  `└─ Device01` &nbsp;-> *Exemplo de **"Device"**, que provê a funcionalidade de "toggle" no led virtual.* <br />
  `└─ Device01` &nbsp;-> *Exemplo de **"Device"**, que provê a funcionalidade de "toggle" no led da Beaglebone Black.*


## ESP8266
Exemplos utilizando o módulo *ESP8266* com *Micropython*.
Para ter acesso ao sistema de arquivos da ESP8266 pode ser utilizado um pacote chamado **ampy**. Segue abaixo os passos e os comandos para a instalação.
<br/>
### Instalando o Ampy
``` python
pip install adafruit-ampy
```
OU

``` python
pip install adafruit-ampy
```

#### Comandos básicos

##### Listando diretórios
``` python
ampy -p COM<Porta> ls
```

##### Rodando aplicação
``` python
ampy -p COM<Porta> run <arquivo.py>
```

##### Copiando a aplicação para o módulo
``` python
ampy -p COM<Porta> put <arquivo.py>
```

##### Copiando um arquivo do módulo para o computador
``` python
ampy -p COM<Porta> get <arquivo.py>
```

##### Removendo um arquivo do módulo
``` python
ampy -p COM<Porta> rm <arquivo.py>
```

### Estrutura
`./` <br />
  `└─ Board - ESP8266/esp8266-ota-20170613-v1.9.1-4.bin` &nbsp;-> *Firmware do Micropython para a gravação na ESP8266. As instruções para a instalação do firmware podem ser encontradas [Neste Link](https://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/intro.html).* <br />
  `└─ networktest.py` &nbsp;-> *Exemplo de programa para se conectar na wifi e obter um IP na rede.* <br />
  `└─ ldr.py` &nbsp;-> *Exemplo de Leitura do conversor A/D usando o LDR onboard da ESP8266.*

Para acessar mais exemplos e a documentação do Micropython acesse [https://docs.micropython.org]()

## Beaglebone Black
Exemplos de código utilizando a beaglebone com NodeJS e o pacote para programação em **Bonescript**.

### Estrutura
`./` <br />
  `└─ Ex1` &nbsp;-> *description* <br />
  `└─ Ex2` &nbsp;-> *description* <br />
  `└─ Ex3` &nbsp;-> *description*


## Raspbarry PI3 Model B
Exemplos de código utilizando a Raspbarry PI3 utilizando sistema operacional **Android Things**.

### Estrutura
`./` <br />
  `└─ Ex1` &nbsp;-> *description* <br />
  `└─ Ex2` &nbsp;-> *description* <br />
  `└─ Ex3` &nbsp;-> *description*

