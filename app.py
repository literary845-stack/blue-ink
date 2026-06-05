import streamlit as st
import datetime

# 1. CONFIGURAÇÃO DA PÁGINA E ESTÉTICA ACOLHEDORA (Vibe BLUe Ink)
st.set_page_config(
    page_title="BLUe Ink — Um refúgio para escritores e leitores",
    page_icon="✒️",
    layout="wide"
)

# Injeção de CSS para trazer as cores da maquete: Azul Escuro (#1B263B) e Bege/Creme (#F9F4E8)
st.markdown("""
    <style>
    .stApp {
        background-color: #F9F4E8;
        color: #1B263B;
    }
    h1, h2, h3 {
        font-family: 'Georgia', serif;
        color: #1B263B !important;
    }
    .stButton>button {
        background-color: #1B263B;
        color: #F9F4E8;
        border-radius: 8px;
        border: none;
        padding: 0.5rem 1rem;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #B08968;
        color: #F9F4E8;
    }
    .story-card {
        background-color: #FDFBF7;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #E9DCC4;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.02);
    }
    .quote-card {
        background-color: #1B263B;
        color: #F9F4E8;
        padding: 25px;
        border-radius: 15px;
        border-left: 5px solid #B08968;
        margin-bottom: 25px;
    }
    .tag {
        background-color: #1B263B;
        color: #F9F4E8;
        padding: 3px 8px;
        border-radius: 4px;
        font-size: 11px;
        text-transform: uppercase;
    }
    </style>
""", unsafe_allow_html=True)

# 2. BASE DE DADOS SIMULADA (Para o site funcionar imediatamente sem Supabase externo por enquanto)
if "stories" not in st.session_state:
    st.session_state.stories = [
        {
            "id": 1,
            "title": "O Último Trem",
            "author": "Ana Martins",
            "tag": "Mais Emocionante",
            "excerpt": "Às vezes, perdemos mais do que lugares. Perdemos versões de nós.",
            "content": "A estação estava quase vazia quando ela chegou. A chuva caía leve, como se o céu também soubesse que despedidas não precisam de fazer barulho. Ele já estava lá, encostado ao banco de madeira, olhando para os trilhos como quem tenta memorizar algo que vai embora. O anúncio ecoou no alto-falante: o último trem da noite partiria em cinco minutos...",
            "content_en": "The station was almost empty when she arrived. The rain fell lightly, as if the sky also knew that goodbyes don't need to make noise. He was already there, leaning against the wooden bench, looking at the tracks like someone trying to memorize something that is leaving. The announcement echoed on the loudspeaker: the last train of the night would leave in five minutes...",
            "rating": 4.8,
            "is_week": True
        },
        {
            "id": 2,
            "title": "Cartas que Nunca Enviei",
            "author": "Beatriz N.",
            "tag": "Melhor Escrita",
            "excerpt": "Algumas palavras nascem para serem escritas, não para serem lidas.",
            "content": "Guardei todas elas numa caixa de sapatos velha, amarradas com uma fita azul que já perdeu a cor. São relatos de outonos que passámos juntos e de promessas que o vento desfez. Escrever foi a minha única forma de não gritar o teu nome quando o silêncio desta casa se tornou demasiado pesado.",
            "content_en": "I kept them all in an old shoebox, tied with a blue ribbon that has already lost its color. They are accounts of autumns we spent together and promises that the wind broke. Writing was my only way of not screaming your name when the silence of this house became too heavy.",
            "rating": 4.9,
            "is_week": False
        }
    ]

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"user": "Juliana L.", "text": "Que história linda! Me fez lembrar de alguém que partiu."},
        {"user": "Caio Ferreira", "text": "A escrita é simplesmente incrível. Parabéns, Ana! 💙"}
    ]

# 3. BARRA DE NAVEGAÇÃO LATERAL (Menu do Site)
st.sidebar.title("✒️ BLUe Ink")
st.sidebar.markdown("*Onde as histórias encontram voz.*")
menu = st.sidebar.radio("Navegação", ["Início", "Ler Histórias", "Clube do Livro", "Escrever Nova", "Painel do BLUe"])

# 4. PÁGINA: INÍCIO
if menu == "Início":
    st.title("Bem-vindo ao BLUe ink")
    st.markdown("#### Escreve. Partilha. Pertence.")
    
    # Banner Principal com a Palavra do Dia
    st.markdown("""
        <div class='quote-card'>
            <small>PALAVRA DO DIA</small>
            <h2>SERENDIPIDADE</h2>
            <p><i>"A descoberta feliz de algo valioso quando não se estava à procura."</i></p>
            <span style='float: right; color: #B08968;'>— BLUe</span><br>
        </div>
    """, unsafe_allow_html=True)
    
    st.subheader("📚 Histórias em Destaque")
    cols = st.columns(2)
    
    for idx, story in enumerate(st.session_state.stories):
        with cols[idx % 2]:
            st.markdown(f"""
                <div class='story-card'>
                    <span class='tag'>{story['tag']}</span>
                    <h3 style='margin-top:10px;'>{story['title']}</h3>
                    <p style='color: #B08968;'>por {story['author']}</p>
                    <p>{story['excerpt']}</p>
                    <p>⭐ {story['rating']}</p>
                </div>
            """, unsafe_allow_html=True)

