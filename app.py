import streamlit as st
import time

# Import auto-refresh component
try:
    from streamlit_autorefresh import st_autorefresh
    HAS_AUTOREFRESH = True
except ImportError:
    HAS_AUTOREFRESH = False

st.set_page_config(page_title="CBSE Class 10 SST Quiz", layout="wide")

# ==========================================
# SESSION STATE INITIALIZATION
# ==========================================
if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False
if "quiz_submitted" not in st.session_state:
    st.session_state.quiz_submitted = False
if "balloons_shown" not in st.session_state:
    st.session_state.balloons_shown = False
if "start_time" not in st.session_state:
    st.session_state.start_time = None

# ==========================================
# SIDEBAR: TIMER & CONFIGURATION OPTIONS
# ==========================================

st.sidebar.header("⏱️ Quiz Mode & Timer")
timer_mode = st.sidebar.radio(
    "Choose Quiz Mode:",
    ["Without Timer (Practice Mode)", "With Timer (Exam Mode)"],
    disabled=st.session_state.quiz_started
)

time_limit_sec = 0
if timer_mode == "With Timer (Exam Mode)":
    time_limit_min = st.sidebar.number_input(
        "Set Time Limit (in minutes):",
        min_value=1,
        max_value=180,
        value=30,
        step=1,
        disabled=st.session_state.quiz_started
    )
    time_limit_sec = time_limit_min * 60

    # Auto-refresh every 1000ms (1 second) when quiz is running
    if HAS_AUTOREFRESH and st.session_state.quiz_started and not st.session_state.quiz_submitted:
        st_autorefresh(interval=1000, key="quiz_timer_refresh")

# Reset / Restart Quiz Button
if st.sidebar.button("🔄 Restart / Reset Quiz"):
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()

sidebar_timer_placeholder = st.sidebar.empty()

# ==========================================
# MAIN HEADER & DUAL TIMER DISPLAY
# ==========================================

col_title, col_timer = st.columns([3, 1])

with col_title:
    st.title("CBSE Class 10 Social Science Board Revision Quiz")

main_timer_placeholder = col_timer.empty()
warning_banner_placeholder = st.empty()

# Timer Logic & Execution
if timer_mode == "With Timer (Exam Mode)":
    if not st.session_state.quiz_started:
        sidebar_timer_placeholder.info("⏳ Waiting for you to start the test.")
        main_timer_placeholder.info("⏳ Press Start Test below")
    elif st.session_state.quiz_started and not st.session_state.quiz_submitted:
        elapsed_time = int(time.time() - st.session_state.start_time)
        remaining_time = time_limit_sec - elapsed_time

        if remaining_time > 0:
            mins, secs = divmod(remaining_time, 60)
            time_text = f"⏳ **Time Left:** {mins:02d}:{secs:02d}"

            if remaining_time <= 60:
                warning_banner_placeholder.error("⚠️ **LAST MINUTE WARNING:** Less than 1 minute remaining!")
                sidebar_timer_placeholder.error(time_text)
                main_timer_placeholder.error(time_text)
            else:
                sidebar_timer_placeholder.warning(time_text)
                main_timer_placeholder.warning(time_text)
        else:
            sidebar_timer_placeholder.error("🚨 **Time's Up!**")
            main_timer_placeholder.error("🚨 **Time's Up!**")
            st.session_state.quiz_submitted = True
            st.rerun()
else:
    sidebar_timer_placeholder.info("ℹ️ Practice Mode active.")
    main_timer_placeholder.info("ℹ️ No time limit")

# ==========================================
# QUESTION BANK (60 QUESTIONS)
# ==========================================

