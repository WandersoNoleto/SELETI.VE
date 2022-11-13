## <div align="center"><img width="28px" height="28px" src="templates/static/base/study.svg"/> SELETI.VE 
   <div/>

<div align="center">
  <img width="1092px" height="534.4px" src="/readme-doc/img/main_picture.png"/><center>
<div/>

<div align="left">

  ## :computer: Sobre
<div align="justify">
&nbsp&nbsp A ideia gira em torno de uma plataforma para aqueles que buscam emprego poderem se organizar melhor. É possível cadastrar as empresas para qual deseja tentar as vagas, cadastrar detalhes e registrar a organização de seus estudos para as mesmas, assim concentrando em um único lugar as informações relacionadas à todas as vagas que está interessado ou até mesmo passando por etapas de contratação. <br>
&nbsp&nbsp O projeto foi desenvolvido durante a Pylab2022 organizado pela equipe <a href="https://pythonando.com.br/">Pythonando<a/> . O objetivo do evento era entregar uma proposta de aplicação, dar a estrutura base em HTML juntamente com sua estilização e desafiar o partipante a construir o backend com as funcionalidades propostas. 
<div/>

## :rocket: Stack utilizada

**Front-end:** HTML, CSS puro, Bootstrap

**Back-end:** Django

## :key: Variáveis de Ambiente
<div align="justify">
&nbsp&nbspA aplicação tem a funcionalidade de informar via SMS os dados do relatório de vendas 
de um determinado vendador ao número informado, utilizando-se da API da <a href="https://www.twilio.com/pt-br/">Twilio<a>. Para que o projeto funcione corretamente, você vai precisar adicionar as seguintes variáveis de ambiente:
<div/>
<br>

`SECRET_KEY`

`DEBUG`

`EMAIL_HOST_USER`

<h6>As duas primeiras são configurações base que sua aplciação deve possuir. Ao SECRET_KEY deve ser atribuído uma chave de aplicação Django. Para o EMAIL_HOST_USER basta apenas informar um email que sera usado para enviar e responder emails das empresas realacionadas às vagas. Configure isso em um arquivo .env<h6>

<div/>

## :mag_right: Preview

<div align="center">
<img width="546px" height="267px" src="/readme-doc/img/IOS_company.png"/><center>
<br>
<br>

<img width="1092px" height="534.4px" src="/readme-doc/img/add_new_vacancy.png"/><center>
<br>
<br>
<img width="1092px" height="534.4px" src="/readme-doc/img/vacancy_view.gif"/><center>
<div/>