# 5. PÁGINA: LER HISTÓRIAS (Com botão de Tradução integrado)
elif menu == "Ler Histórias":
    st.title("Biblioteca de Contos")
    
    story_titles = [s["title"] for s in st.session_state.stories]
    selected_title = st.selectbox("Escolha uma história para ler:", story_titles)
    
    story = next(s for s in st.session_state.stories if s["title"] == selected_title)
    
    st.write("---")
    
    # Sistema de Tradução Visual
    col_t, col_l = st.columns([3, 1])
    with col_t:
        st.subheader(story["title"])
        st.caption(f"Por {story['author']} | Avaliação: ⭐ {story['rating']}")
    with col_l:
        idioma = st.selectbox("Idioma de Leitura", ["Português (Original)", "English (Tradução DeepL)"])
    
    # Alterar conteúdo com base no idioma selecionado
    if "English" in idioma:
        st.info("Tradução automática gerada e recuperada do cache.")
        st.markdown(f"<div style='font-size:18px; line-height:1.6; font-family:serif;'>{story['content_en']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div style='font-size:18px; line-height:1.6; font-family:serif;'>{story['content']}</div>", unsafe_allow_html=True)

    # Secção de Comentários e Resenhas
    st.write("---")
    st.subheader("💬 Comentários da Comunidade")
    
    for msg in st.session_state.messages:
        st.markdown(f"**{msg['user']}:** {msg['text']}")
        
    novo_comentario = st.text_input("Deixe o seu feedback:")
    if st.button("Enviar Comentário"):
        if novo_comentario:
            st.session_state.messages.append({"user": "Leitor Anónimo", "text": novo_comentario})
            st.success("Comentário adicionado!")
            st.rerun()

# 6. PÁGINA: CLUBE DO LIVRO
elif menu == "Clube do Livro":
    story_week = next((s for s in st.session_state.stories if s["is_week"]), st.session_state.stories[0])
    
    st.title("📖 Clube do Livro Semanal")
    st.write(f"Esta semana estamos todos a ler e a analisar a obra: **{story_week['title']}** de *{story_week['author']}*.")
    
    st.markdown(f"""
        <div class='story-card'>
            <h4>Sinopse da Leitura Coletiva:</h4>
            <p>"{story_week['excerpt']}"</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.subheader("💬 Fórum de Discussão Semanal")
    st.write("Deixe a sua análise sobre o Plot Twist, a escrita ou os sentimentos que a história despertou:")
    
    discussao = st.text_area("A sua análise crítica:")
    if st.button("Publicar no Fórum"):
        st.success("Análise publicada! Obrigado por participar no Clube do Livro.")

# 7. PÁGINA: ESCREVER NOVA HISTÓRIA (Para a comunidade publicar)
elif menu == "Escrever Nova":
    st.title("✒️ Espaço do Escritor")
    st.write("Partilhe a sua short story com o mundo.")
    
    novo_titulo = st.text_input("Título da História")
    novo_autor = st.text_input("Seu Nome / Pseudónimo")
    nova_categoria = st.selectbox("Categoria Principal", ["Mais Emocionante", "Melhor Escrita", "Melhor Plot Twist", "Mais Inspiradora"])
    resumo = st.text_input("Breve resumo (Excert)")
    conteudo = st.text_area("Escreva o seu conto aqui...", height=300)
    
    if st.button("Publicar História"):
        if novo_titulo and conteudo:
            nova_story = {
                "id": len(st.session_state.stories) + 1,
                "title": novo_titulo,
                "author": novo_autor if novo_autor else "Anónimo",
                "tag": nova_categoria,
                "excerpt": resumo if resumo else conteudo[:50] + "...",
                "content": conteudo,
                "content_en": "[Tradução pendente na API] " + conteudo[:50],
                "rating": 5.0,
                "is_week": False
            }
            st.session_state.stories.append(nova_story)
            st.success("Parabéns! A sua história foi publicada com sucesso no BLUe Ink.")
        else:
            st.error("Por favor, preencha o título e o conteúdo do conto.")

# 8. PÁGINA: PAINEL DO ADMIN (Exclusivo do teu Alterego BLUe)
elif menu == "Painel do BLUe":
    st.title("👑 Painel Administrativo de BLUe")
    st.write("Olá, BLUe. Aqui controlas a dinâmica do teu refúgio literário.")
    
    st.write("---")
    st.subheader("Selecção da História da Semana (Clube do Livro)")
    
    story_titles = [s["title"] for s in st.session_state.stories]
    escolha_semana = st.selectbox("Escolha o conto para a próxima semana:", story_titles)
    
    if st.button("Atualizar História da Semana"):
        for s in st.session_state.stories:
            s["is_week"] = (s["title"] == escolha_semana)
        st.success(f"O Clube do Livro foi atualizado! A história ativa agora é '{escolha_semana}'.")

    st.write("---")
    st.subheader("Métricas Básicas")
    col1, col2 = st.columns(2)
    col1.metric("Total de Histórias", len(st.session_state.stories))
    col2.metric("Membros Ativos", "1,240 leitores")