python-bitcoinadress
====================
Bitcoin address validation


Python-bitcoinadress Python 3 integrations has been complated.

Note : This library should not works with (new) MULTİSİG BTC address.

Mail : yasak@gmx.com 
BTC address :  1KJ9f2xS6CMLeeUJ9t2rf5VCauhGjbcUtZ
ETH address : 0xFBd6f9704478104f0EF3F4f9834c3621210fE598

For donations !

## How can i install!

```shell
git clone https://github.com/omgbbqhaxx/python-bitcoinaddress.git
cd python-bitcoinaddress
python setup.py build
python setup.py install
```

## How can i use!

```shell
from bitcoinaddress import validation as bitcoinaddress
bitcoinaddress.validate('1KJ9f2xS6CMLeeUJ9t2rf5VCauhGjbcUtZ')
>>True
bitcoinaddress.validate('Hi')
>>False
```
