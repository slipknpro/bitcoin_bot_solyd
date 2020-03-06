import ssl
import json

import websocket

def comprar():
    print('Comprou')


def vender():
    print('Vendeu')



def ao_abrir(ws):
    print('abriu a conexão')

    json_subscribe = '''
    {
        "event": "bts:subscribe",
        "data": {
            "channel": "live_trades_btcusd"
        }
    }    
'''
    ws.send(json_subscribe)


def ao_fechar(ws):
    print('fechou a conexão')


def erro(ws, erro):
    print('Deu erro: ', erro)


def ao_receber_mensagem(ws, mensagem):
    mensagem = json.loads(mensagem)
    price = mensagem['data']['price']
    print(price)

    if price > 9000:
        vender()
    elif price < 8100:
        comprar()
    else:
        print('aguardar !')


if __name__ == '__main__':
    ws = websocket.WebSocketApp('wss://ws.bitstamp.net.',
                                on_open=ao_abrir,
                                on_close=ao_fechar,
                                on_message=ao_receber_mensagem,
                                on_error=erro)
    ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})