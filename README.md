🚀 Nome do Projeto: [FNaF em Terminal]

Dupla (Equipe):

Integrante 1: [Everton]

Integrante 2: [Gustavo]


🎯 1. Visão do Produto

O programa resolve o problema de criar uma experiência de jogo de terror simples e interativa usando apenas o terminal, permitindo que o jogador tome decisões rápidas para sobreviver até o final da noite.

📦 2. MVP

As 3 funcionalidades principais são:

Sistema de energia
A energia diminui conforme o jogador usa câmeras e portas.

Sistema de câmeras
O jogador pode verificar onde os animatronics estão.

Sistema de sobrevivência
O jogador precisa sobreviver até 6AM sem deixar os animatronics chegarem.

🚫 3. Fora de Escopo

O sistema não vai ter:

interface gráfica;
imagens ou animações;
multiplayer;
mapa muito grande;
inteligência artificial muito complexa;
salvamento online;
sons obrigatórios.

⚙️ 4. Arquitetura e Lógica
Variáveis

O sistema precisa guardar:

energia
hora
porta_esquerda
porta_direita
local_animatronic
jogador_vivo
camera_atual

Condicionais

O sistema usa if/else para decidir:

se a energia acabou;
se o jogador sobreviveu até 6AM;
se a porta está aberta ou fechada;
se o animatronic atacou;
se o comando digitado é válido;
se o jogador venceu ou perdeu.

Loops

O sistema usa while para repetir a noite até:

o jogador vencer;
o jogador perder;
a energia acabar.

Também pode usar for para:

mostrar câmeras;
contar tempo;
exibir mensagens com efeito de digitação.

🗺️ 5. Fluxo do Usuário

O usuário abre o programa e vê a tela inicial com o nome do jogo.

Depois:

escolhe iniciar a noite;
recebe instruções básicas;
vê a hora atual, energia e opções;
escolhe entre olhar câmeras, fechar portas ou esperar;
os animatronics se movimentam;
o sistema verifica se houve ataque;
o ciclo se repete até 6AM;
se sobreviver, aparece mensagem de vitória;
se perder, aparece mensagem de jumpscare/game over.