## Processamento de Transações Bancárias com PySpark, Hadoop, Databricks Azure e Flask

#### echo "Descrição" >> ####

echo "Codificação em Python de uma aplicação Flask que utiliza PySpark para processar transações bancárias. Ele foi projetado para rodar em um ambiente distribuído e é integrado com o Azure para armazenamento de dados e Databricks para processamento de big data. Usado Hadoop um framework de código aberto que permite o processamento distribuído de grandes conjuntos de dados em clusters de computadores usando modelos de programação simples." >> 

## echo "Funcionalidades" >> ####
echo "- API Flask para processamento de transações em batch e streaming." >> 
echo "- Integração com Azure Data Lake para armazenamento de dados." >> 
echo "- Utilização do PySpark para processamento distribuído de dados." >> 
echo "- Scripts de utilidade para backup, restauração e migração de dados." >> 
echo "- É o sistema de arquivos distribuído do Hadoop." >> 



## Para fazer a aplicação rodar, você precisa dos seguintes pacotes e ferramentas:
- Linguagem:
- Python, Shell, HCL e Dockerfile

- Flask: O framework web usado para criar a API.

``pip install Flask``

- Azure SDK: Para interagir com o Azure Blob Storage e outros serviços do Azure.

``pip install azure-storage-blob``

- Hadoop: Para interagir com o sistema de arquivos HDFS. Instalar separadamente e não via pip.

- Azure CLI: Ferramenta de linha de comando para gerenciar recursos do Azure. 

``curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash``

- jq: Uma ferramenta leve e flexível de linha de comando para processar JSON.

``sudo apt-get install jq``

- mrjob: Se você estiver usando MapReduce.

``pip install mrjob``

Pyspark: Se você estiver usando Spark para processamento.

``pip install pyspark``

- PostgreSQL (opcional): Se você estiver usando um banco de dados PostgreSQL em algum lugar da sua aplicação.

``pip install psycopg2``

- Databricks: Se você estiver usando a plataforma Databricks, pode precisar de bibliotecas ou SDKs específicos.

Instale o Databricks CLI usando pip:
``pip3 install databricks-cli``

- Depois de instalar o CLI, você precisa configurá-lo para se conectar à sua instância Databricks. 
Use o seguinte comando:
``databricks configure --token``

- Atualize o Pacotes:
``pip install --upgrade jinja2 markupsafe``
``pip install jinja2==2.10 markupsafe==1.1.0``

``python3 -m venv myenv``
``source venv/bin/activate``

 - Instale as dependências necessárias com
``pip install -r requirements.txt``

- Comando para rodar seria:
``python3 setup.py``

     
   
$$E=mc^2$$

Inline $$E=mc^2$$ Inline，Inline $$E=mc^2$$ Inline。

$$\(\sqrt{3x-1}+(1+x)^2\)$$
                    
$$\sin(\alpha)^{\theta}=\sum_{i=0}^{n}(x^i + \cos(f))$$
                
###FlowChart

```flow
st=>start: Login
op=>operation: Login operation
cond=>condition: Successful Yes or No?
e=>end: To admin

st->op->cond
cond(yes)->e
cond(no)->op
```

###Sequence Diagram
                    
```seq
Emerson->Brazil: Says Hello 
Note right of Brazil: Brazil thinks\nabout it 
Brazil-->Emerson: How are you? 
Emerson->>Brazil: I am good thanks!
