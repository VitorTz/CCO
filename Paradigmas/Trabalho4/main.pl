camiseta(amarela).
camiseta(azul).
camiseta(branca).
camiseta(verde).
camiseta(vermelha).


nome(camilo).
nome(elias).
nome(fernandinho).
nome(josue).
nome(marcio).


vinho(cabernet_sauvignon).
vinho(carmenere).
vinho(malbec).
vinho(merlot).
vinho(tannat).


queijo(brie).
queijo(emmenthal).
queijo(gorgonzola).
queijo(gouda).
queijo(roquefort).


hobby(acampar).
hobby(bilhar).
hobby(fotografar).
hobby(montanhismo).
hobby(pescar).


estado(mato_grosso).
estado(minas_gerais).
estado(paraiba).
estado(roraima).
estado(santa_catarina).


aEsquerda(X, Y, Lista) :- nth0(IndexX, Lista, X), nth0(IndexY, Lista, Y), IndexX < IndexY.
aDireita(X, Y, Lista) :- aEsquerda(Y, X, Lista).


aoLado(X, Y, Lista) :- nextto(X, Y, Lista);nextto(Y, X, Lista).
aoLadoEsquerda(X, Y, Lista) :- aoLado(X, Y, Lista), aEsquerda(X, Y, Lista).
aoLadoDireita(X, Y, Lista) :- aoLado(X, Y, Lista), aDireita(X, Y, Lista).


pontaDireita(X, Lista) :- last(Lista, X).
pontaEsquerda(X, [X|_]).
naPonta(X, Lista) :- pontaDireita(X, Lista) ; pontaEsquerda(X, Lista).


todosDiferentes([]).
todosDiferentes([H|T]) :- not(member(H, T)), todosDiferentes(T).


