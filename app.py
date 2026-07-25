
from pathlib import Path
from urllib.parse import quote
import streamlit as st

BASE_DIR = Path(__file__).parent
ASSETS_DIR = BASE_DIR / "assets"
WHATSAPP_NUMBER = "50938058311"
DEFAULT_MESSAGE = "Bonjour M. Absolu, je souhaite obtenir plus d'informations sur vos services."
DEFAULT_WHATSAPP_URL = f"https://wa.me/{WHATSAPP_NUMBER}?text={quote(DEFAULT_MESSAGE)}"

st.set_page_config(
    page_title="Comptabilité pour les non-comptables",
    page_icon="📘",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
        .stApp {
            background: linear-gradient(180deg, #f7f9fc 0%, #eef3f8 100%);
        }
        .hero-box {
            background: linear-gradient(135deg, #0f2742 0%, #1d4d7a 100%);
            border-radius: 24px;
            padding: 2rem;
            color: white;
            box-shadow: 0 15px 35px rgba(15, 39, 66, 0.18);
            margin-bottom: 1rem;
        }
        .hero-box h1 {
            margin: 0;
            font-size: 2.7rem;
            line-height: 1.12;
        }
        .hero-box p {
            margin-top: 0.9rem;
            font-size: 1.08rem;
            opacity: 0.96;
        }
        .gold { color: #f6c453; font-weight: 800; }
        .small-card {
            background: white;
            border-radius: 18px;
            padding: 1.2rem;
            border: 1px solid #dfe7ef;
            box-shadow: 0 7px 22px rgba(30, 55, 80, 0.07);
            height: 100%;
        }
        .small-card h3 {
            color: #173f63;
            margin-top: 0;
        }
        .value-box {
            background: #ffffff;
            border-left: 6px solid #1e73a1;
            border-radius: 14px;
            padding: 1rem 1.2rem;
            box-shadow: 0 5px 18px rgba(30, 55, 80, 0.06);
            margin: 0.8rem 0;
        }
        .section-title {
            color: #0f2742;
            font-weight: 800;
            margin-top: 0.3rem;
        }
        .footer {
            text-align: center;
            color: #617181;
            padding: 2rem 0 1rem;
            font-size: 0.92rem;
        }
        section[data-testid="stSidebar"] {
            background: #0f2742;
        }
        section[data-testid="stSidebar"] * {
            color: white;
        }

        .trust-strip {
            background: #0f2742;
            color: white;
            padding: 1rem 1.2rem;
            border-radius: 16px;
            margin: 1rem 0 1.4rem;
        }
        .prototype {
            background: white;
            border: 1px dashed #8fa9bb;
            border-radius: 17px;
            padding: 1.2rem;
            height: 100%;
        }
        .wa-float {
            position: fixed;
            right: 22px;
            bottom: 22px;
            background: #22a45d;
            color: white !important;
            padding: 13px 18px;
            border-radius: 999px;
            text-decoration: none !important;
            font-weight: 800;
            box-shadow: 0 10px 25px rgba(20,110,60,.30);
            z-index: 9999;
        }
        div[data-testid="stMetric"] {
            background: white;
            border: 1px solid #dfe7ef;
            padding: .9rem;
            border-radius: 15px;
            box-shadow: 0 5px 16px rgba(30,55,80,.06);
        }
        @media (max-width: 720px) {
            .hero-box { padding: 1.35rem; }
            .hero-box h1 { font-size: 2.05rem; }
            .wa-float { right: 12px; bottom: 12px; padding: 11px 14px; }
        }
        .contact-box {
            background: white;
            border-radius: 18px;
            padding: 1.2rem 1.35rem;
            border: 1px solid #dfe7ef;
            box-shadow: 0 7px 22px rgba(30, 55, 80, 0.07);
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f'<a class="wa-float" href="{DEFAULT_WHATSAPP_URL}" target="_blank">💬 WhatsApp</a>',
    unsafe_allow_html=True,
)

with st.sidebar:
    st.markdown("## 📘 Absolu — Comptable")
    st.caption("Le Comptable Absolu • Formation • Solutions digitales")
    page = st.radio(
        "Navigation",
        [
            "Accueil",
            "À propos",
            "Formations",
            "Services comptables",
            "Systèmes & sites personnalisés",
            "Outils gratuits",
            "Portfolio",
            "Pourquoi me choisir",
            "Demander un devis",
            "Contact",
        ],
    )
    st.divider()
    st.write("**Téléphone / WhatsApp**")
    st.write("+509 38 05 8311")
    st.link_button("Écrire sur WhatsApp", DEFAULT_WHATSAPP_URL, use_container_width=True)

st.markdown(
    """
    <div class="hero-box">
        <h1>Comptabilité pour les non-comptables</h1>
        <p>Je suis <span class="gold">Absolu</span>, comptable et créateur de la marque <b>Le Comptable Absolu</b>. Je vous aide à apprendre la comptabilité et à structurer vos besoins comptables, administratifs et digitaux.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

if page == "Accueil":
    col1, col2 = st.columns([1.25, 1])
    with col1:
        st.markdown("### Un espace pensé pour apprendre et passer à l’action")
        st.write(
            "Je m’appelle Absolu et je suis comptable. Je vous accompagne pour comprendre la comptabilité, "
            "structurer vos opérations et mettre en place des outils adaptés à votre activité."
        )
        st.markdown(
            """
            <div class="value-box">
                <b>Ce que je propose :</b><br>
                • des contenus pédagogiques simples ;<br>
                • des services comptables et administratifs ;<br>
                • des tableaux, systèmes et sites personnalisés pour entreprises.
            </div>
            """,
            unsafe_allow_html=True,
        )
        cta1, cta2 = st.columns(2)
        with cta1:
            st.link_button("Demander un service", DEFAULT_WHATSAPP_URL, use_container_width=True)
        with cta2:
            st.link_button("Appeler / WhatsApp", DEFAULT_WHATSAPP_URL, use_container_width=True)
    with col2:
        st.image(str(ASSETS_DIR / "hero_banner.png"), use_container_width=True)

    st.markdown("### Mes principaux domaines d’intervention")
    a, b, c = st.columns(3)
    with a:
        st.markdown(
            """
            <div class="small-card">
                <h3>📚 Formation</h3>
                <p>Initiation à la comptabilité, explications accessibles, accompagnement des étudiants et non-comptables.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with b:
        st.markdown(
            """
            <div class="small-card">
                <h3>📊 Comptabilité</h3>
                <p>Suivi des opérations, conciliation bancaire, états financiers, tableaux Excel et appui administratif.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c:
        st.markdown(
            """
            <div class="small-card">
                <h3>💻 Solutions digitales</h3>
                <p>Création de systèmes et sites web personnalisés pour mieux gérer l’information dans votre entreprise.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )


    st.markdown(
        """
        <div class="trust-strip">
            ✓ Explications accessibles &nbsp;&nbsp; • &nbsp;&nbsp;
            ✓ Outils pratiques &nbsp;&nbsp; • &nbsp;&nbsp;
            ✓ Accompagnement personnalisé &nbsp;&nbsp; • &nbsp;&nbsp;
            ✓ Contact direct sur WhatsApp
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### Pour qui ?")
    p1, p2, p3, p4 = st.columns(4)
    publics = [
        (p1, "👤 Particuliers", "Comprendre et mieux organiser leurs finances."),
        (p2, "🎓 Étudiants", "Renforcer les bases comptables et pratiquer."),
        (p3, "🏪 Entrepreneurs", "Suivre l’activité et mieux décider."),
        (p4, "🏢 Entreprises", "Structurer et digitaliser certains processus."),
    ]
    for col, titre, texte in publics:
        with col:
            st.markdown(
                f'<div class="small-card"><h3>{titre}</h3><p>{texte}</p></div>',
                unsafe_allow_html=True,
            )


elif page == "À propos":
    st.markdown("### À propos de moi")
    a1, a2 = st.columns([1.2, 1])
    with a1:
        st.write("Je suis Absolu, comptable et créateur de la marque professionnelle « Le Comptable Absolu ». À travers cette plateforme, je rends la comptabilité plus accessible et je propose des solutions pratiques de gestion aux particuliers, étudiants, entrepreneurs et entreprises.")
        st.markdown("""
        **Domaines d’intervention :**
        - comptabilité générale et suivi des opérations ;
        - conciliation bancaire ;
        - tableaux Excel et reporting ;
        - accompagnement administratif ;
        - initiation aux outils comptables ;
        - création de sites et systèmes simples sur mesure.
        """)
        st.info("Mission : rendre la comptabilité plus compréhensible et aider les organisations à utiliser de meilleurs outils de suivi.")
    with a2:
        st.markdown("""
        <div class="contact-box">
            <h3 class="section-title">Valeurs professionnelles</h3>
            <p><b>Rigueur</b> — travailler avec méthode et précision.</p>
            <p><b>Clarté</b> — expliquer sans jargon inutile.</p>
            <p><b>Confidentialité</b> — respecter les informations du client.</p>
            <p><b>Utilité</b> — proposer des outils réellement exploitables.</p>
            <p><b>Amélioration continue</b> — adapter les solutions aux besoins.</p>
        </div>
        """, unsafe_allow_html=True)

elif page == "Formations":
    st.image(str(ASSETS_DIR / "hero_banner.png"), use_container_width=True)

    st.markdown("## Si tu veux devenir un Comptable Absolu, commence ici")
    st.write(
        "Un Comptable Absolu ne se contente pas d’enregistrer des chiffres. Il comprend les opérations, "
        "vérifie la qualité de son travail, explique les résultats et aide à prendre de meilleures décisions."
    )

    st.markdown(
        """
        <div class="trust-strip">
            Parcours recommandé : 16 cours • 4 niveaux • exercices pratiques • quiz final
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.info(
        "Méthode conseillée : suivez les cours dans l’ordre, prenez des notes, réalisez l’exercice de chaque cours "
        "et cochez « Cours terminé » seulement lorsque vous pouvez expliquer la notion avec vos propres mots."
    )

    cours = [
        {
            "niveau": "Niveau 1 — Les fondations",
            "numero": 1,
            "titre": "Comprendre le rôle de la comptabilité",
            "objectif": "Comprendre pourquoi une entreprise tient une comptabilité et à qui servent les informations produites.",
            "contenu": """
            La comptabilité permet d’enregistrer, classer, résumer et interpréter les opérations financières.
            Elle sert à connaître les ressources de l’entreprise, ses dettes, ses revenus, ses dépenses et son résultat.

            Les principaux utilisateurs sont :
            - les dirigeants, pour prendre des décisions ;
            - les propriétaires, pour évaluer la performance ;
            - les banques, pour analyser la capacité de remboursement ;
            - l’administration fiscale, pour vérifier les déclarations ;
            - les fournisseurs et investisseurs, pour apprécier la solidité de l’entreprise.
            """,
            "exercice": "Citez cinq opérations réalisées dans une petite entreprise et expliquez pourquoi elles doivent être enregistrées.",
        },
        {
            "niveau": "Niveau 1 — Les fondations",
            "numero": 2,
            "titre": "Maîtriser l’équation comptable",
            "objectif": "Comprendre la relation entre l’actif, le passif et les capitaux propres.",
            "contenu": """
            L’équation fondamentale est : **Actif = Passif + Capitaux propres**.

            - L’actif représente ce que l’entreprise possède ou contrôle : caisse, banque, stocks, matériel, créances.
            - Le passif représente les obligations : dettes fournisseurs, emprunts, impôts à payer.
            - Les capitaux propres représentent la part revenant aux propriétaires.

            Exemple : une entreprise possède 15 000 € d’actifs et doit 6 000 € à ses créanciers. Ses capitaux propres sont de 9 000 €.
            """,
            "exercice": "Une entreprise possède 25 000 € d’actifs et 10 000 € de passifs. Calculez ses capitaux propres.",
        },
        {
            "niveau": "Niveau 1 — Les fondations",
            "numero": 3,
            "titre": "Reconnaître les catégories de comptes",
            "objectif": "Classer correctement un élément dans les actifs, passifs, capitaux propres, produits ou charges.",
            "contenu": """
            Les cinq grandes catégories sont :
            - **Actifs** : caisse, banque, clients, stocks, équipements ;
            - **Passifs** : fournisseurs, emprunts, salaires à payer ;
            - **Capitaux propres** : capital, réserves, résultat accumulé ;
            - **Produits** : ventes, prestations, commissions ;
            - **Charges** : loyer, salaires, transport, électricité.

            Un bon comptable doit d’abord comprendre la nature économique de l’opération avant de choisir le compte.
            """,
            "exercice": "Classez les éléments suivants : stock, dette fournisseur, vente, loyer, capital et créance client.",
        },
        {
            "niveau": "Niveau 1 — Les fondations",
            "numero": 4,
            "titre": "Comprendre le débit et le crédit",
            "objectif": "Déterminer le côté d’augmentation et de diminution de chaque catégorie de comptes.",
            "contenu": """
            Le débit et le crédit sont les deux côtés d’une écriture comptable.

            - Les actifs et les charges augmentent généralement au **débit**.
            - Les passifs, les capitaux propres et les produits augmentent généralement au **crédit**.
            - Toute écriture doit respecter l’égalité : total des débits = total des crédits.

            Exemple : achat de fournitures payé comptant pour 300 € : débit Fournitures 300 €, crédit Caisse 300 €.
            """,
            "exercice": "Enregistrez une vente au comptant de 1 200 € en indiquant le compte débité et le compte crédité.",
        },
        {
            "niveau": "Niveau 2 — Le cycle comptable",
            "numero": 5,
            "titre": "Identifier les pièces justificatives",
            "objectif": "Reconnaître les documents qui prouvent et expliquent une opération.",
            "contenu": """
            Une écriture fiable doit reposer sur une pièce justificative : facture, reçu, bordereau bancaire, contrat, bon de commande, fiche de paie ou note de crédit.

            Avant l’enregistrement, vérifiez :
            - la date ;
            - le nom des parties ;
            - le montant ;
            - la nature de l’opération ;
            - l’autorisation ;
            - la cohérence entre le document et le paiement.
            """,
            "exercice": "Préparez une liste de contrôle de six points à vérifier avant d’enregistrer une facture fournisseur.",
        },
        {
            "niveau": "Niveau 2 — Le cycle comptable",
            "numero": 6,
            "titre": "Enregistrer les opérations dans le journal",
            "objectif": "Analyser une opération et produire une écriture comptable équilibrée.",
            "contenu": """
            Le journal enregistre les opérations par ordre chronologique. Chaque écriture comprend généralement la date, les comptes, les montants, la référence de la pièce et une description.

            Méthode d’analyse :
            1. identifier les comptes concernés ;
            2. déterminer leur catégorie ;
            3. déterminer s’ils augmentent ou diminuent ;
            4. appliquer le débit et le crédit ;
            5. vérifier l’équilibre.
            """,
            "exercice": "Passez l’écriture d’un paiement de loyer de 800 € par banque.",
        },
        {
            "niveau": "Niveau 2 — Le cycle comptable",
            "numero": 7,
            "titre": "Comprendre le grand livre et la balance",
            "objectif": "Suivre les mouvements de chaque compte et contrôler l’équilibre général.",
            "contenu": """
            Le grand livre regroupe les opérations par compte. Il permet de connaître le solde de la caisse, de la banque, des clients, des fournisseurs et des autres comptes.

            La balance présente pour chaque compte : le total débit, le total crédit et le solde. Une balance équilibrée confirme l’égalité arithmétique entre débits et crédits, mais ne garantit pas l’absence de toutes les erreurs.
            """,
            "exercice": "Expliquez pourquoi une balance peut être équilibrée même lorsqu’une opération a été enregistrée dans le mauvais compte.",
        },
        {
            "niveau": "Niveau 2 — Le cycle comptable",
            "numero": 8,
            "titre": "Régularisations et clôture",
            "objectif": "Comprendre pourquoi certaines écritures sont nécessaires à la fin d’une période.",
            "contenu": """
            Les écritures de régularisation permettent d’affecter les produits et les charges à la bonne période.

            Elles concernent notamment :
            - les charges à payer ;
            - les produits à recevoir ;
            - les charges constatées d’avance ;
            - les produits constatés d’avance ;
            - les amortissements ;
            - les provisions et corrections nécessaires.
            """,
            "exercice": "Une assurance annuelle de 1 200 € est payée le 1er octobre. Calculez la charge correspondant aux trois premiers mois.",
        },
        {
            "niveau": "Niveau 3 — États financiers et contrôle",
            "numero": 9,
            "titre": "Lire et préparer un bilan",
            "objectif": "Comprendre la structure du bilan et analyser la situation financière à une date donnée.",
            "contenu": """
            Le bilan présente les actifs, les passifs et les capitaux propres. Il permet d’évaluer ce que l’entreprise possède, ce qu’elle doit et sa valeur comptable nette.

            Analysez notamment :
            - le niveau de trésorerie ;
            - les créances clients ;
            - les stocks ;
            - les dettes à court terme ;
            - l’endettement ;
            - les capitaux propres.
            """,
            "exercice": "Préparez un mini-bilan avec caisse 2 000 €, banque 8 000 €, stock 5 000 €, fournisseurs 4 000 € et capital 11 000 €.",
        },
        {
            "niveau": "Niveau 3 — États financiers et contrôle",
            "numero": 10,
            "titre": "Comprendre le compte de résultat",
            "objectif": "Calculer et interpréter le bénéfice ou la perte d’une période.",
            "contenu": """
            Le compte de résultat compare les produits et les charges d’une période.

            **Résultat = Produits − Charges**

            Un bénéfice ne signifie pas nécessairement que l’entreprise dispose immédiatement de beaucoup d’argent en banque. Certaines ventes peuvent être à crédit, et certains paiements peuvent concerner une autre période.
            """,
            "exercice": "Une entreprise réalise 18 000 € de produits et 13 500 € de charges. Calculez et interprétez son résultat.",
        },
        {
            "niveau": "Niveau 3 — États financiers et contrôle",
            "numero": 11,
            "titre": "Gérer la trésorerie et faire une conciliation bancaire",
            "objectif": "Comparer les livres comptables avec le relevé bancaire et expliquer les écarts.",
            "contenu": """
            La conciliation bancaire rapproche le solde comptable de la banque avec le solde du relevé bancaire.

            Les différences peuvent provenir de :
            - chèques ou virements en circulation ;
            - dépôts non encore crédités ;
            - frais bancaires ;
            - intérêts ;
            - erreurs de saisie ;
            - opérations enregistrées par la banque mais pas encore en comptabilité.

            Chaque écart doit être documenté, expliqué et, si nécessaire, corrigé par une écriture.
            """,
            "exercice": "Préparez un tableau avec les colonnes : date, description, montant banque, montant comptabilité, écart et observation.",
        },
        {
            "niveau": "Niveau 3 — États financiers et contrôle",
            "numero": 12,
            "titre": "Budget, ratios et tableau de bord",
            "objectif": "Transformer les données comptables en informations utiles à la décision.",
            "contenu": """
            Le budget fixe des objectifs de recettes et de dépenses. Le suivi budgétaire compare le prévu au réel et explique les écarts.

            Quelques indicateurs simples :
            - marge = ventes − coût des ventes ;
            - taux de marge = marge ÷ ventes × 100 ;
            - liquidité = actifs à court terme ÷ passifs à court terme ;
            - délai de recouvrement des clients ;
            - évolution des dépenses et du résultat.
            """,
            "exercice": "Calculez la marge et le taux de marge pour des ventes de 20 000 € et un coût des ventes de 12 000 €.",
        },
        {
            "niveau": "Niveau 4 — Le Comptable Absolu en pratique",
            "numero": 13,
            "titre": "Utiliser Excel pour la comptabilité",
            "objectif": "Construire des tableaux fiables, lisibles et contrôlables.",
            "contenu": """
            Excel peut servir à préparer un journal, une conciliation, un budget, un suivi de caisse ou un tableau de bord.

            Compétences essentielles :
            - références de cellules ;
            - SOMME, SI, SOMME.SI et RECHERCHEX ;
            - tableaux structurés ;
            - validation des données ;
            - filtres et tris ;
            - tableaux croisés dynamiques ;
            - protection et contrôle des formules.
            """,
            "exercice": "Créez un tableau de dépenses avec date, catégorie, description, montant et total par catégorie.",
        },
        {
            "niveau": "Niveau 4 — Le Comptable Absolu en pratique",
            "numero": 14,
            "titre": "Découvrir les logiciels comptables",
            "objectif": "Comprendre comment travailler dans QuickBooks, ACCPAC ou un autre système comptable.",
            "contenu": """
            Un logiciel comptable facilite l’enregistrement, le classement, les contrôles et la production des rapports.

            Avant toute saisie :
            - comprendre le plan comptable ;
            - identifier le bon module ;
            - utiliser une description claire ;
            - joindre ou conserver la pièce justificative ;
            - vérifier la période et la devise ;
            - contrôler le rapport après l’enregistrement.

            Le logiciel automatise certains calculs, mais il ne remplace pas le jugement du comptable.
            """,
            "exercice": "Rédigez une procédure de cinq étapes pour enregistrer et vérifier un paiement fournisseur dans un logiciel comptable.",
        },
        {
            "niveau": "Niveau 4 — Le Comptable Absolu en pratique",
            "numero": 15,
            "titre": "Contrôle interne et prévention des erreurs",
            "objectif": "Mettre en place des contrôles simples pour protéger les ressources et fiabiliser l’information.",
            "contenu": """
            Le contrôle interne comprend les règles et procédures utilisées pour réduire les erreurs, les pertes et les fraudes.

            Exemples :
            - séparation entre autorisation, paiement et enregistrement ;
            - approbation des dépenses ;
            - numérotation des pièces ;
            - rapprochements réguliers ;
            - inventaires physiques ;
            - contrôle des accès aux systèmes ;
            - revue des rapports par un responsable.
            """,
            "exercice": "Proposez cinq contrôles internes pour une petite entreprise qui reçoit beaucoup d’argent en espèces.",
        },
        {
            "niveau": "Niveau 4 — Le Comptable Absolu en pratique",
            "numero": 16,
            "titre": "Éthique, confidentialité et communication",
            "objectif": "Adopter le comportement professionnel attendu d’un comptable fiable.",
            "contenu": """
            Un comptable doit agir avec intégrité, objectivité, compétence, prudence et confidentialité.

            Il doit également savoir communiquer :
            - présenter un rapport clair ;
            - expliquer un écart sans accuser sans preuve ;
            - signaler les risques importants ;
            - distinguer les faits, les hypothèses et les recommandations ;
            - protéger les documents et les mots de passe ;
            - reconnaître les limites de son intervention.
            """,
            "exercice": "Rédigez un court message professionnel pour signaler à un supérieur un écart bancaire non encore expliqué.",
        },
    ]

    niveaux = list(dict.fromkeys(item["niveau"] for item in cours))
    cours_termines = 0

    for niveau in niveaux:
        st.markdown(f"### {niveau}")
        for item in [c for c in cours if c["niveau"] == niveau]:
            key = f"cours_termine_{item['numero']}"
            with st.expander(f"Cours {item['numero']} — {item['titre']}"):
                st.markdown(f"**Objectif :** {item['objectif']}")
                st.markdown(item["contenu"])
                st.markdown(f"**Exercice pratique :** {item['exercice']}")
                st.checkbox("Cours terminé", key=key)
            if st.session_state.get(key, False):
                cours_termines += 1

    progression = int((cours_termines / len(cours)) * 100)
    st.markdown("## Ma progression")
    st.progress(progression / 100)
    st.write(f"**{cours_termines} cours terminés sur {len(cours)} — {progression} %**")

    if cours_termines == len(cours):
        st.success(
            "Félicitations ! Vous avez terminé le parcours. Continuez maintenant avec des exercices, "
            "des cas pratiques et une expérience professionnelle supervisée."
        )

    st.markdown("## Quiz final — Es-tu prêt à devenir un Comptable Absolu ?")
    with st.form("quiz_comptable_absolu"):
        q1 = st.radio(
            "1. Quelle équation est correcte ?",
            ["Actif = Passif + Capitaux propres", "Produits = Actif + Charges", "Passif = Actif + Ventes"],
            index=None,
        )
        q2 = st.radio(
            "2. Une charge augmente normalement au :",
            ["Débit", "Crédit", "Aucun côté"],
            index=None,
        )
        q3 = st.radio(
            "3. À quoi sert principalement une conciliation bancaire ?",
            [
                "À comparer la banque et la comptabilité",
                "À calculer uniquement les ventes",
                "À remplacer le relevé bancaire",
            ],
            index=None,
        )
        q4 = st.radio(
            "4. Quelle pratique renforce le contrôle interne ?",
            [
                "Une seule personne autorise, paie et enregistre tout",
                "Séparer l’autorisation, le paiement et l’enregistrement",
                "Supprimer les pièces justificatives après paiement",
            ],
            index=None,
        )
        q5 = st.radio(
            "5. Un logiciel comptable remplace-t-il le jugement du comptable ?",
            ["Oui, toujours", "Non", "Seulement pour les grandes entreprises"],
            index=None,
        )
        valider = st.form_submit_button("Voir mon résultat")

    if valider:
        reponses = [q1, q2, q3, q4, q5]
        if any(rep is None for rep in reponses):
            st.warning("Répondez aux cinq questions avant de valider.")
        else:
            score = sum([
                q1 == "Actif = Passif + Capitaux propres",
                q2 == "Débit",
                q3 == "À comparer la banque et la comptabilité",
                q4 == "Séparer l’autorisation, le paiement et l’enregistrement",
                q5 == "Non",
            ])
            st.metric("Votre résultat", f"{score}/5")
            if score == 5:
                st.success("Excellent ! Vous maîtrisez les notions fondamentales du parcours.")
            elif score >= 3:
                st.info("Bon résultat. Revoyez les cours correspondant aux réponses incorrectes.")
            else:
                st.warning("Reprenez le parcours depuis le Niveau 1 et réalisez chaque exercice.")

    st.markdown("## Formation personnalisée")
    st.write(
        "Pour une formation individuelle, une formation d’équipe ou un accompagnement pratique, contactez directement Absolu."
    )
    formation_message = (
        "Bonjour M. Absolu, je souhaite suivre une formation pour devenir un Comptable Absolu. "
        "Merci de m’envoyer les modalités, la durée et le tarif."
    )
    st.link_button("Demander la formation sur WhatsApp", f"https://wa.me/{WHATSAPP_NUMBER}?text={quote(formation_message)}")

elif page == "Services comptables":
    st.image(str(ASSETS_DIR / "services_banner.png"), use_container_width=True)
    st.markdown("### Services comptables et administratifs")
    left, right = st.columns(2)
    with left:
        st.markdown(
            """
            **Je propose notamment :**
            - tenue et mise à jour de comptabilité ;
            - conciliation bancaire ;
            - préparation de tableaux de suivi ;
            - préparation ou assistance à la préparation des états financiers ;
            - suivi des dépenses, recettes et caisse ;
            - assistance administrative et organisation documentaire ;
            - tableaux Excel personnalisés ;
            - accompagnement des petites structures.
            """
        )
    with right:
        st.markdown(
            """
            <div class="contact-box">
                <h3 class="section-title">Pourquoi ce service est utile ?</h3>
                <p>Une bonne organisation comptable aide à mieux décider, mieux contrôler les opérations et mieux présenter la situation financière de l’entreprise.</p>
                <p><b>Contact direct :</b> +509 38 05 8311</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.link_button("Parler de mon besoin sur WhatsApp", DEFAULT_WHATSAPP_URL, use_container_width=True)

    st.markdown("### Exemples de besoins que je peux traiter")
    ex1, ex2, ex3 = st.columns(3)
    ex1.info("Mettre de l’ordre dans les opérations comptables d’une petite entreprise")
    ex2.info("Créer un tableau de suivi de caisse, banque, clients ou dépenses")
    ex3.info("Préparer un système simple de contrôle et de reporting")

elif page == "Systèmes & sites personnalisés":
    st.image(str(ASSETS_DIR / "digital_banner.png"), use_container_width=True)
    st.markdown("### Création de systèmes et de sites web personnalisés")
    st.write(
        "En plus des services liés à la comptabilité, je peux contribuer à la création de solutions personnalisées pour les entreprises."
    )

    c1, c2 = st.columns(2)
    with c1:
        st.markdown(
            """
            **Systèmes personnalisés possibles :**
            - suivi des ventes et encaissements ;
            - gestion de caisse ;
            - suivi des dépenses ;
            - suivi de stock ;
            - gestion de paiements ;
            - tableaux de bord et rapports simplifiés ;
            - outils internes de suivi administratif.
            """
        )
    with c2:
        st.markdown(
            """
            **Sites web possibles :**
            - site vitrine d’entreprise ;
            - page de présentation de services ;
            - site éducatif ou professionnel ;
            - formulaire de contact et prise de rendez-vous ;
            - interface simple orientée clients.
            """
        )

    st.success("Chaque projet peut être adapté selon les besoins, le secteur et le budget de l’entreprise.")
    st.link_button("Demander un système ou un site personnalisé", DEFAULT_WHATSAPP_URL)


elif page == "Outils gratuits":
    st.markdown("### Outils gratuits")
    st.write("Téléchargez des modèles simples pour commencer à mieux organiser vos données.")

    budget_csv = """Catégorie,Budget prévu (€),Dépense réelle (€),Écart (€)\nLoyer,0,0,=B2-C2\nTransport,0,0,=B3-C3\nCommunication,0,0,=B4-C4\nFournitures,0,0,=B5-C5\nAutres,0,0,=B6-C6\n"""
    caisse_csv = """Date,Description,Entrée (€),Sortie (€),Solde (€)\n,Solde initial,0,0,0\n,,,,=E2+C3-D3\n"""
    conciliation_csv = """Date,Description,Montant selon banque (€),Montant selon comptabilité (€),Écart (€),Observation\n,,,,=C2-D2,\n"""

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="small-card"><h3>📁 Budget mensuel</h3><p>Prévisions, réalisations et écarts.</p></div>', unsafe_allow_html=True)
        st.download_button("Télécharger", budget_csv.encode("utf-8-sig"), "modele_budget.csv", "text/csv", use_container_width=True)
    with c2:
        st.markdown('<div class="small-card"><h3>💶 Suivi de caisse</h3><p>Entrées, sorties et solde progressif.</p></div>', unsafe_allow_html=True)
        st.download_button("Télécharger", caisse_csv.encode("utf-8-sig"), "suivi_caisse.csv", "text/csv", use_container_width=True)
    with c3:
        st.markdown('<div class="small-card"><h3>🏦 Conciliation</h3><p>Comparer banque et comptabilité.</p></div>', unsafe_allow_html=True)
        st.download_button("Télécharger", conciliation_csv.encode("utf-8-sig"), "conciliation_bancaire.csv", "text/csv", use_container_width=True)

    st.markdown("### Calcul rapide du résultat")
    produits = st.number_input("Produits (€)", min_value=0.0, step=100.0)
    charges = st.number_input("Charges (€)", min_value=0.0, step=100.0)
    resultat = produits - charges
    if resultat > 0:
        st.success(f"Bénéfice : {resultat:,.2f} €")
    elif resultat < 0:
        st.error(f"Perte : {abs(resultat):,.2f} €")
    else:
        st.info("Résultat : 0,00 €")

elif page == "Portfolio":
    st.markdown("### Portfolio de démonstration")
    st.caption("Les éléments ci-dessous sont présentés comme prototypes ou modèles. Ils ne constituent pas des témoignages ou missions clients non vérifiés.")
    p1, p2, p3 = st.columns(3)
    with p1:
        st.markdown("""<div class="prototype"><h3>Mini Gestion Comptable</h3><p>Prototype de calcul des recettes, dépenses et solde final.</p><b>Type :</b> application de démonstration</div>""", unsafe_allow_html=True)
    with p2:
        st.markdown("""<div class="prototype"><h3>Tableau de conciliation</h3><p>Modèle pour comparer les données bancaires et comptables.</p><b>Type :</b> outil de suivi</div>""", unsafe_allow_html=True)
    with p3:
        st.markdown("""<div class="prototype"><h3>Site éducatif comptable</h3><p>Plateforme de formation et de présentation de services.</p><b>Type :</b> site web</div>""", unsafe_allow_html=True)
    st.markdown("### Votre projet peut devenir le prochain")
    st.link_button("Présenter mon projet", f"https://wa.me/{WHATSAPP_NUMBER}?text={quote('Bonjour M. Absolu, je souhaite vous présenter un projet.')}")


elif page == "Pourquoi me choisir":
    st.markdown("### Pourquoi travailler avec moi ?")
    x1, x2, x3 = st.columns(3)
    with x1:
        st.markdown(
            """
            <div class="small-card">
                <h3>🎯 Approche claire</h3>
                <p>J’explique les concepts de manière simple et professionnelle, même pour les non-initiés.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with x2:
        st.markdown(
            """
            <div class="small-card">
                <h3>🧾 Vision comptable</h3>
                <p>Je comprends les besoins concrets de gestion, d’organisation, de contrôle et de suivi.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with x3:
        st.markdown(
            """
            <div class="small-card">
                <h3>🚀 Solutions pratiques</h3>
                <p>Je propose des outils utiles, adaptés à la réalité des particuliers, professionnels et entreprises.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        """
        <div class="value-box">
            <b>Mon engagement :</b> fournir un service sérieux, clair, pratique et orienté résultats.
        </div>
        """,
        unsafe_allow_html=True,
    )


elif page == "Demander un devis":
    st.markdown("### Demande de devis")
    st.write("Remplissez les informations. Le site préparera un message WhatsApp structuré.")
    with st.form("devis_form"):
        nom = st.text_input("Nom ou entreprise *")
        service = st.selectbox("Service recherché *", [
            "Service comptable",
            "Conciliation bancaire",
            "Tableau Excel personnalisé",
            "Formation en comptabilité",
            "Création d’un site web",
            "Création d’un système personnalisé",
            "Assistance administrative",
            "Autre besoin",
        ])
        secteur = st.text_input("Secteur d’activité")
        delai = st.selectbox("Délai souhaité", ["À discuter", "Moins d’une semaine", "1 à 2 semaines", "1 mois ou plus"])
        budget = st.selectbox("Budget approximatif", ["À discuter", "Budget limité", "Budget moyen", "Selon la proposition"])
        details = st.text_area("Description du besoin *", height=150)
        valider = st.form_submit_button("Préparer le message")

    if valider:
        if not nom.strip() or not details.strip():
            st.warning("Veuillez remplir le nom et la description du besoin.")
        else:
            message = (
                f"Bonjour M. Absolu,\n\n"
                f"Je souhaite demander un devis.\n"
                f"Nom / entreprise : {nom}\n"
                f"Service : {service}\n"
                f"Secteur : {secteur or 'Non précisé'}\n"
                f"Délai : {delai}\n"
                f"Budget : {budget}\n"
                f"Besoin : {details}\n\n"
                f"Merci de me contacter pour discuter des prochaines étapes."
            )
            st.success("Votre message est prêt.")
            st.code(message, language="text")
            st.link_button("Envoyer sur WhatsApp", f"https://wa.me/{WHATSAPP_NUMBER}?text={quote(message)}", use_container_width=True)


elif page == "Contact":
    st.markdown("### Contact & demande de service")
    c1, c2 = st.columns([1, 1.2])
    with c1:
        st.markdown(
            """
            <div class="contact-box">
                <h3 class="section-title">Informations de contact</h3>
                <p><b>Nom :</b> Absolu</p>
                <p><b>Profession :</b> Comptable</p>
                <p><b>Marque professionnelle :</b> Le Comptable Absolu</p>
                <p><b>Spécialités :</b> comptabilité, formation, assistance administrative, systèmes et sites personnalisés</p>
                <p><b>Téléphone / WhatsApp :</b> +509 38 05 8311</p>
                <p><b>Disponibilité :</b> particuliers, entrepreneurs, institutions et entreprises</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.link_button("Envoyer un message direct sur WhatsApp", DEFAULT_WHATSAPP_URL, use_container_width=True)
    with c2:
        st.markdown("#### Préparer un message WhatsApp personnalisé")
        nom = st.text_input("Votre nom")
        service = st.selectbox(
            "Votre besoin principal",
            [
                "Demande d'information générale",
                "Service comptable",
                "Formation en comptabilité",
                "Création d'un système personnalisé",
                "Création d'un site web personnalisé",
                "Assistance administrative",
            ],
        )
        details = st.text_area("Décrivez brièvement votre besoin")
        if not nom:
            nom = "un client"
        if not details:
            details = "Je souhaite avoir plus d'informations."
        msg = f"Bonjour, je m'appelle {nom}. Je vous contacte pour : {service}. Détails : {details}"
        custom_url = f"https://wa.me/{WHATSAPP_NUMBER}?text={quote(msg)}"
        st.link_button("Ouvrir WhatsApp avec ce message", custom_url, use_container_width=True)
        st.code(msg, language="text")


    st.markdown("### Questions fréquentes")
    with st.expander("Comment demander un devis ?"):
        st.write("Utilisez la page « Demander un devis » ou contactez directement par WhatsApp.")
    with st.expander("Les services sont-ils personnalisés ?"):
        st.write("Oui. Le contenu, le délai et le prix dépendent du besoin réel.")
    with st.expander("Un système peut-il être adapté à mon entreprise ?"):
        st.write("Oui. Le projet commence par une analyse des processus, des données et des utilisateurs.")
    with st.expander("Le site remplace-t-il un conseil professionnel complet ?"):
        st.write("Les contenus éducatifs sont généraux. Une mission professionnelle nécessite l’analyse de votre situation et de vos documents.")


st.markdown(
    """
    <div class="footer">
        © 2026 Comptabilité pour les non-comptables — Créé par Absolu, comptable | Le Comptable Absolu | WhatsApp : +509 38 05 8311
    </div>
    """,
    unsafe_allow_html=True,
)
