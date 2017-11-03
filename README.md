# Dojo sobre IoT
O repositório contém os códigos para a implementação dos exemplos apresentados no Dojo.
Os exemplos estão separados pelos protocolos, Sistemas Operacionais e módulos utilizados no Dojo.

## MQTT
Mensageiro para devices com alto desempenho de telemetria. No sistema há um servidor centralizado chamado de **broker**, o qual é responsável pelo envio das mensagens para o os grupos.
### Estrutura
`./` <br />
  `└─ Client` &nbsp;-> *Cliente em NodeJS para comunicar com o servidor MQTT e enviar uma mensagem de teste.* <br />
  `└─ Client-ESP8266` &nbsp;-> *Cliente MQTT em Micropython onde é feita a medida de luminosidade pelo valor A/D da porta onde está o LDR(sensor de luminosidade). Logo após a medida é enviada para o servidor* <br />
  `└─ Server` &nbsp;-> *Servidor MQTT construido com o Mosca MQTT para NodeJS servindo como Broker MQTT.*

Esquema do exemplo utilizando a ESP8266:
[![1](https://cdn.instructables.com/F3P/CZSJ/IZYGIEL7/F3PCZSJIZYGIEL7.MEDIUM.jpg)](https://cdn.instructables.com/F3P/CZSJ/IZYGIEL7/F3PCZSJIZYGIEL7.MEDIUM.jpg)

## IFTTT
Ferramenta para gerenciamento de ações entre serviços e dispositivos utilizando a simples operação *"IF"*.

### Estrutura
`./` <br />
  `└─ Client-ESP8266/door_open` &nbsp;-> *Cliente IFTTT em Micropython onde todas as vezes em que a interrupção externa da porta *"P0"* da *"ESP866"* é acionada, é enviada uma HTTPRequest para a URL do IFTTT, indicando que a porta está aberta.* <br />
  `└─ Client-ESP8266/luminosity` &nbsp;-> *Cliente IFTTT em Micropython onde ao anoitecer ou amanhecer, é enviada uma HTTPRequest para a URL do IFTTT, indicando que que este evento ocorreu, e qual o valor A/D de luminosidade registrado no momento.* <br />

Esquema do módulo com o sensor de magnetismo RedSwitch:
[![2](https://horaciobouzas.files.wordpress.com/2015/07/screen-shot-2015-07-31-at-4-03-43-pm.png)](https://horaciobouzas.files.wordpress.com/2015/07/screen-shot-2015-07-31-at-4-03-43-pm.png)

## ZettaJS
Protocolo baseado em NodeJS, onde cada device é um servidor RESTFUL HTTP, para proporcionar a programação dita como *Reativa*. 
<br/>
É possivel com este protocolo criar **hubs** de comunicação, proporcionando uma estrura distribuida de servidores.
<br/>
Para comunicação com os sensores e periféricos de Hardware o ZettaJS conta com os drivers de comunicação, caso o driver que você precise não exista, você pode criar o seu. 
<br/>
Nos exemplos usamos o módulo BeagleBone Black, e um driver para trabalhar com um LED, e também um driver de *Mock* para simular um LED.
<br/>
Para simular as ações do ZettaJS é utilizado um browser oferecido pelo próprio framework: 
http://browser.zettajs.io/#/overview?url=http:%2F%2F127.0.0.1:3000&filter=BeagleBone%20LED
<br/>
Para utilizar uma action via REST você pode utilizar o **POSTMAN**, passando a url com com o hash de identificação do device que você irá utilizar, e no *body* você pode passar a action. 
<br/>
Exemplo: http://127.0.0.1:3000/servers/Device02/devices/831ec80b-33c4-4067-b1f5-aabcefe2ad43
body{
  action: "turn-on"
}

### Estrutura
`./` <br />
  `└─ Hub` &nbsp;-> *Exemplo de **HUB** onde todas as requisições são **"centralizadas"**.* <br />
  `└─ Device01` &nbsp;-> *Exemplo de **"Device"**, que provê a funcionalidade de "toggle" no led virtual.* <br />
  `└─ Device02` &nbsp;-> *Exemplo de **"Device"**, que provê a funcionalidade de "toggle" no led virtual.*<br />
  `└─ BeagleBoneDeviceLed` &nbsp;-> *Exemplo de **"Device"**, que provê a funcionalidade de "toggle", "turn-on" e "turn-off" no led da Beaglebone Black. Junto ao exemplos temos um arquivo **device.js** onde é criado um driver para trabalhar com os LED's da Beaglebone Black.*

## ESP8266
Exemplos utilizando o módulo *ESP8266* com *Micropython*.

### Instalando o micropython
#### Pacote para a instalação
``` python
pip install esptool
```
#### Comando para gravar a flash da ESP
``` python
esptool.py --port COM4 --baud 460800 write_flash --flash_size=detect
``` 

Para ter acesso ao sistema de arquivos da ESP8266 pode ser utilizado um pacote chamado **ampy**. Segue abaixo os passos e os comandos para a instalação.
<br/>
### Instalando o Ampy
``` python
pip install adafruit-ampy
```
OU

``` python
pip3 install adafruit-ampy
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
Para utilizar a Beaglebone Black com NodeJS é aconselhado o uso do Sistema operacional **debian** em um compilação própria para a 
Beaglebone. Esta versão pode ser encontrada em https://debian.beagleboard.org/images/bone-debian-9.2-iot-armhf-2017-10-10-4gb.img.xz.
<br/>
Para instalar a imagem no SDCard pelo windows você pode utilizar a ferramenta [Win32DiskImager](https://sourceforge.net/projects/win32diskimager/), e basta escolher a imagem e mandar gravar.
<br/>
Quando você pluga a Beagle na usb do computador ela cria uma interface de rede virtual no seu computador, e assim você pode acessar a placa a partir do IP **192.168.7.2**, na porta 80 há uma série de exemplos utilizando o **Bonescript**, e você pode rodá-los pelo próprio navegado, porém você tem uma opção muito mais interessante, que é a IDE **Cloud9**, que está disponível na porta *3000*. Na IDE do Cloud9 você já tem uma série de exemplos e você pode criar seus próprios diretórios e arquivos, podendo também acessar o bash diretamente pelo navegador, assim você pode installar os seus pacotes e fazer todas as operações necessárias para que o aplicativo rode.
<br/>
O [Cloud9](https://c9.io/) é uma IDE extremamente amigável e desenvolvida em NodeJS, o que já é um grande atrativo para trabalhar com a Beaglebone.

### Estrutura
`./` <br />
  `└─ \Board - BeagleBone\Blink OnboardLED` &nbsp;-> *Neste exemplo são acessados os GPIO's dos led's e é feito o toggle dos led's dado um intervalo de tempo ditado pelo 'interval'* <br />
  `└─ \Board - BeagleBone\AD_simple` &nbsp;-> *Neste exemplo é feita a leitura de um conversor A/D, e logo após é feita a escrita do valor lido em um port A/D configurado como **output*** <br />


## Raspbarry PI3 Model B
Exemplos de código utilizando a Raspbarry PI3 utilizando sistema operacional **Android Things**.
Para utilizar a imagem do Androir Things na RaPI3, você pode baixar a imagem do Sistema no [Android Things Console](https://partner.android.com/things/console/), onde você cria o seu próprio build com a placa de desenvolvimento desejada e a última versão do Android Things.
<br/>
Depois de criada a imagem você pode gravá-la no SDCard utilizando a ferramenta [Win32DiskImager](https://sourceforge.net/projects/win32diskimager/). 
<br/> **Importante:** *Utilize um SDCard no mínimo de classe 10, caso contrario o sistema nem irá inicializar.*
<br/>
### Utilizando o debugger do Android
Depois de instalado o Android Things, você terá que conectar o cabo UTP na placa ligado ao seu swicth para que a placa tenha um IP atribuido, este ip aparecerá na tela que você estiver conectado com o cabo HDMI. Você pode utilizar o Debug pelo cabo mesmo, porém é um pouco incômodo, então você tem a opção de fazer o debug por *Wifi*, seguido estes passos:
<br/>
1. Conecte com a placa via adb.
``` bash
adb connect <new-ip-address:5555>
```

2. Confirme a conexão com o dispositivo.
``` bash
adb devices
```

3. Configure a conexão Wifi
``` bash
am startservice \
    -n com.google.wifisetup/.WifiSetupService \
    -a WifiSetupService.Connect \
    -e ssid YOURWIFINAME \
    -e passphrase YOURWIFIPASSWORD
```

4. Reinicie a placa e verifique o IP atribuido a conexão Wifi, após repita o *passo 1* conectando o **adb** na placa via Wifi.

Pronto, agora você pode rodar e fazer o debug dos aplicativos instalados na *RaPI3* via Wifi.

### Estrutura
`./` <br />
  `└─ AndroidThings\simple-audio` &nbsp;-> *Aplicativo utilizando um botão via hardware com um handler onde será utilizada a biblioteca **texttospeach** para dar as boas vindas ao Dojo* <br />
  `└─ AndroidThings\image-classifier` &nbsp;-> *Aplicativo para classificar imagens e passar a descrição do objeto de acordo com o match feito utilizando a biblioteca **Tensorflow*** <br />

