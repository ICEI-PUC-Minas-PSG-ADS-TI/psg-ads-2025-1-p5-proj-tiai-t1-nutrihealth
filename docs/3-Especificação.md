  
# 3. Especificações do Projeto

## 3.1 Classificação dos Requisitos Funcionais x Requisitos não Funcionais 

### Requisitos Funcionais


| ID     | Descrição do Requisito                                                        | Prioridade |
|--------|------------------------------------------------------------------------------|------------|
| RF-001 | Permitir que o usuário cadastre tarefas relacionadas ao planejamento de refeições | ALTA       |  
| RF-002 | Emitir um relatório de tarefas no mês, como consumo de alimentos e desperdício | ALTA      |  
| RF-003 | Permitir que o usuário cadastre os ingredientes disponíveis em casa          | ALTA       |  
| RF-004 | Sugerir receitas com base nos ingredientes cadastrados                        | ALTA       |  
| RF-005 | Gerar uma lista de compras personalizada conforme as receitas escolhidas      | MÉDIA      |  
| RF-006 | Indicar o impacto ambiental das receitas sugeridas                            | MÉDIA      |  
| RF-007 | Oferecer filtros para preferências alimentares (vegetariano, vegano, etc.)   | MÉDIA      |  
| RF-008 | Permitir que o usuário salve receitas                                        | BAIXA      |  
| RF-009 | Oferecer um modo de planejamento semanal de refeições                        | MÉDIA      |  
| RF-010 | Permitir compartilhamento de receitas                                       | BAIXA      |  

### Requisitos não Funcionais

| ID      | Descrição do Requisito                                                       | Prioridade |
|---------|-----------------------------------------------------------------------------|------------|
| RNF-001 | O sistema deve ser responsivo para rodar em um dispositivo móvel            | MÉDIA      |
| RNF-002 | Deve processar requisições do usuário em no máximo 3s                       | BAIXA      |
| RNF-003 | A interface deve ser intuitiva                                              | ALTA      |
| RNF-04 | Deve ser compatível com os principais navegadores                            | MÉDIA      |

## Restrições

|ID| Restrição                                               |
|--|---------------------------------------------------------|
|01| O software deve ser compatível com Windows, LINUX E MACOS.     |
|02| O sistema deve ser desenvolvido utilizando Python, PostgreSQL, html, css, js.|
|03| O código-fonte deve ser versionado utilizando Git e hospedado em um repositório privado. |
|04|	A interface deve ser responsiva e adaptável para dispositivos móveis e desktops.| 



## 3.2 Histórias de Usuários

|EU COMO... `PERSONA`| QUERO/PRECISO ... `FUNCIONALIDADE` |PARA ... `MOTIVO/VALOR`                 |
|--------------------|------------------------------------|----------------------------------------|
|Eu como administrador do sistema | Quero gerenciar as ações dos usuários| Para manter a organização do sistema e prevenir usos indevidos, como o envio de receitas em formatos incorretos ou publicação de spam|
|Eu como usuário do sistema | Quero cadastrar tarefas relacionadas ao planejamento de refeições           | Para organizar melhor minha alimentação                |
|Eu como usuário do sistema       | Quero visualizar meu relatório mensal                | Para acompanhar meus hábitos alimentares e melhorar meu planejamento |
|Eu como usuário do sistema       | Quero cadastrar os ingredientes disponíveis em casa           | Para facilitar a organização da minha despensa e evitar compras desnecessárias               |
|Eu como usuário do sistema       | Quero receber sugestões de receitas com base nos ingredientes que tenho disponíveis                 | Para evitar desperdícios e compras desnecessárias|
|Eu como usuário do sistema       | Quero gerar uma lista de compras personalizada conforme as receitas escolhidas                 | Para facilitar minhas compras e garantir que tenho todos os ingredientes necessários|
|Eu como usuário do sistema       | Quero visualizar o impacto ambiental das receitas sugeridas                | Para tomar decisões mais sustentáveis na minha alimentação|
|Eu como usuário do sistema       | Quero aplicar filtros de preferências alimentares                | Para visualizar apenas receitas que atendam às minhas restrições e preferências|
|Eu como usuário do sistema       | Quero salvar receitas favoritas                 | Para acessá-las facilmente sempre que precisar|
|Eu como usuário do sistema       | Quero planejar minhas refeições semanalmente dentro da plataforma                 | Para manter uma alimentação organizada|
|Eu como usuário do sistema       | Quero compartilhar receitas com amigos e familiares                 | Para trocar e explorar novas experiências culinárias|


