# py_maze
SI202 : Resolucao de Problemas II 
<h2>O Jogo</h2> 
<p>O nosso jogo possui um tabuleiro 11×11 disposto da seguinte forma.</p>
<img src = "https://user-images.githubusercontent.com/37659078/47247410-cb7b0080-d3d9-11e8-8755-735e6f2179b3.png"/>
<p>O seu jogador poder´a se movimentar para seis posi¸c˜oes diferentes, conforme a ﬁgura abaixo:</p>
<img src="https://user-images.githubusercontent.com/37659078/47247430-011fe980-d3da-11e8-9453-d411a635fe78.png"/>
Entretanto, algumas casas s˜ao bloqueadas. Nesse caso, vocˆe perder´a o jogo imediatamente se pisar em uma casa bloqueada. Al´em disso, vocˆe tamb´em perder´a o jogo se sair do tabuleiro.
Nas bordas do tabuleiro, algumas casas “especiais” ser˜ao consideradas sa´ıdas. Vocˆe dever´a atingir essas casas no menor tempo poss´ıvel.
2 Entrada
O seu programa receber´a como entrada, no primeiro parˆametro da linha de comando, a localiza¸c˜ao de um arquivo de conﬁgurac¸˜ao no formato “confXX.py”, onde XX pode ser “01,02,...,99” . Um arquivo de conﬁgurac¸˜ao, por exemplo, tem o seguinte formato, que ´e correspondente aos exemplos deste documento.
cat = [5, 5] blocks = [ (1,1), (1,5), (2,5), (4,5), (5,1), (5, 4), (6, 5), (8, 2) ] exits = [ (0,0), (6, 10), (9, 10), (10, 1) ] minimum = 5

Para importar um arquivo de conﬁgurac¸˜oes de nome “conf01.py” no seu c´odigo, vocˆe pode usar o seguinte trecho de c´odigo:
import importlib mod = importlib.import_module("conf01")
Da´ı, vocˆe poder´a acessar as vari´aveis com mod.cat, mod.blocks e assim por diante.
3 Sa´ıda
O seu programa dever´a invocar continuamente o comando print com alguma das strings: NE, NW, E, W, SW ou SE. Esse resultado ser´a posteriormente veriﬁcado pelo professor. Por exemplo, na entrada anterior, o seu programa dever´a gerar a seguinte sa´ıda:
SE E E E E
4 Avalia¸c˜ao
1. O seu programa receber´a score 1 em um dado tabuleiro se conseguir sair no menor nu´mero de passos.
2. O seu programa receber´a score 0 se demorar o dobro do nu´mero m´ınimo de passos para sair do tabuleiro.
3. Seja x o nu´mero m´ınimo de passos em um dado tabuleiro e k o nu´mero de passos que o seu programa demorou para sair. O seu programa receber´a score 2x−k x no tabuleiro se x < k < 2x. 4. A sua nota no primeiro trabalho ser´a a m´edia de todos os tabuleiros usados pelo professor nos testes.
