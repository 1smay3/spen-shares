import pandas as pd
import pickle
from settings import SPYDATAROOT




def loadspycon():

    with open(SPYDATAROOT, 'rb') as handle:
        SPYConstituents = pickle.load(handle)

    SPYConstituents = [ k["symbol"] for k in SPYConstituents]
    SPYConstituents.remove('BRK.B')
    SPYConstituents.remove('BF.B')
    SPYConstituents.remove('CARR')
    SPYConstituents.remove('FRC')
    return SPYConstituents



def SPYConstituentsDictionarynames(key1, key2):
    
    with open(SPYDATAROOT, 'rb') as handle:
        SPYConstituents = pickle.load(handle)

    names = [k["name"] for k in SPYConstituents]
    tickers = [k["symbol"] for k in SPYConstituents]

    # mappedData = dict(zip(tickers,names ))
    # mappedData = []
    # for symbol, fullname in zip(tickers,names) :
    #     mappedData.append({'Symbol': symbol, 'FullName': fullname})
    #     return mappedData
    return names

def SPYConstituentsDictionaryFULL(key1, key2):
    
    with open(SPYDATAROOT, 'rb') as handle:
        SPYConstituents = pickle.load(handle)

    names = [k["name"] for k in SPYConstituents]
    tickers = [k["symbol"] for k in SPYConstituents]

    #map tickers to names
    mappeddata = []
    for symbol, fullname in zip(tickers, names):
        mappeddata.append({fullname: symbol})
    return mappeddata




def SPYConstituentsDictionarytickers(key1, key2):
    
    with open(SPYDATAROOT, 'rb') as handle:
        SPYConstituents = pickle.load(handle)

    names = [k["name"] for k in SPYConstituents]
    tickers = [k["symbol"] for k in SPYConstituents]

    # mappedData = dict(zip(tickers,names ))
    # mappedData = []
    # for symbol, fullname in zip(tickers,names) :
    #     mappedData.append({'Symbol': symbol, 'FullName': fullname})
    #     return mappedData
    return tickers


def getspydictionary():
    
    with open(SPYDATAROOT, 'rb') as handle:
        SPYDict = pickle.load(handle)

    keys = {"name", "symbol"}

    filtered_dict = [{k:v for k, v in i.items() if k in keys} for i in SPYDict]

    #rename keys to be comaptible
    for d in filtered_dict:
        d['label'] = d.pop('name')
        d['value'] = d.pop('symbol')

    return filtered_dict





