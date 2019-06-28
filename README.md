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
<img src="https://user-images.githubusercontent.com/37659078/47247442-1563e680-d3da-11e8-8efc-3ff97afc456f.png"/>
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
<img src="https://user-images.githubusercontent.com/37659078/47247449-1f85e500-d3da-11e8-9882-672486432747.png"/>