history_questions = [
    {"q": "Which treaty recognized Greece as an independent nation in 1832?", "options": ["(A) Treaty of Versailles", "(B) Treaty of Constantinople", "(C) Treaty of Vienna", "(D) Treaty of Lausanne"], "ans": "(B)", "exp": "The Treaty of Constantinople of 1832 recognized Greece as an independent nation."},
    {"q": "Who among the following described Giuseppe Mazzini as 'The most dangerous enemy of our social order'?", "options": ["(A) Giuseppe Garibaldi", "(B) Otto von Bismarck", "(C) Duke Metternich", "(D) King Victor Emmanuel II"], "ans": "(C)", "exp": "The Austrian Chancellor, Duke Metternich, feared Mazzini's underground societies and republican ideals."},
    {"q": "On which date did the infamous Jallianwala Bagh incident take place?", "options": ["(A) 13 April 1919", "(B) 15 April 1921", "(C) 20 October 1981", "(D) 10 March 1939"], "ans": "(A)", "exp": "The Jallianwala Bagh massacre took place on Baisakhi day, 13 April 1919, in Amritsar."},
    {"q": "Which of the following books was written by Mahatma Gandhi in 1909?", "options": ["(A) Discovery of India", "(B) Anandamath", "(C) Poverty and Un-British Rule in India", "(D) Hind Swaraj"], "ans": "(D)", "exp": "Hind Swaraj was written by Mahatma Gandhi in 1909."},
    {"q": "Which class was the dominant class socially and politically on the European continent in the 19th century?", "options": ["(A) Peasantry", "(B) Landed Aristocracy", "(C) Industrial Workers", "(D) Traders"], "ans": "(B)", "exp": "Socially and politically, a landed aristocracy was the dominant class on the European continent."},
    {"q": "Who was proclaimed King of United Italy in 1861?", "options": ["(A) Victor Emmanuel II", "(B) Louis Philippe", "(C) Kaiser William I", "(D) Cavour"], "ans": "(A)", "exp": "Victor Emmanuel II was proclaimed King of United Italy in 1861."},
    {"q": "Which architect was responsible for the unification of Germany?", "options": ["(A) Otto von Bismarck", "(B) Count Cavour", "(C) Mazzini", "(D) Garibaldi"], "ans": "(A)", "exp": "Otto von Bismarck, Chief Minister of Prussia, was the architect of German unification."},
    {"q": "Under whose leadership was the Non-Cooperation Movement launched in India?", "options": ["(A) Jawaharlal Nehru", "(B) Mahatma Gandhi", "(C) Subhash Chandra Bose", "(D) Bhagat Singh"], "ans": "(B)", "exp": "The Non-Cooperation Movement was launched under the leadership of Mahatma Gandhi in 1921."},
    {"q": "Why was the Simon Commission boycotted by Indians?", "options": ["(A) It supported partition", "(B) It had no Indian members", "(C) It raised taxes", "(D) It banned the Congress party"], "ans": "(B)", "exp": "The Simon Commission did not have a single Indian member."},
    {"q": "From where did Mahatma Gandhi start his famous Salt March to Dandi?", "options": ["(A) Sabarmati Ashram", "(B) Dandi seashore", "(C) Champaran", "(D) Chauri Chaura"], "ans": "(A)", "exp": "Gandhiji started his famous 240-mile Salt March from Sabarmati Ashram."},
    {"q": "Which incident led Mahatma Gandhi to halt the Non-Cooperation Movement in 1922?", "options": ["(A) Jallianwala Bagh incident", "(B) Chauri Chaura incident", "(C) Kakori conspiracy", "(D) Rowlatt Act passage"], "ans": "(B)", "exp": "The violent incident at Chauri Chaura in Gorakhpur led Gandhiji to withdraw the movement."},
    {"q": "Who authored the famous book 'Anandamath' containing Vande Mataram?", "options": ["(A) Rabindranath Tagore", "(B) Bankim Chandra Chattopadhyay", "(C) Abanindranath Tagore", "(D) Sarat Chandra Chattopadhyay"], "ans": "(B)", "exp": "Bankim Chandra Chattopadhyay wrote Anandamath, which included Vande Mataram."},
    {"q": "What was the main outcome of the Poona Pact of September 1932?", "options": ["(A) Separate electorates for Dalits", "(B) Reserved seats for Depressed Classes in council elections", "(C) Complete Independence declaration", "(D) End of Salt Satyagraha"], "ans": "(B)", "exp": "The Poona Pact gave Depressed Classes reserved seats in provincial and central legislative councils."},
    {"q": "Which region was known as the 'powder keg' of Europe before WWI?", "options": ["(A) The Balkans", "(B) The Baltic states", "(C) The Iberian Peninsula", "(D) Scandinavia"], "ans": "(A)", "exp": "The Balkans was a region of intense ethnic conflict and nationalist tension before WWI."},
    {"q": "Who formed the 'Young Italy' secret society?", "options": ["(A) Giuseppe Mazzini", "(B) Metternich", "(C) Garibaldi", "(D) Cavour"], "ans": "(A)", "exp": "Giuseppe Mazzini founded the secret society 'Young Italy' in Marseilles."}
]

