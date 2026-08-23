import streamlit as st

st.title("CBSE Class 10 Social Science Board Revision Quiz")
st.write("Select your options for each section, then click **Submit Entire Quiz** at the bottom to calculate your total score!")

# --- QUESTION BANK STRUCTURED BY SUBJECT ---

history_questions = [
    {
        "q": "Which treaty recognized Greece as an independent nation in 1832?",
        "options": ["(A) Treaty of Versailles", "(B) Treaty of Constantinople", "(C) Treaty of Vienna", "(D) Treaty of Lausanne"],
        "ans": "(B)",
        "exp": "The Treaty of Constantinople of 1832 recognized Greece as an independent nation."
    },
    {
        "q": "Who among the following described Giuseppe Mazzini as 'The most dangerous enemy of our social order'?",
        "options": ["(A) Giuseppe Garibaldi", "(B) Otto von Bismarck", "(C) Duke Metternich", "(D) King Victor Emmanuel II"],
        "ans": "(C)",
        "exp": "The Austrian Chancellor, Duke Metternich, feared Mazzini's underground societies and republican ideals."
    },
    {
        "q": "On which date did the infamous Jallianwala Bagh incident take place?",
        "options": ["(A) 13 April 1919", "(B) 15 April 1921", "(C) 20 October 1981", "(D) 10 March 1939"],
        "ans": "(A)",
        "exp": "The Jallianwala Bagh massacre took place on Baisakhi day, 13 April 1919, in Amritsar."
    },
    {
        "q": "Which of the following books was written by Mahatma Gandhi in 1909?",
        "options": ["(A) Discovery of India", "(B) Anandamath", "(C) Poverty and Un-British Rule in India", "(D) Hind Swaraj"],
        "ans": "(D)",
        "exp": "Hind Swaraj was written by Mahatma Gandhi in 1909."
    }
]

geography_questions = [
    {
        "q": "In which year was the Earth Summit held in Rio de Janeiro?",
        "options": ["(A) 1990", "(B) 1992", "(C) 1997", "(D) 2002"],
        "ans": "(B)",
        "exp": "The first International Earth Summit was held in Rio de Janeiro, Brazil, in 1992."
    },
    {
        "q": "Which of the following soils is most ideal for growing cotton and is known as regur soil?",
        "options": ["(A) Red soil", "(B) Laterite soil", "(C) Black soil", "(D) Arid soil"],
        "ans": "(C)",
        "exp": "Black soil, also known as regur soil, is ideal for growing cotton."
    },
    {
        "q": "Resources which are obtained from the biosphere and have life are known as:",
        "options": ["(A) Biotic Resources", "(B) Abiotic Resources", "(C) Renewable Resources", "(D) Potential Resources"],
        "ans": "(A)",
        "exp": "Biotic resources are obtained from the biosphere and have life."
    },
    {
        "q": "Which of the following crops is a rabi crop in India?",
        "options": ["(A) Rice", "(B) Wheat", "(C) Maize", "(D) Jowar"],
        "ans": "(B)",
        "exp": "Wheat is a principal rabi crop sown in winter and harvested in spring."
    },
    {
        "q": "Which one of the following is the staple food crop of the majority of people in India?",
        "options": ["(A) Wheat", "(B) Millets", "(C) Maize", "(D) Rice"],
        "ans": "(D)",
        "exp": "Rice is the staple food crop for the majority of people in India."
    },
    {
        "q": "What is 'Jhumming' in India?",
        "options": ["(A) A type of commercial farming", "(B) A method of manufacturing", "(C) Shifting cultivation", "(D) A type of plantation agriculture"],
        "ans": "(C)",
        "exp": "Jhumming is the local name for shifting cultivation in north-eastern India."
    }
]

civics_questions = [
    {
        "q": "Which two languages are spoken by the majority of people in Belgium?",
        "options": ["(A) French and German", "(B) Dutch and French", "(C) English and Dutch", "(D) German and Italian"],
        "ans": "(B)",
        "exp": "59% of the population lives in the Flemish region and speaks Dutch, while 40% lives in the Wallonia region and speaks French."
    },
    {
        "q": "Which legal act was passed in Sri Lanka in 1956 to establish Sinhala dominance?",
        "options": ["(A) An Act recognizing Sinhala as the sole official language", "(B) An Act creating a federal government", "(C) An Act establishing Tamil as an official language", "(D) An Act declaring Sri Lanka a republic"],
        "ans": "(A)",
        "exp": "In 1956, an Act was passed in Sri Lanka to recognize Sinhala as the only official language, disregarding Tamil."
    },
    {
        "q": "Subjects of national importance, such as Defense, Foreign Affairs, and Banking, are included in which list of the Indian Constitution?",
        "options": ["(A) State List", "(B) Concurrent List", "(C) Union List", "(D) Residuary List"],
        "ans": "(C)",
        "exp": "The Union List includes subjects of national importance because a uniform policy is needed across the entire nation."
    },
    {
        "q": "Which third tier of government was reinforced in India through the Constitutional Amendment of 1992?",
        "options": ["(A) Union Territory Government", "(B) Panchayati Raj / Local Self-Government", "(C) State Assembly", "(D) Supreme Court Directorate"],
        "ans": "(B)",
        "exp": "The 73rd and 74th Amendments in 1992 constitutionalized Panchayati Raj (Rural) and Municipalities (Urban) to strengthen local democracy."
    },
    {
        "q": "Which of the following is a recognized 'National Party' in India?",
        "options": ["(A) Samajwadi Party", "(B) Bharatiya Janata Party (BJP)", "(C) Rashtriya Janata Dal", "(D) DMK"],
        "ans": "(B)",
        "exp": "The Bharatiya Janata Party (BJP) is a registered and recognized National Party in India."
    }
]

