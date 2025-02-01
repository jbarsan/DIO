
# DIO | Repositório de apoio

Repositório para armazenar arquivos dos cursos da [Digital Innovation One](https://www.dio.me).


## 📚 Documentação
- [Documentação Python](https://docs.python.org/pt-br/3.12/);
- [Documentação Git](https://git-scm.com/doc);
- [Documentação GitHub](https://docs.github.com/pt);

## 🐍 Resumo comandos Python
| Aulas | Resumo |
| ----- | ------ |

## 📖 Resumo comandos Git e GitHub
| Aulas | Resumo |
| ------| ------ |
| Listar todas as informações de configurações do Git | ``` git global <ENTER> ``` |
| Configurando informações globais de nome do usuário | ``` git config --global user.name "nome-do-usuario" ``` |
| Configurando informações globais de email do usuário |  ```git config --global user.email endereco-do-email```|
| Verificar se as informações foram adicionadas com sucesso | Digite o comando ``` git config ``` seguido das opções que deseja visualizar. Ex.: ```git config user.name <ENTER> ``` |
| Configurando a branch padrão | ``` git config --global init.defaultBranch main ``` |
| Alterando o editor padrão | ``` git config --global core.editor nome-do-editor ``` |
| Escolhend uma maneira de lidar com a falta de sincronia entre o código presente na branch remota e na branch local | ``` git config --global pull.ff only ``` Ativando o processo que chamamos de “fast-forward merge” |
| Listar todas as configurações aplicadas ao Git | ``` git config --list --show-origin ``` |
| Criando um Repositório local | ``` git init ``` |
| Ignorando pastas e/ou arquivos no repositório | Crie o arquivo **.gitignore** na raíz do projeto e adicione as pastas ou arquivos que não deseja versionar |
| Reconhecendo diretórios vazios | Adicione um arquivo **.gitkeep** dentro da pasta vazia |
| Vinculando Repositório local com o Repositório remoto | ``` git remote add origin URL ``` |
| Clonando um Repositório remoto | ``` git clone URL ``` |
| Clonando um Repositório remoto alterando o nome | ``` git clone URL nome-do-repositorio-local ``` |
| Clonando uma branch específica | ``` git clone URL --branch nome-da-branch --single-branch ``` |
| Visualizando as alterações nos arquivos | ``` git status ``` |
| Incluindo arquivos específicos em um commit | ``` git add <arquivo> ``` |
| Incluindo todos os arquivos em um commit | ``` git add . ``` |
| **O git não lista pastas vazias** | ``` git status ``` não lista pastas vazias |
| Comitando as alterações no repositório | ``` git commit -m "Mensagem" ``` |
| Visualizando os logs do commit | ``` git log ``` |
| Visualizando os logs do commit de forma mais detalhada | ``` git reflog ``` |
| Alterando da branch **master** para a branch **main**. Somente se durante a criação do repositório o nome do branch for master | ``` git branch -M main ``` |
| Subindo o primeiro commit (_-u_ é uma abreviação para _--set-upstream_) | ``` git push -u origin main ``` Considerando que main é a branch principal |
| Excluíndo o versionamento de um diretório | Exclua o arquivo **.git** da pasta raíz |
| Restaurar um arquivo para o estado anterior | ``` git restore <ARQUIVO> ``` |
| Alterar mensagem do último commit | ``` git commit --amend -m "Nova Mensagem" ``` |
| Outra forma de alterar a mensagem do último commit | ``` git commit --amend <ENTER> ``` Será aberto o editor de texto e então altere a mensagem desejada. |
| Restaurar um commit para um estado anterior (--soft). Retorna os arquivos para a stage area anterior | ``` git reset --soft <HASH-DO-COMMIT> ``` O Hash pode ser adquirido como comando ``` git log ``` |
| Restaurar um commit para um estado anterior (--mixed). Retorna para a área de trabalho (untracked files). É o comportamento padrão do git reset | ``` git reset --mixed <HASH-DO-COMMIT> ``` ou somente ``` git reset <HASH-DO-COMMIT ``` > |
| Restaurar um commit para o estado anterior que desejar (--hard). Retorna para o status do commit que deseja. Apaga todos os commits anteriores | ``` git reset --hard <HASH-DO-COMMIT> ``` |
| Removendo arquivos da área de preparação | ``` git reset <NOME-DO-ARQUIVO> ``` ou ``` git restore --staged <NOME-DO-ARQUIVO> ``` |
| Atualizando o repositório local com as alterações do repositório remoto | ``` git pull ``` |
| Listando as branchs disponíveis | ``` git branch <ENTER> ``` |
| Criando uma nova branch e alterna para a nova | Comando recomendado ```git switch -c <NOME-DO-BRANCH> ``` ou ``` git checkout -b <NOME-DO-BRANCH> ``` |
| Alterando entre as branchs existentes | Comando recomendado ``` git switch <NOME-DO-BRANCH> ``` ou ``` git checkout <NOME-DO-BRANCH> ``` |
| Listando o último commit de cada branch | ``` git branch -v ``` |
| Mesclando alterações entre as branchs. Entre na branch que deseja ter as alterações e mescladas e dê o seguinte comando | ``` git merge <NOME-DA-BRANCH-QUE-DESEJA-MESCLAR> ``` Ex.: Entre na branch main e mescle as alterações da branch dev-login ``` git merge dev-login ```|
| Para permitir que o Git faça o merge de dois projetos com históricos diferentes, é só passar o parâmetro --allow-unrelated-histories quando for fazer o pull | ``` git pull origin <BRANCH> --allow-unrelated-histories ``` |
| Apagar uma branch existente | ``` git branch -d <NOME-DO-BRANCH> ``` |
| Comparar e verificar os arquivos em branchs diferentes | ``` git diff <BRANCH-LOCAL> origin/<BRANCH-REMOTA> ``` |
| Quando quiser registrar o estado atual do diretório de trabalho e do índice, mas queira retornar para um diretório de trabalho limpo (arquivar modificações) | ``` git stash ``` |
| Listar as modificações arquivas com o ``` git stash ``` | ``` git stash list ``` |
| Inspencionar as alterações armazenadas | ``` git stash show ``` |
| Restaurar (potencialmente em cima de um commit diferente) modificações | ``` git stash apply ``` |