geography_questions = [
    {"q": "In which year was the Earth Summit held in Rio de Janeiro?", "options": ["(A) 1990", "(B) 1992", "(C) 1997", "(D) 2002"], "ans": "(B)", "exp": "The first International Earth Summit was held in Rio de Janeiro, Brazil, in 1992."},
    {"q": "Which of the following soils is most ideal for growing cotton and is known as regur soil?", "options": ["(A) Red soil", "(B) Laterite soil", "(C) Black soil", "(D) Arid soil"], "ans": "(C)", "exp": "Black soil, also known as regur soil, is ideal for growing cotton."},
    {"q": "Resources which are obtained from the biosphere and have life are known as:", "options": ["(A) Biotic Resources", "(B) Abiotic Resources", "(C) Renewable Resources", "(D) Potential Resources"], "ans": "(A)", "exp": "Biotic resources are obtained from the biosphere and have life."},
    {"q": "Which of the following crops is a rabi crop in India?", "options": ["(A) Rice", "(B) Wheat", "(C) Maize", "(D) Jowar"], "ans": "(B)", "exp": "Wheat is a principal rabi crop sown in winter and harvested in spring."},
    {"q": "Which one of the following is the staple food crop of the majority of people in India?", "options": ["(A) Wheat", "(B) Millets", "(C) Maize", "(D) Rice"], "ans": "(D)", "exp": "Rice is the staple food crop for the majority of people in India."},
    {"q": "What is 'Jhumming' in India?", "options": ["(A) A type of commercial farming", "(B) A method of manufacturing", "(C) Shifting cultivation", "(D) A type of plantation agriculture"], "ans": "(C)", "exp": "Jhumming is the local name for shifting cultivation in north-eastern India."},
    {"q": "Which state is the largest producer of bauxite in India?", "options": ["(A) Jharkhand", "(B) Odisha", "(C) Gujarat", "(D) Chhattisgarh"], "ans": "(B)", "exp": "Odisha is the largest bauxite-producing state in India."},
    {"q": "Which type of resource is solar energy?", "options": ["(A) Non-renewable", "(B) Replenishable / Renewable", "(C) Abiotic", "(D) Non-recyclable"], "ans": "(B)", "exp": "Solar energy can be renewed or replenished naturally."},
    {"q": "In which state is the Sariska Tiger Reserve located?", "options": ["(A) Madhya Pradesh", "(B) Rajasthan", "(C) Assam", "(D) Kerala"], "ans": "(B)", "exp": "Sariska Tiger Reserve is located in Rajasthan."},
    {"q": "Which dam is constructed on the River Narmada as part of the Sardar Sarovar Project?", "options": ["(A) Bhakra Nangal Dam", "(B) Tehri Dam", "(C) Sardar Sarovar Dam", "(D) Hirakud Dam"], "ans": "(C)", "exp": "Sardar Sarovar Dam is built over the Narmada River in Gujarat."},
    {"q": "Which state in India has made rooftop rainwater harvesting compulsory for all houses?", "options": ["(A) Tamil Nadu", "(B) Rajasthan", "(C) Meghalaya", "(D) Karnataka"], "ans": "(A)", "exp": "Tamil Nadu is the first state in India to make rooftop rainwater harvesting compulsory."},
    {"q": "Which crop is known as the 'Golden Fibre' of India?", "options": ["(A) Cotton", "(B) Silk", "(C) Jute", "(D) Hemp"], "ans": "(C)", "exp": "Jute is known as the Golden Fibre because of its color and economic value."},
    {"q": "Kudremukh iron ore mines are located in which state?", "options": ["(A) Karnataka", "(B) Odisha", "(C) Chhattisgarh", "(D) Goa"], "ans": "(A)", "exp": "Kudremukh mines are located in the Western Ghats of Karnataka."},
    {"q": "Which port is a tidal port located in Gujarat?", "options": ["(A) Mumbai Port", "(B) Marmagao Port", "(C) Kandla Port", "(D) Haldia Port"], "ans": "(C)", "exp": "Kandla in Kuchchh is a tidal port constructed after independence."},
    {"q": "Red soil develops a reddish color due to:", "options": ["(A) High humus content", "(B) Diffusion of iron in crystalline and metamorphic rocks", "(C) High moisture retention", "(D) Accumulation of lime content"], "ans": "(B)", "exp": "Diffusion of iron in crystalline and metamorphic rocks gives red soil its characteristic color."}
]

