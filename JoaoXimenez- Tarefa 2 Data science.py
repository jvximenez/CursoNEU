#João Vitor Dias Ximenez - 9351203
#Tarefa 1 - NEU - Data Science

import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from sklearn.ensemble import RandomForestRegressor





def main():
    train = pd.read_csv('train.csv').reset_index()
    train2 = pd.read_csv('train3.csv').reset_index()
    #test = pd.read_csv('test.csv')
    #features = pd.read_csv('features.csv')
    #df = pd.concat([train,test,features],axis=0) 

    #df = pd.concat([train,features],axis=0) 
    
    resposta = 1
    
    if resposta == 1:
        cont = 52
        
        inicial = 0
        array =[]
        x = []
        xn = []
        contador = 0
        train = train.groupby(by='Date').agg({'Weekly_Sales':'sum'}).reset_index()
        print('primeiramente uma regressão linear tendo em vista um mes completo, com resultados por semana. Onde há um padrão maior. pegamos o mes inicial ')

        
        
        while inicial <= 143:
            array.append(train['Weekly_Sales'][inicial])
            array.append(train['Weekly_Sales'][inicial+1])
            array.append(train['Weekly_Sales'][inicial+2])
            array.append(train['Weekly_Sales'][inicial+3])
            
            x.append(train['Date'][inicial])
            x.append(train['Date'][inicial+1])
            x.append(train['Date'][inicial+2])
            x.append(train['Date'][inicial+3])

            xn.append(contador)
            xn.append(contador+1)
            xn.append(contador+2)
            xn.append(contador+3)
            
            contador += 4
            inicial += cont
        print(array)
        pl = np.polyfit(xn,array,1)
        plt.plot(xn,array,'o')
        plt.plot(xn,np.polyval(pl,xn),'g--')
        plt.xlabel('x')
        plt.show()


    resposta = 2

    if resposta == 2:
        print('Segunda regressão linear, com todos os dados, é possivel ver uma linha de tendencia subindo')
        
        train = pd.read_csv('train.csv').reset_index()
        train['Media'] = train['Weekly_Sales']*(0.022)   #divisão de valores para se obter a média
        train = train.groupby(by='Date').agg({'Media':'sum'})
        cont = 0
        x = []
        while cont < 143:
            x.append(cont)
            cont+=1
        pl = np.polyfit(x,train['Media'],1)
        plt.plot(x,train['Media'],'o')
        plt.plot(x,np.polyval(pl,x),'g--')
        plt.xlabel('x')
        plt.show()
            

    test = train2
    print("BONUS: usando a métrica de temperatura, podemos perceber que há um maior numero de compras em temperaturas médias, diminuindo nos extremos")
    test['Media'] = test['Weekly_Sales']
    test2 = test.groupby(by='Temperature').agg({'Media':'sum'})
    print(test2)
    test2.plot.bar(legend='')
    plt.title('Vendas totais por semana')
    plt.xlabel('Temperatura')
    plt.ylabel('Vendas por semana')
    plt.xticks(rotation=45)
    plt.show()
    


        
        
        
                   
main()

