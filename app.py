import streamlit as st

st.title("CBSE Class 10 Social Science Board Revision Quiz")

# Question Bank
questions = [
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
    },
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

# Display Questions using Loop
for idx, item in enumerate(questions):
    st.subheader(f"Question {idx + 1}")
    st.write(item["q"])
    
    # Key parameter prevents Streamlit duplicate errors
    choice = st.radio("Select your option:", item["options"], key=f"radio_{idx}")
    
    if st.button("Submit Answer", key=f"btn_{idx}"):
        if item["ans"] in choice:
            st.success(f"You are correct! 🎉 {item['exp']}")
        else:
            st.error("It is wrong. Try harder next time! 💡")
    st.divider()
  