% Problema 26
% https://rachacuca.com.br/logica/problemas/degustacao-de-vinho/
solucao(S) :- 
    S = [
        degustador(Camiseta1, Nome1, Vinho1, Queijo1, Hobby1, Estado1),
        degustador(Camiseta2, Nome2, Vinho2, Queijo2, Hobby2, Estado2),
        degustador(Camiseta3, Nome3, Vinho3, Queijo3, Hobby3, Estado3),
        degustador(Camiseta4, Nome4, Vinho4, Queijo4, Hobby4, Estado4),
        degustador(Camiseta5, Nome5, Vinho5, Queijo5, Hobby5, Estado5)
    ],

    % Elias está em algum lugar à direita do degustador de camiseta Branca.
    aDireita(
        degustador(_, elias, _, _, _, _),
        degustador(branca, _, _, _, _, _),
        S
    ),
    
    % O homem que nasceu em Boa Vista está de camiseta Amarela.
    member(
        degustador(amarela, _, _, _, _, roraima),
        S
    ),
    
    % O degustador que gosta de queijo Roquefort está ao lado do que gosta de queijo Emmenthal.
    aoLado(
        degustador(_, _, _, roquefort, _, _),
        degustador(_, _, _, emmenthal, _, _),
        S
    ),
    
    % O Paraibano está na terceira posição.
    Estado3 = paraiba,
    
    % O degustador que nasceu no sul do Brasil gosta de Acampar.
    member(
        degustador(_, _, _, _, acampar, santa_catarina),
        S
    ),
    
    % Em uma das pontas está o homem que gosta de Montanhismo.
    naPonta(
        degustador(_, _, _, _, montanhismo, _),
        S
    ),
    
    % Quem está degustando o vinho tipo Tannat está ao lado de quem gosta de queijo Emmenthal.
    aoLado(
        degustador(_, _, tannat, _, _, _),
        degustador(_, _, _, emmenthal, _, _),
        S
    ),
    
    % O catarinense está exatamente à esquerda do homem que está degustando o vinho tipo Carmenere.
    aoLadoEsquerda(
        degustador(_, _, _, _, _, santa_catarina),
        degustador(_, _, carmenere, _, _, _),
        S
    ),
    
    % Márcio está degustando o vinho tipo Tannat.
    member(
        degustador(_, marcio, tannat, _, _, _),
        S
    ),
    
    % O homem que gosta de queijo Gorgonzola está ao lado do homem que gosta de Pescar.
    aoLado(
        degustador(_, _, _, gorgonzola, _, _),
        degustador(_, _, _, _, pescar, _),
        S
    ),
    
    % Ferdinando está na primeira posição.
    Nome1 = fernandinho,
    
    % O degustador de Branco está em algum lugar à esquerda do Paraibano.
    aEsquerda(
        degustador(branca, _, _, _, _, _),
        degustador(_, _, _, _, _, paraiba),
        S
    ),
    
    % Na segunda posição está o homem que está degustando o vinho tipo Merlot.
    Vinho2 = merlot,
    
    % O homem que gosta de Bilhar está ao lado do que gosta de queijo Brie.
    aoLado(
        degustador(_, _, _, _, bilhar, _),
        degustador(_, _, _, brie, _, _),
        S
    ),
    
    % O degustador de camiseta Verde está em algum lugar à esquerda do degustador que nasceu em Minas Gerais.
    aEsquerda(
        degustador(verde, _, _, _, _, _),
        degustador(_, _, _, _, _, minas_gerais),
        S
    ),
    
    % Na terceira posição está o homem que está degustando o vinho tipo Cabernet.
    Vinho3 = cabernet_sauvignon,

    % O homem de camiseta Verde está ao lado do homem que gosta de Acampar.
    aoLado(
        degustador(verde, _, _, _, _, _),
        degustador(_, _, _, _, acampar, _),
        S
    ),

    % Josué está na quinta posição.
    Nome5 = josue,

    % O degustador que gosta de Pescar está em algum lugar à direita do degustador de camiseta Azul.
    aDireita(
        degustador(_, _, _, _, pescar, _),
        degustador(azul, _, _, _, _, _),
        S
    ),

    % O homem que gosta de queijo Emmenthal está na terceira posição.
    Queijo3 = emmenthal,

    % O mato-grossense está em algum lugar à direita do degustador de camiseta Amarela.
    aDireita(
        degustador(_, _, _, _, _, mato_grosso),
        degustador(amarela, _, _, _, _, _),
        S
    ),

    % Quem gosta de Montanhismo está ao lado de quem gosta de Bilhar.
    aoLado(
        degustador(_, _, _, _, montanhismo, _),
        degustador(_, _, _, _, bilhar, _),
        S
    ),

    % Na segunda posição está o degustador que gosta de queijo Roquefort.
    Queijo2 = roquefort,

    camiseta(Camiseta1),
    camiseta(Camiseta2),
    camiseta(Camiseta3),
    camiseta(Camiseta4),
    camiseta(Camiseta5),
    todosDiferentes([Camiseta1, Camiseta2, Camiseta3, Camiseta4, Camiseta5]),

    nome(Nome1),
    nome(Nome2),
    nome(Nome3),
    nome(Nome4),
    nome(Nome5),
    todosDiferentes([Nome1, Nome2, Nome3, Nome4, Nome5]),

    vinho(Vinho1),
    vinho(Vinho2),
    vinho(Vinho3),
    vinho(Vinho4),
    vinho(Vinho5),
    todosDiferentes([Vinho1, Vinho2, Vinho3, Vinho4, Vinho5]),

    queijo(Queijo1),
    queijo(Queijo2),
    queijo(Queijo3),
    queijo(Queijo4),
    queijo(Queijo5),
    todosDiferentes([Queijo1, Queijo2, Queijo3, Queijo4, Queijo5]),

    hobby(Hobby1),
    hobby(Hobby2),
    hobby(Hobby3),
    hobby(Hobby4),
    hobby(Hobby5),
    todosDiferentes([Hobby1, Hobby2, Hobby3, Hobby4, Hobby5]),

    estado(Estado1),
    estado(Estado2),
    estado(Estado3),
    estado(Estado4),
    estado(Estado5),
    todosDiferentes([Estado1, Estado2, Estado3, Estado4, Estado5]).








