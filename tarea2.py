
import random

import pandas as pd

import matplotlib.pyplot as plt

import csv

import seaborn as sns

 

 

hostnames = []

dataset=[]

df= None

 

def set_hostnames(number_of_hosts: int) -> None:

    o_system = ['L']*4 + ['S']*3 + ['A']*2 + ['H']*1  # 40% Linux | 30% Solaris | 20% AIX | 10% HP-UX

    enviroments = ['D']*10 + ['I']*10 + ['T']*25 + ['S']*25 + ['P']*30

    alpha_country_codes = ['NOR']*6 + ['FRA']*9 + ['ITA']*16 + ['SPA']*16 + ['DEU']*23 + ['IRL']*30

    grupo_alpha = []

   

    for i in range(number_of_hosts):

        country = random.choice(alpha_country_codes)

        hostname = random.choice(o_system) + random.choice(enviroments)

        hostname += country

        grupo_alpha.append(hostname)

        hostname += str(grupo_alpha.count(hostname)).zfill(3)

        hostnames.append(hostname)

 

def get_os(hostname_code: str) -> str:

    if hostname_code.startswith('L'):

        return 'Linux'

    elif hostname_code.startswith('S'):

        return 'Solaris'

    elif hostname_code.startswith('A'):

        return 'AIX'

    elif hostname_code.startswith('H'):

        return 'HP-UX'

    else:

        return 'Unknow'

 

def get_enviroment(hostname_code: str) -> str:

    if hostname_code[1]=='D':

        return 'Development'

    elif hostname_code[1]=='I':

        return 'Integration'

    elif hostname_code[1]=='T':

        return 'Testing'

    elif hostname_code[1]=='S':

        return 'Staging'

    elif hostname_code[1]=='P':

        return 'Production'

    else:

        return 'Unknown'

 

def get_country(hostname_code: str) -> str:

    if hostname_code[2:5]=='NOR':

        return 'Norway'

    elif hostname_code[2:5]=='DEU':

        return 'Germany'

    elif hostname_code[2:5]=='ITA':

        return 'Italy'

    elif hostname_code[2:5]=='SPA':

        return 'Spain'

    elif hostname_code[2:5]=='IRL':

        return 'Ireland'

    elif hostname_code[2:5]=='FRA':

        return 'France'

    else:

        return 'Unknown'

 

def set_dataframe(numero: int) -> None:

    global df

   

    set_hostnames(numero)

   

    for hostname_code in hostnames:

        dataset.append({

            'hostname_code': hostname_code,

            'os':get_os(hostname_code),

            'enviroment': get_enviroment(hostname_code),

            'country': get_country(hostname_code),

            'numero': int(hostname_code[-3:])

        })

   

    df= pd.DataFrame(dataset)

 

set_dataframe(1500)df

df.to_csv(

    'hosts.csv',

    header=True,

    index=False

)

 

hosts_df= pd.read_csv('hosts.csv')

 

hosts_df

 

H= hosts_df.groupby(['country','enviroment']).size()

H

 

H.unstack().plot(kind='bar')

plt.show()

 

fig, ax= plt.subplots(2,2,figsize=(15,10))

df.groupby(['country','os']).size().unstack().plot(kind='barh',

ax=ax[0,0],title='type of grouped by country')

ax[0,0].legend(loc='center left',bbox_to_anchor=(1,0.5))

 

os_counts=df['os'].value_counts()

ax[0,1].pie(os_counts.values, labels=os_counts.index,autopct='%1.1f%%')

ax[0, 1].legend(title='Operating System', loc='center right', bbox_to_anchor=(1.25, 0.5))

sns.color_palette("dark")

country_counts = df['country'].value_counts()

 

sns.barplot(x=country_counts.values, y=country_counts.index, ax=ax[1, 0])

ax[1, 0].set_title('Total hosts by country')

for i, v in enumerate(country_counts.values):

    ax[1, 0].text(v + 100, i, str(v))

   

   

host_counts = df.groupby(['enviroment', 'country']).size().unstack()

host_counts.plot(kind='bar', ax=ax[1, 1])

ax[1, 1].set_title('Hosts by country grouped by environment')

ax[1, 1].set_ylabel('Number of hosts')

 

 

fig.tight_layout()