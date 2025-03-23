import streamlit as st
from agents import AgentManager
manager = AgentManager(llm_provider="local", max_retries=3, debug=True)

def reset():
    for key in st.session_state.keys():
        del st.session_state[key]

def landing_page():
    st.title('Stock Analysis Assistant')
    ticker = st.text_input('Enter the stock ticker you want to analyze: (e.g. APPLE, TESLA, etc.)')

    if ticker:
        st.write(f"You have entered the stock ticker: {ticker}")

        # Reset results when the ticker changes
        if ticker != st.session_state.get("last_ticker"):
            reset()
            st.session_state.last_ticker = ticker

        st.write("Please select the type of analysis you would like to perform:")
        analysis_type = st.selectbox("Select the type of analysis", ["Technical Analysis", "Fundamental Analysis", "Recommendation"])

        if analysis_type == "Technical Analysis":
            st.write("You have selected Technical Analysis")
            st.write("Technical Analysis is the study of past market data, primarily price and volume, to forecast future price movements.")
            st.write("Technical analysts use charts and technical indicators to identify patterns that can suggest future price movements.")
            st.write("Technical analysis does not consider the intrinsic value of a stock, but rather focuses on historical price movements and trends.")
            st.write("Technical analysis can be used to identify entry and exit points for trades.")
        elif analysis_type == "Fundamental Analysis":
            st.write("You have selected Fundamental Analysis")
            st.write("Fundamental Analysis is the study of a company's financial statements and health.")
            st.write("Fundamental analysts look at financial ratios, management, growth prospects, and the competitive landscape.")
            st.write("Fundamental analysis aims to determine the intrinsic value of a security.")
            st.write("Fundamental analysis can be used to identify undervalued or overvalued stocks.")
        elif analysis_type == "Recommendation":
            st.write("You have selected Recommendation")
            st.write("Recommendation combines both Technical and Fundamental Analysis to make informed decisions about buying, selling, or holding a stock.")
            st.write("Recommendation considers both the intrinsic value of a stock and its historical price movements.")
            st.write("Recommendation can help investors make informed decisions about their stock portfolio.")
        else:
            st.write("Please select a valid analysis type.")

        st.write("Click on the 'Analyze' button to proceed with the analysis.")
            
        if st.button("Analyze"):
            if ticker:
                st.write(f"Analyzing {ticker.upper()}...")
                if analysis_type == "Technical Analysis":
                    st.write("Performing Technical Analysis...")
                    ta_agent = manager.get_agent("decision")
                    st.session_state.technical_analysis = ta_agent.run(ticker)
                elif analysis_type == "Fundamental Analysis":
                    st.write("Performing Fundamental Analysis...")
                    fa_agent = manager.get_agent("fundamental")
                    st.session_state.fundamental_analysis = fa_agent.run(ticker)
                elif analysis_type == "Recommendation":
                    st.write("Finalizing Recommendation...")
                    fa_agent = manager.get_agent("fundamental")
                    ta_agent = manager.get_agent("technical")
                    decision_agent = manager.get_agent("decision")
                    st.session_state.fundamental_analysis = fa_agent.run(ticker)
                    st.session_state.technical_analysis = ta_agent.run(ticker)
                    st.session_state.final_decision = decision_agent.run(
                        ticker,
                        st.session_state.fundamental_analysis,
                        st.session_state.technical_analysis
                    )
                else:
                    st.write("Please select a valid analysis type.")
            else:
                st.write("Please enter a valid stock ticker.")

    if st.session_state.get("fundamental_analysis"):
        st.subheader("Fundamental Analysis:")
        st.write(st.session_state.fundamental_analysis)
    if st.session_state.get("technical_analysis"):
        st.subheader("Technical Analysis:")
        st.write(st.session_state.technical_analysis)
    if st.session_state.get("final_decision"):
        st.subheader("Recommendation:")
        st.write(st.session_state.final_decision)

#landing_page()

def alternate_landing_page():
    # Sidebar Inputs
    st.sidebar.header("Stock Analysis Settings")
    ticker = st.sidebar.text_input("Stock Ticker (e.g., AAPL, TSLA)", key="ticker_input")

    # Reset results when ticker changes
    if ticker != st.session_state.get("last_ticker"):
        reset()
        st.session_state.last_ticker = ticker

    analysis_type = st.sidebar.selectbox(
        "Select Analysis Type",
        ["Technical Analysis", "Fundamental Analysis", "Recommendation"],
        key="analysis_type"
    )

    st.title("📈 Stock Analysis Assistant")

    # Explanation of Analysis Types
    analysis_descriptions = {
        "Technical Analysis": "Technical Analysis studies past market data (price, volume) to predict future movements.",
        "Fundamental Analysis": "Fundamental Analysis evaluates a company's financial health, growth, and intrinsic value.",
        "Recommendation": "A Recommendation combines both Technical and Fundamental analysis for a final investment decision."
    }
    st.info(analysis_descriptions[analysis_type])

    if st.sidebar.button("Analyze"):
        if ticker:
            st.write(f"🔍 Analyzing **{ticker.upper()}**...")

            if analysis_type == "Technical Analysis":
                ta_agent = manager.get_agent("technical")
                st.session_state.technical_analysis = ta_agent.run(ticker.upper())

            elif analysis_type == "Fundamental Analysis":
                fa_agent = manager.get_agent("fundamental")
                st.session_state.fundamental_analysis = fa_agent.run(ticker.upper())

            elif analysis_type == "Recommendation":
                fa_agent = manager.get_agent("fundamental")
                ta_agent = manager.get_agent("technical")
                decision_agent = manager.get_agent("decision")

                st.session_state.fundamental_analysis = fa_agent.run(ticker.upper())
                st.session_state.technical_analysis = ta_agent.run(ticker.upper())
                st.session_state.final_decision = decision_agent.run(
                    ticker.upper(),
                    st.session_state.fundamental_analysis,
                    st.session_state.technical_analysis
                )

        else:
            st.warning("⚠️ Please enter a valid stock ticker before analyzing.")

    # Display Results in Expandable Sections
    if st.session_state.get("fundamental_analysis"):
        with st.expander("📊 **Fundamental Analysis**", expanded=True):
            st.markdown(f"**Results:**\n\n{st.session_state.fundamental_analysis}")

    if st.session_state.get("technical_analysis"):
        with st.expander("📉 **Technical Analysis**", expanded=True):
            st.markdown(f"**Results:**\n\n{st.session_state.technical_analysis}")

    if st.session_state.get("final_decision"):
        with st.expander("📢 **Final Recommendation**", expanded=True):
            st.markdown(f"**Decision:**\n\n{st.session_state.final_decision}")

alternate_landing_page()