civics_questions = [
    {"q": "Which two languages are spoken by the majority of people in Belgium?", "options": ["(A) French and German", "(B) Dutch and French", "(C) English and Dutch", "(D) German and Italian"], "ans": "(B)", "exp": "59% speak Dutch and 40% speak French in Belgium."},
    {"q": "Which legal act was passed in Sri Lanka in 1956 to establish Sinhala dominance?", "options": ["(A) An Act recognizing Sinhala as the sole official language", "(B) An Act creating a federal government", "(C) An Act establishing Tamil as an official language", "(D) An Act declaring Sri Lanka a republic"], "ans": "(A)", "exp": "In 1956, an Act was passed in Sri Lanka recognizing Sinhala as the only official language."},
    {"q": "Subjects of national importance, such as Defense, Foreign Affairs, and Banking, are included in which list?", "options": ["(A) State List", "(B) Concurrent List", "(C) Union List", "(D) Residuary List"], "ans": "(C)", "exp": "The Union List includes subjects of national importance."},
    {"q": "Which third tier of government was reinforced through the 1992 Constitutional Amendment?", "options": ["(A) Union Territory Government", "(B) Panchayati Raj / Local Self-Government", "(C) State Assembly", "(D) Supreme Court Directorate"], "ans": "(B)", "exp": "The 73rd and 74th Amendments reinforced local self-governments."},
    {"q": "Which of the following is a recognized 'National Party' in India?", "options": ["(A) Samajwadi Party", "(B) Bharatiya Janata Party (BJP)", "(C) Rashtriya Janata Dal", "(D) DMK"], "ans": "(B)", "exp": "BJP is a recognized National Party in India."},
    {"q": "Power shared among different organs of government (Legislature, Executive, Judiciary) is called:", "options": ["(A) Vertical distribution", "(B) Horizontal distribution", "(C) Federal division", "(D) Coalition government"], "ans": "(B)", "exp": "Horizontal distribution places organs of government at the same level."},
    {"q": "Which type of government exists in Belgium to represent cultural and linguistic interests?", "options": ["(A) Unitary Government", "(B) Community Government", "(C) Military Rule", "(D) Dictatorship"], "ans": "(B)", "exp": "Belgium has a third tier called 'Community Government'."},
    {"q": "Subjects like Education, Forests, and Trade Unions fall under which list in India?", "options": ["(A) Union List", "(B) State List", "(C) Concurrent List", "(D) Residuary List"], "ans": "(C)", "exp": "The Concurrent List includes subjects of common interest to both Central and State Governments."},
    {"q": "What is the official state religion of Sri Lanka according to its Constitution?", "options": ["(A) Hinduism", "(B) Buddhism", "(C) Islam", "(D) Christianity"], "ans": "(B)", "exp": "The Constitution of Sri Lanka states that the state shall protect and foster Buddhism."},
    {"q": "A government formed by an alliance of two or more political parties is known as a:", "options": ["(A) Single-party government", "(B) Coalition government", "(C) Federal government", "(D) Unitary government"], "ans": "(B)", "exp": "A Coalition government is formed by two or more parties coming together."},
    {"q": "How many languages are scheduled in the Eighth Schedule of the Indian Constitution?", "options": ["(A) 18", "(B) 20", "(C) 22", "(D) 25"], "ans": "(C)", "exp": "There are 22 languages recognized as Scheduled Languages in the 8th Schedule."},
    {"q": "Who is the head of a Municipal Corporation?", "options": ["(A) Sarpanch", "(B) Mayor", "(C) Collector", "(D) Governor"], "ans": "(B)", "exp": "The political head of a Municipal Corporation is called the Mayor."},
    {"q": "In which system of government is power divided between a central authority and constituent units?", "options": ["(A) Federalism", "(B) Unitary System", "(C) Monarchy", "(D) Oligarchy"], "ans": "(A)", "exp": "Federalism divides power between central and regional authorities."},
    {"q": "Which party system exists in India?", "options": ["(A) One-party system", "(B) Two-party system", "(C) Multi-party system", "(D) Bi-party system"], "ans": "(C)", "exp": "India has a multi-party system with several regional and national parties."},
    {"q": "Democracy is considered a better form of government because it:", "options": ["(A) Promotes equality among citizens", "(B) Enhances dignity of the individual", "(C) Allows room to correct mistakes", "(D) All of the above"], "ans": "(D)", "exp": "Democracy promotes equality, enhances dignity, and provides mechanisms to fix errors."}
]