-------------------------------------------------------------------------------------------------------------------------------------------

## Tarefas Técnicas (Tasks)

## História de Usuário: 
                  Como administrador do sistema, quero gerenciar as ações dos usuários para manter a organização do sistema e prevenir usos indevidos, como o envio de receitas em formatos incorretos ou publicação de spam.
## As tarefas técnicas referente a história:
                  Criar painel de administração: Desenvolver uma interface onde o administrador pode visualizar e gerenciar as ações dos usuários.
                  Implementar sistema de moderação: Criar lógica para detectar e sinalizar conteúdos inadequados, como spam ou formatos incorretos de receitas.
                  Criar funcionalidade de bloqueio e alerta: Permitir que o administrador possa emitir advertências ou bloquear usuários que violem as regras.
                  Criar logs de atividades: Registrar todas as ações relevantes dos usuários para auditoria e controle.



## História de Usuário: 
                   Como usuário do sistema, quero cadastrar tarefas relacionadas ao planejamento de refeições para organizar melhor minha alimentação.

## As tarefas técnicas referente a história:
                  Criar a interface de cadastro de tarefas: Implementar uma tela para adicionar, editar e remover tarefas de planejamento de refeições.
                  Criar a lógica de armazenamento: Implementar a persistência das tarefas no banco de dados.
                  Criar validação de dados: Garantir que todas as tarefas cadastradas contenham informações válidas.
                  


## História de Usuário: 
                   Como usuário do sistema, quero visualizar meu relatório mensal para acompanhar meus hábitos alimentares e melhorar meu planejamento.

## As tarefas técnicas referente a história:
                 Criar a interface de relatório: Desenvolver a tela que exibe o relatório mensal do usuário.
                 Implementar geração de relatório: Criar a lógica para calcular e exibir métricas relevantes dos hábitos alimentares do usuário.
                 Criar integração com banco de dados: Garantir que os dados do relatório sejam armazenados e recuperados corretamente.
                 



## História de Usuário: 
                 Como usuário do sistema, quero cadastrar os ingredientes disponíveis em casa para facilitar a organização da minha despensa e evitar compras desnecessárias.
                 
## As tarefas técnicas referente a história:
               Criar a interface de cadastro de ingredientes: Desenvolver uma tela para adicionar e visualizar os ingredientes cadastrados.
               Implementar banco de dados para ingredientes: Criar a estrutura de armazenamento e recuperação dos ingredientes cadastrados.
               Criar funcionalidade de atualização e remoção: Permitir que os usuários editem ou excluam ingredientes conforme necessário.


## História de Usuário: 
                  Como usuário do sistema, quero receber sugestões de receitas com base nos ingredientes que tenho disponíveis para evitar desperdícios e compras desnecessárias.

## As tarefas técnicas referente a história:
                 Criar algoritmo de sugestão de receitas: Implementar lógica que cruza os ingredientes disponíveis com receitas do banco de dados.
                 Criar a interface de sugestões de receitas: Desenvolver uma tela que exibe as sugestões ao usuário.
                 Criar integração com banco de dados: Garantir que as receitas sejam filtradas corretamente conforme os ingredientes cadastrados.




  ## História de Usuário: 
                  Como usuário do sistema, quero gerar uma lista de compras personalizada conforme as receitas escolhidas para facilitar minhas compras e garantir que tenho todos os ingredientes necessários.
                  
