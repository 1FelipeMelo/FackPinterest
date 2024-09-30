# FakePinterest

**Descrição:**
Uma recriação simplificada do Pinterest, desenvolvida com Flask como backend e HTML/CSS para a interface. O objetivo deste projeto é explorar os conceitos de redes sociais e desenvolvimento web. Com ele, você pode fazer postagens de imagens, no Feed pode visualizar as imagens dos outros usuários, e até mesmo acessar o perfil. O proprietário também pode deletar fotos do seu perfil.

## **Funcionalidades:**

* **✅Criar conta:** Novos usuários podem se registrar e criar um perfil.
![Captura de tela 2024-09-30 153817](https://github.com/user-attachments/assets/265e4fc6-7abe-4a53-9fe4-aa42610a85da)
Ao acessar a página, você vai se deparar com a página de login, mas caso não seja cadastrado, pode clicar em: 'Não tem uma conta? Crie aqui.'

* **✅Postagens:** Usuários podem adicionar imagens ao seu perfil.
  Essa funcionalidade aparece apenas se estiver dentro do perfil.
![1](https://github.com/user-attachments/assets/a34d9206-db15-43cf-87bf-6d5776353cf6)

* **✅Deletar Postagens:** Remova imagens do seu perfil a qualquer momento.
![2](https://github.com/user-attachments/assets/fef10c0d-f20e-4d4d-83af-591debcb9a94)

* **✅Feed:** Janela onde exibe todas as imagens postadas por outros usuários.
  Consegue acessar o Feed através do botão 'FakePinterest' localizado no canto superior esquerdo.
![3](https://github.com/user-attachments/assets/dedd5182-5def-4390-b845-aebb536f7a0e)

* **✅Visitas em Perfis:** O usuário pode visitar outros perfis cadastrados.
  Dentro do Feed, pode expandir a imagem e, ao expandi-la, vai exibir o botão 'Perfil do Usuário'. Basta clicar e será redirecionado.
![1](https://github.com/user-attachments/assets/79c9155b-e054-4acb-9820-b366abceae0b)

* **✅Sair:** A qualquer momento, o usuário pode fazer logoff e sair de sua conta.
  O botão está localizado no canto superior esquerdo.
![2](https://github.com/user-attachments/assets/fc3c1b79-9d18-46a8-9097-2e1284456726)

**Tecnologias Utilizadas:**

* **Flask:** Framework web para Python, destinado ao backend.
* **HTML/CSS:** Organização e personalização da parte visual do site.
* **SQLite:** Criado com o flask_sqlalchemy, uma extensão do Flask.

# **Como Usar:**

### 1- Executar o arquivo 'criar_banco.py' para criar o Banco de Dados. 
Obs: Ao baixar os arquivos, já vem com um banco de dados configurado, contendo imagens para visualização do projeto. Execute 'criar_banco.py' caso deseje começar do zero.

### 2- Executar o arquivo 'main.py'. Ele vai iniciar o programa. Basta acessar o endereço inserido no terminal.

### 3- Dentro do navegador, o endereço vai redirecionar para a página de login. Basta criar uma conta ou inserir os dados cadastrados. A senha deve conter de 6 a 20 caracteres.

1. **Copiar repositório:**
   ```bash
   git clone 1FelipeMelo/FakePinterest