economics_questions = [
    {"q": "Which international body publishes the Human Development Index (HDI)?", "options": ["(A) World Bank", "(B) IMF", "(C) UNDP", "(D) WTO"], "ans": "(C)", "exp": "The UNDP publishes the Human Development Report."},
    {"q": "Activities involving extraction of natural resources belong to which sector?", "options": ["(A) Primary Sector", "(B) Secondary Sector", "(C) Tertiary Sector", "(D) Quaternary Sector"], "ans": "(A)", "exp": "The Primary sector directly uses natural resources."},
    {"q": "Which organization in India issues currency notes on behalf of the Central Government?", "options": ["(A) State Bank of India", "(B) Reserve Bank of India", "(C) Ministry of Finance", "(D) NITI Aayog"], "ans": "(B)", "exp": "The Reserve Bank of India issues currency notes."},
    {"q": "What is a essential requirement of the barter system?", "options": ["(A) Double coincidence of wants", "(B) Collateral system", "(C) Deferred payment", "(D) Credit agreement"], "ans": "(A)", "exp": "Double coincidence of wants is required for barter exchanges."},
    {"q": "Which process describes the rapid integration between countries through trade and investment?", "options": ["(A) Privatization", "(B) Urbanization", "(C) Globalization", "(D) Decentralization"], "ans": "(C)", "exp": "Globalization integrates economies worldwide."},
    {"q": "The sum of total production of goods and services in all three sectors of a country in a year is called:", "options": ["(A) Gross Domestic Product (GDP)", "(B) Net National Product (NNP)", "(C) Per Capita Income", "(D) National Revenue"], "ans": "(A)", "exp": "GDP is the total value of final goods and services produced in all three sectors."},
    {"q": "Disguised unemployment is most commonly found in which sector in India?", "options": ["(A) Agriculture Sector", "(B) Industrial Sector", "(C) IT Sector", "(D) Banking Sector"], "ans": "(A)", "exp": "Agriculture suffers from disguised unemployment where more people work than needed."},
    {"q": "Money or asset pledged as a guarantee to a lender until the loan is repaid is called:", "options": ["(A) Credit", "(B) Deposit", "(C) Collateral", "(D) Interest"], "ans": "(C)", "exp": "Collateral is an asset that the borrower owns and pledges to the lender."},
    {"q": "In which sector are workers provided job security, medical benefits, and fixed working hours?", "options": ["(A) Unorganized Sector", "(B) Organized Sector", "(C) Informal Sector", "(D) Primary Sector"], "ans": "(B)", "exp": "The Organized sector covers enterprises with registered, secure employment."},
    {"q": "Per Capita Income is calculated by dividing National Income by the country's:", "options": ["(A) Total Area", "(B) Total Population", "(C) Total Working Population", "(D) Total Exports"], "ans": "(B)", "exp": "Per Capita Income = Total Income of Country / Total Population."},
    {"q": "Which sector has emerged as the largest producing sector in India in recent decades?", "options": ["(A) Primary Sector", "(B) Secondary Sector", "(C) Tertiary (Service) Sector", "(D) Agricultural Sector"], "ans": "(C)", "exp": "The Tertiary (Service) sector has become the largest contributor to India's GDP."},
    {"q": "Removing barriers or restrictions set by the government on international trade is known as:", "options": ["(A) Globalization", "(B) Liberalization", "(C) Privatization", "(D) Industrialization"], "ans": "(B)", "exp": "Removing trade barriers or restrictions is called Liberalization."},
    {"q": "MNCs stand for:", "options": ["(A) Multi-National Corporations", "(B) Multi-National Companies", "(C) Multi-National Centers", "(D) Multi-National Councils"], "ans": "(A)", "exp": "MNCs are Multinational Corporations that own or control production in more than one nation."},
    {"q": "Which agency sets quality standards for food items in India like ISI or Agmark?", "options": ["(A) Consumer Forum", "(B) Bureau of Indian Standards (BIS)", "(C) NITI Aayog", "(D) FCI"], "ans": "(B)", "exp": "BIS issues quality certification standards (like ISI mark and Agmark)."},
    {"q": "Self-Help Groups (SHGs) usually consist of how many members, typically women from neighboring areas?", "options": ["(A) 5 to 10", "(B) 15 to 20", "(C) 50 to 100", "(D) 100 to 200"], "ans": "(B)", "exp": "A typical SHG has 15-20 members who meet and save regularly."}
]

