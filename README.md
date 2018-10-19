# py_maze
SI202 : Resolucao de Problemas II 
<h2>O Jogo</h2> 
<p>O nosso jogo possui um tabuleiro 11×11 disposto da seguinte forma.</p>
<img src = "https://user-images.githubusercontent.com/37659078/47247410-cb7b0080-d3d9-11e8-8755-735e6f2179b3.png"/>
<p>O seu jogador poderá se movimentar para seis posições diferentes, conforme a ﬁgura abaixo:</p>
<img src="https://user-images.githubusercontent.com/37659078/47247430-011fe980-d3da-11e8-9453-d411a635fe78.png"/>
<p>Entretanto, algumas casas são bloqueadas. Nesse caso, você perderá o jogo imediatamente se pisar em uma casa bloqueada. Além disso, você também perderá o jogo se sair do tabuleiro.</p>
<img src="https://user-images.githubusercontent.com/37659078/47247437-0e3cd880-d3da-11e8-80f8-6b9e12fcbb72.png"/>
<p>Nas bordas do tabuleiro, algumas casas “especiais” serão consideradas saídas. Você deverá atingir essas casas no menor tempo possível.<p>
<h2>Entrada</h2>
<p>
O seu programa receberá como entrada, no primeiro parâmetro da linha de comando, a localização de um arquivo de conﬁguração no formato <b>“confXX.py”</b>, onde <b>XX</b> pode ser “01,02,...,99” . Um arquivo de conﬁguração, por exemplo, tem o seguinte formato, que é correspondente aos exemplos deste documento.
</p>

<p>
<b>cat</b> = [5, 5] <br />
<b>blocks</b> = [ (1,1), (1,5), (2,5), (4,5), (5,1), (5, 4), (6, 5), (8, 2) ]<br /> 
<b>exits</b> = [ (0,0), (6, 10), (9, 10), (10, 1) ] <br />
<b>minimum</b> = 5
</p>

<p>Para importar um arquivo de conﬁgurações de nome “conf01.py” no seu código, você pode usar o seguinte trecho de código:</p>
<p>
<b>import</b> importlib <br />
<b>mod</b> = importlib.import_module("conf01")
</p>
<p>Daí, você poderá acessar as variáveis com mod.cat, mod.blocks e assim por diante.</p>

<h2>Saída</h2>
<p>O seu programa deverá invocar continuamente o comando print com alguma das strings: NE, NW, E, W, SW ou SE. Esse resultado será posteriormente veriﬁcado pelo professor. Por exemplo, na entrada anterior, o seu programa deverá gerar a seguinte saída:</p>
<p>
SE<br />E<br />E<br />E<br />E
</p>
<h2>Avaliação</h2>
<p>1. O seu programa receberá score 1 em um dado tabuleiro se conseguir sair no menor número de passos.</p>
<p>2. O seu programa receberá score 0 se demorar o dobro do número mínimo de passos para sair do tabuleiro.</p>
<p>3. Seja x o número mínimo de passos em um dado tabuleiro e k o nu´mero de passos que o seu programa demorou para sair. O seu programa receberá score (2x−k)/x no tabuleiro se x < k < 2x.</p>
<p>4. A sua nota no primeiro trabalho será a média de todos os tabuleiros usados pelo professor nos testes.</p>
