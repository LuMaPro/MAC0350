-- 1. Tabela Principal do Personagem
CREATE TABLE personagens (
    id INTEGER PRIMARY KEY,
    personagem_nome TEXT NOT NULL,
    jogador_nome TEXT NOT NULL,
    origem TEXT NOT NULL,
    classe text NOT NULL
);

-- 2. Tabela de Atributos (1 para 1)
CREATE TABLE atributos (
    id INTEGER PRIMARY KEY,
    personagem_id INTEGER NOT NULL,
    força INTEGER DEFAULT 0,
    agilidade INTEGER DEFAULT 0,
    inteligencia INTEGER DEFAULT 0,
    vigor INTEGER DEFAULT 0,
    presença INTEGER DEFAULT 0,
    FOREIGN KEY (personagem_id) REFERENCES personagens(id) ON DELETE CASCADE
);

-- 3. Tabela de Saúde (1 para 1)
CREATE TABLE saude (
    id INTEGER PRIMARY KEY,
    personagem_id INTEGER NOT NULL,
    pv TEXT DEFAULT '0/0',
    san TEXT DEFAULT '0/0',
    pe TEXT DEFAULT '0/0',
    FOREIGN KEY (personagem_id) REFERENCES personagens(id) ON DELETE CASCADE 
);

-- 4. Tabela de Defesa (1 para 1)
CREATE TABLE defesa (
    id INTEGER PRIMARY KEY,
    personagem_id INTEGER NOT NULL,
    passiva INTEGER DEFAULT 0,
    bloqueio INTEGER DEFAULT 0,
    esquiva INTEGER DEFAULT 0,
    FOREIGN KEY (personagem_id) REFERENCES personagens(id) ON DELETE CASCADE 
);

-- 5. Tabela de Perícias (1 para 1)
CREATE TABLE pericias (
    id INTEGER PRIMARY KEY,
    personagem_id INTEGER NOT NULL,
    atletismo INTEGER DEFAULT 0,
    atualidades INTEGER DEFAULT 0,
    ciencia INTEGER DEFAULT 0,
    diplomacia INTEGER DEFAULT 0,
    enganacao INTEGER DEFAULT 0,
    fortitude INTEGER DEFAULT 0,
    furtividade INTEGER DEFAULT 0,
    ilusionismo INTEGER DEFAULT 0,
    intimidacao INTEGER DEFAULT 0,
    intuicao INTEGER DEFAULT 0,
    investigacao INTEGER DEFAULT 0,
    luta INTEGER DEFAULT 0,
    medicina INTEGER DEFAULT 0,
    ocultismo INTEGER DEFAULT 0,
    percepcao INTEGER DEFAULT 0,
    pilotagem INTEGER DEFAULT 0,
    pontaria INTEGER DEFAULT 0,
    profissao INTEGER DEFAULT 0,
    reflexos INTEGER DEFAULT 0,
    religiao INTEGER DEFAULT 0,
    tatica INTEGER DEFAULT 0,
    tecnologia INTEGER DEFAULT 0,
    vontade INTEGER DEFAULT 0,
    FOREIGN KEY (personagem_id) REFERENCES personagens(id) ON DELETE CASCADE
);

-- 6. Tabela de Habilidades (1 para Muitos)
CREATE TABLE habilidades (
    id INTEGER PRIMARY KEY,
    personagem_id INTEGER NOT NULL,
    nome TEXT NOT NULL,
    descricao TEXT NOT NULL,
    dano TEXT NOT NULL,
    efeito TEXT NOT NULL,
    FOREIGN KEY (personagem_id) REFERENCES personagens(id) ON DELETE CASCADE
);

-- 7. Tabela de Itens (1 para Muitos)
CREATE TABLE itens (
    id INTEGER PRIMARY KEY,
    personagem_id INTEGER NOT NULL,
    nome TEXT NOT NULL,
    descricao TEXT NOT NULL,
    quantidade TEXT NOT NULL,
    FOREIGN KEY (personagem_id) REFERENCES personagens(id) ON DELETE CASCADE
);