all_sections = [
    (history_questions, "hist", "📜 History"),
    (geography_questions, "geo", "🌍 Geography"),
    (civics_questions, "civ", "🏛️ Civics"),
    (economics_questions, "eco", "📈 Economics")
]

# Initialize state keys for all question options
for questions, prefix, _ in all_sections:
    for idx in range(len(questions)):
        key_name = f"ans_{prefix}_{idx}"
        if key_name not in st.session_state:
            st.session_state[key_name] = None

# ==========================================
# TEST START SCREEN & QUESTIONS DISPLAY
# ==========================================

if not st.session_state.quiz_started and not st.session_state.quiz_submitted:
    st.info("📌 **Instructions:** Select your desired mode in the sidebar, then click **Start Test Now** below to begin.")
    if st.button("🚀 Start Test Now", type="primary", use_container_width=True):
        st.session_state.quiz_started = True
        st.session_state.start_time = time.time()
        st.rerun()

elif st.session_state.quiz_started and not st.session_state.quiz_submitted:
    st.write("Select your options across all 4 subjects, then click **Submit Entire Quiz** at the bottom!")

    tabs = st.tabs([title for _, _, title in all_sections])

    for i, (questions, prefix, title) in enumerate(all_sections):
        with tabs[i]:
            st.header(f"{title} Section ({len(questions)} Questions)")
            for idx, item in enumerate(questions):
                st.subheader(f"Q{idx + 1}. {item['q']}")
                
                key_name = f"ans_{prefix}_{idx}"
                st.radio(
                    label=f"q_{prefix}_{idx}",
                    options=item["options"],
                    key=key_name,
                    index=None,
                    label_visibility="collapsed"
                )
                st.divider()

    if st.button("Submit Entire Quiz 🚀", type="primary", use_container_width=True):
        st.session_state.quiz_submitted = True
        st.rerun()