economics_questions = [
    {
        "q": "Which international body calculates and publishes the Human Development Index (HDI)?",
        "options": ["(A) World Bank", "(B) International Monetary Fund (IMF)", "(C) United Nations Development Programme (UNDP)", "(D) World Trade Organization (WTO)"],
        "ans": "(C)",
        "exp": "The UNDP publishes the Human Development Report, comparing countries based on educational levels, health status, and per capita income."
    },
    {
        "q": "Activities involving the extraction and exploitation of natural resources belong to which sector?",
        "options": ["(A) Primary Sector", "(B) Secondary Sector", "(C) Tertiary Sector", "(D) Quaternary Sector"],
        "ans": "(A)",
        "exp": "The Primary sector directly uses natural resources to produce goods."
    },
    {
        "q": "Which organization in India issues currency notes on behalf of the Central Government?",
        "options": ["(A) State Bank of India (SBI)", "(B) Reserve Bank of India (RBI)", "(C) Ministry of Finance", "(D) NITI Aayog"],
        "ans": "(B)",
        "exp": "In India, only the Reserve Bank of India (RBI) is authorized to issue currency notes on behalf of the Central Government."
    },
    {
        "q": "What is the term for a situation where both parties have to agree to sell and buy each other's commodities without using money?",
        "options": ["(A) Double coincidence of wants", "(B) Collateral system", "(C) Deferred payment", "(D) Credit agreement"],
        "ans": "(A)",
        "exp": "Double coincidence of wants is an essential feature of the barter system."
    },
    {
        "q": "Which process describes the rapid integration or interconnection between countries through trade, foreign investment, and technology?",
        "options": ["(A) Privatization", "(B) Urbanization", "(C) Globalization", "(D) Decentralization"],
        "ans": "(C)",
        "exp": "Globalization is the process of rapid integration or interconnection between countries through trade, capital, and labor movement."
    }
]

# --- FORM & SUBJECT TABS ---

user_responses = {}

with st.form("sst_quiz_form"):
    tab1, tab2, tab3, tab4 = st.tabs(["📜 History", "🌍 Geography", "🏛️ Civics", "📈 Economics"])

    # History Tab Content
    with tab1:
        st.header("History Section")
        for idx, item in enumerate(history_questions):
            st.subheader(f"Q{idx + 1}. {item['q']}")
            user_responses[f"hist_{idx}"] = st.radio("Select option:", item["options"], key=f"hist_radio_{idx}")
            st.divider()

    # Geography Tab Content
    with tab2:
        st.header("Geography Section")
        for idx, item in enumerate(geography_questions):
            st.subheader(f"Q{idx + 1}. {item['q']}")
            user_responses[f"geo_{idx}"] = st.radio("Select option:", item["options"], key=f"geo_radio_{idx}")
            st.divider()

    # Civics Tab Content
    with tab3:
        st.header("Civics Section")
        for idx, item in enumerate(civics_questions):
            st.subheader(f"Q{idx + 1}. {item['q']}")
            user_responses[f"civ_{idx}"] = st.radio("Select option:", item["options"], key=f"civ_radio_{idx}")
            st.divider()

    # Economics Tab Content
    with tab4:
        st.header("Economics Section")
        for idx, item in enumerate(economics_questions):
            st.subheader(f"Q{idx + 1}. {item['q']}")
            user_responses[f"eco_{idx}"] = st.radio("Select option:", item["options"], key=f"eco_radio_{idx}")
            st.divider()

    # Submit Button for the entire quiz
    submitted = st.form_submit_button("Submit Entire Quiz 🚀")

# --- RESULTS & SCORE CALCULATION ---

if submitted:
    total_score = 0
    all_sections = [
        (history_questions, "hist"),
        (geography_questions, "geo"),
        (civics_questions, "civ"),
        (economics_questions, "eco")
    ]
    
    total_questions = sum(len(questions) for questions, _ in all_sections)

    for questions, prefix in all_sections:
        for idx, item in enumerate(questions):
            if item["ans"] in user_responses.get(f"{prefix}_{idx}", ""):
                total_score += 1

    st.balloons()
    st.header("🏆 Final Quiz Scorecard")
    percentage = (total_score / total_questions) * 100
    
    st.metric(label="Total Marks Obtained", value=f"{total_score} / {total_questions}", delta=f"{percentage:.1f}% Score")

    if percentage >= 80:
        st.success("🎉 Excellent! Your preparation for CBSE Class 10 SST is on track for a top score!")
    elif percentage >= 50:
        st.warning("👍 Good effort! Review the chapters you missed to strengthen your concepts.")
    else:
        st.error("💡 Keep practicing! Go through your NCERT textbook once more and re-attempt the quiz.")
        