## As tarefas técnicas referente a história:
                Criar a interface de lista de compras: Desenvolver uma tela onde o usuário pode visualizar e gerenciar sua lista de compras.
  	            Implementar a geração automática da lista: Criar a lógica para adicionar automaticamente ingredientes das receitas escolhidas.
                Criar funcionalidade de edição: Permitir que o usuário adicione ou remova itens manualmente da lista de compras.



 ## História de Usuário: 
                 Como usuário do sistema, quero visualizar o impacto ambiental das receitas sugeridas para tomar decisões mais sustentáveis na minha alimentação.
                  
## As tarefas técnicas referente a história:
                Criar a interface de impacto ambiental: Desenvolver uma seção onde o usuário pode ver métricas ambientais das receitas.
                Implementar cálculo de impacto ambiental: Criar um algoritmo que estima a pegada ecológica dos ingredientes usados nas receitas.
                Criar integração com banco de dados: Garantir que os dados ambientais estejam armazenados e atualizados corretamente.



 ## História de Usuário: 
                Como usuário do sistema, quero aplicar filtros de preferências alimentares para visualizar apenas receitas que atendam às minhas restrições e preferências.
                  
## As tarefas técnicas referente a história:
              Criar a interface de filtros: Desenvolver um sistema onde o usuário pode selecionar preferências e restrições alimentares.
              Implementar lógica de filtragem: Criar um mecanismo que filtra receitas com base nos critérios escolhidos.
              Criar integração com banco de dados: Garantir que os filtros sejam aplicados corretamente ao buscar receitas.



 ## História de Usuário: 
               Como usuário do sistema, quero salvar receitas favoritas para acessá-las facilmente sempre que precisar.
                  
## As tarefas técnicas referente a história:
              Criar a funcionalidade de favoritos: Implementar um botão para marcar/desmarcar receitas como favoritas.
              Criar uma página de receitas favoritas: Desenvolver uma tela onde o usuário pode visualizar suas receitas salvas.
              Criar persistência de dados: Garantir que as receitas favoritas sejam armazenadas no banco de dados e recuperadas corretamente.




 ## História de Usuário: 
                Como usuário do sistema, quero aplicar filtros de preferências alimentares para visualizar apenas receitas que atendam às minhas restrições e preferências.
                  
## As tarefas técnicas referente a história:
              Criar a interface de filtros: Desenvolver um sistema onde o usuário pode selecionar preferências e restrições alimentares.
              Implementar lógica de filtragem: Criar um mecanismo que filtra receitas com base nos critérios escolhidos.
              Criar integração com banco de dados: Garantir que os filtros sejam aplicados corretamente ao buscar receitas.



 ## História de Usuário: 
                Como usuário do sistema, quero salvar receitas favoritas para acessá-las facilmente sempre que precisar.
                  
## As tarefas técnicas referente a história:
              Criar a funcionalidade de favoritos: Implementar um botão para marcar/desmarcar receitas como favoritas.
              Criar uma página de receitas favoritas: Desenvolver uma tela onde o usuário pode visualizar suas receitas salvas.
              Criar persistência de dados: Garantir que as receitas favoritas sejam armazenadas no banco de dados e recuperadas corretamente.



 ## História de Usuário: 
              Como usuário do sistema, quero compartilhar receitas com amigos e familiares para trocar e explorar novas experiências culinárias.
                  
## As tarefas técnicas referente a história:
              Criar funcionalidade de compartilhamento: Implementar um botão que gera um link ou permite envio direto por redes sociais.
              Criar controle de permissões: Definir regras para quem pode visualizar e acessar receitas compartilhadas.
              Criar integração com redes sociais: Permitir o compartilhamento direto em aplicativos como WhatsApp e Instagram.