# ==========================================
# RESULTS & DETAILED ANSWER KEY (POST-SUBMISSION)
# ==========================================

if st.session_state.quiz_submitted:
    # Trigger balloons ONCE upon submission
    if not st.session_state.balloons_shown:
        st.balloons()
        st.session_state.balloons_shown = True

    total_correct = 0
    total_incorrect = 0
    total_unattempted = 0
    total_questions = sum(len(q_list) for q_list, _, _ in all_sections)
    section_scores = {}

    for questions, prefix, title in all_sections:
        sec_score = 0
        for idx, item in enumerate(questions):
            user_choice = st.session_state.get(f"ans_{prefix}_{idx}")
            if user_choice is None:
                total_unattempted += 1
            elif item["ans"] in user_choice:
                sec_score += 1
                total_correct += 1
            else:
                total_incorrect += 1

        section_scores[title] = (sec_score, len(questions))

    st.header("🏆 Final Quiz Scorecard")
    percentage = (total_correct / total_questions) * 100

    # TOP OVERALL SCORE METRICS
    m1, m2, m3, m4 = st.columns(4)
    m1.metric(label="Total Score", value=f"{total_correct} / {total_questions}", delta=f"{percentage:.1f}%")
    m2.metric(label="✅ Correctly Attempted", value=f"{total_correct}")
    m3.metric(label="❌ Incorrectly Attempted", value=f"{total_incorrect}")
    m4.metric(label="⚠️ Left Unattended", value=f"{total_unattempted}")

    st.divider()

    # SECTION BREAKDOWN METRICS
    st.write("### 📊 Subject-Wise Marks Breakdown")
    cols = st.columns(4)
    for idx, (title, (score, total)) in enumerate(section_scores.items()):
        cols[idx].metric(label=title, value=f"{score} / {total}")

    if percentage >= 80:
        st.success("🎉 Outstanding Performance! You are board-exam ready!")
    elif percentage >= 50:
        st.warning("👍 Good Attempt! Go through the answer key below to review weak topics.")
    else:
        st.error("💡 Needs Improvement! Check the detailed answers below and revise NCERT chapters.")

    st.divider()

    # DETAILED ANSWER KEY SECTION
    st.header("🔑 Detailed Answer Key & Explanations")

    answer_tabs = st.tabs([f"Answers: {title}" for _, _, title in all_sections])

    for i, (questions, prefix, title) in enumerate(all_sections):
        with answer_tabs[i]:
            st.write(f"### {title} Review")
            for idx, item in enumerate(questions):
                user_choice = st.session_state.get(f"ans_{prefix}_{idx}")
                
                if user_choice is None:
                    status_str = "⚠️ Left Unattended"
                    display_choice = "None Selected"
                elif item["ans"] in user_choice:
                    status_str = "✅ Correct"
                    display_choice = user_choice
                else:
                    status_str = "❌ Incorrect"
                    display_choice = user_choice

                with st.expander(f"Q{idx + 1}: {item['q']} - {status_str}"):
                    st.write(f"**Your Selected Answer:** {display_choice}")
                    st.write(f"**Correct Answer:** {item['ans']}")
                    st.info(f"**Explanation:** {item['exp']}")
