#João Vitor Dias Ximenez - 9351203
#Tarefa 1 - NEU - Data Science

import pandas as pd
from matplotlib import pyplot as plt



def main():
    train = pd.read_csv('train.csv')
    resposta = 10
    while resposta != 0:
        resposta = int(input("Boa tarde, digite o número do exercício que quer resolver\n1-Exercicio 1\n2-Exercicio 2\n3-Exercicio 3\n4-Exercicio 4\nResposta:  "))
        if resposta == 1:
            print('Tarefa 1:')
            print("O gráfico de barras é o melhor, pois mostra a variação dos valores com o tempo. Como o resultado de vendas não esta necessariamente ligado ao resultado das vendas anteriores, um grafico de dispersão ou curva não se adequaria")
            train['Media'] = train['Weekly_Sales']*(0.022)   #divisão de valores para se obter a média
            train.groupby(by='Date').agg({'Media':'sum'} ).plot.bar(legend='', fontsize=3)
            plt.title('Vendas totais por semana')
            plt.xlabel('Data')
            plt.ylabel('Vendas por semana')
            plt.xticks(rotation=45)
            plt.show()
            

            
            
        if resposta == 2:   
            print('Tarefa 2')
            train2 = train.groupby(by='Store').agg({'Weekly_Sales':'sum'})
            train2 = train2.sort_values(by='Weekly_Sales',ascending=False)

            train2.head(10).plot.bar(legend='')
            plt.title('Melhores lojas')
            plt.xlabel('Lojas')
            plt.ylabel('Vendas no periodo')
            plt.xticks(rotation=45)
            plt.show()

            train2 = train2.sort_values(by='Weekly_Sales',ascending=False).reset_index()


            
            array = []
            for i in range(10):
                array.append(train2['Store'][i])
            print("\n Lojas que tiveram maior performance: ")
            print(array)
            print("\n Para evitar a poluição dos dados, o grafico de cada uma das lojas pode ser visto na função abaixo, separadamente")
            graf = int(input('de 1 a 10, qual grafico gostaria de ver?  '))
            while graf > 0 and graf < 11:
                train.groupby(by='Date').agg({'Weekly_Sales':'sum'}).plot.bar(legend='')
                filtro = train['Store'] == train2['Store'][graf-1]
                train3 = train[filtro].groupby(by='Date').agg({'Weekly_Sales':'sum'}).plot.bar(legend='')
                plt.xlabel('Data')
                plt.ylabel('Vendas por semana')
                plt.xticks(rotation=45)
                plt.show()
                graf = int(input('de 1 a 10, qual grafico gostaria de ver?  '))  
            


        if resposta == 3:

            print('Tarefa 3')
            train2 = train.groupby(by='Store').agg({'Weekly_Sales':'sum'})
            train2 = train2.sort_values(by='Weekly_Sales',ascending=True)

            train2.head(10).plot.bar(legend='')
            plt.title('Melhores lojas')
            plt.xlabel('Lojas')
            plt.ylabel('Vendas no periodo')
            plt.xticks(rotation=45)
            plt.show()

            train2 = train2.sort_values(by='Weekly_Sales',ascending=False).reset_index()


            
            array = []
            for i in range(10):
                array.append(train2['Store'][i])
            print("\n Lojas que tiveram pior performance: ")
            print(array)
            print("\n Para evitar a poluição dos dados, o grafico de cada uma das lojas pode ser visto na função abaixo, separadamente")
            graf = int(input('de 1 a 10, qual grafico gostaria de ver?  '))
            while graf > 0 and graf < 11:
                train.groupby(by='Date').agg({'Weekly_Sales':'sum'})
                filtro = train['Store'] == train2['Store'][graf-1]
                train3 = train[filtro].groupby(by='Date').agg({'Weekly_Sales':'sum'}).plot.bar(legend='')
                plt.xlabel('Data')
                plt.ylabel('Vendas por semana')
                plt.xticks(rotation=45)
                plt.show()
                graf = int(input('de 1 a 10, qual grafico gostaria de ver?  '))



            print('Tarefa 3:')
            df2 = train.groupby(by='Date').mean()
            plt.bar(df2.index,df2['Weekly_Sales'],label='Vendas Totais por data')
            plt.xticks(rotation=45)
            plt.title('Vendas totais por semana')
            plt.legend()
            plt.show()

            print("Comparação entre os graficos de maior e menos performance: ")
            train2 = train.groupby(by='Store').agg({'Weekly_Sales':'sum'})
            train2 = train2.sort_values(by='Weekly_Sales',ascending=False)
            train3 = train.groupby(by='Store').agg({'Weekly_Sales':'sum'})
            train3 = train3.sort_values(by='Weekly_Sales',ascending=True)
            df2 = train2.head(10)
            df3 = train3.head(10)
            plt.bar(df2.index,df2['Weekly_Sales'],label='Melhores')
            plt.bar(df3.index,df3['Weekly_Sales'],label='Piores')

            
            plt.title('Melhores e piores lojas')
            plt.xlabel('Lojas')
            plt.ylabel('Vendas no periodo')
            plt.xticks(rotation=0)
            plt.legend()
            plt.show()

            
            

        if resposta == 4:
            

            filtro = train['IsHoliday'] == False
            filtro2 = train['IsHoliday'] == True
            train3 = train[filtro].groupby(by='Date').agg({'Weekly_Sales':'sum'})
            train4 = train[filtro2].groupby(by='Date').agg({'Weekly_Sales':'sum'})
            train5 = train.groupby(by='IsHoliday').agg({'Weekly_Sales':'sum'}).reset_index()
            
            cferiado = train5['Weekly_Sales'][0]/train3.shape[0]
            sferiado = train5['Weekly_Sales'][1]/train4.shape[0]
            print('Media por semana sem feriado', sferiado)
            print('Media por semana com feriado', cferiado,train4.shape[0])
            print(cferiado/sferiado*100,'%')
            plt.bar(['Com Feriado','Sem Feriado'],[cferiado,sferiado])
            print('A princípio, os feriados afetam positivamente nas vendas')
            train3 = train[filtro].groupby(by='Date').agg({'Weekly_Sales':'median'})
            train4 = train[filtro2].groupby(by='Date').agg({'Weekly_Sales':'median'})
            print('Mediana por semana sem feriado', train5['Weekly_Sales'][0])
            print('Mediana por semana com feriado',train5['Weekly_Sales'][1] )

            
            plt.show()
            
            df2 = train3
            df3 = train4
            plt.bar(df3.index,df3['Weekly_Sales'],label='Sem Feriado')
            plt.bar(df2.index,df2['Weekly_Sales'],label='Feriado')

            
            plt.title('Melhores e piores lojas')
            plt.xlabel('Lojas')
            plt.ylabel('Vendas no periodo')
            plt.xticks(rotation=45)
            plt.legend()
            plt.show()
            
           
            
                
            


            
            #filtro = train.groupby(by=['IsHoliday'].agg({'Weekly_Sales':'sum'})
            #train2 = train2.sort_values(by='Weekly_Sales',ascending=True)

            print('Tarefa 4:')

            
            
            
                       
main()

