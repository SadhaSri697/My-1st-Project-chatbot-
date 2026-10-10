data_of_companies = {
    "apple": {
        "display_name": "Apple",
        "fiscal_year": 2025,       # it's like "sadha" : {forever,life long etc}
        "total_revenue": 416161,
        "net_income": 112010,
        "net_income_prior_year": 93736,
        "net_income_growth_pct": 20,
        "total_assets": 359240,
        "total_liabilities": 285510,
        "operating_cash_flow": 111482,
        "net_margin_pct": 27,
    },
    "microsoft": {
        "display_name": "Microsoft",
        "fiscal_year": 2025,
        "total_revenue": 281724,
        "net_income": 101832,
        "net_income_prior_year": 88136,
        "net_income_growth_pct": 16,
        "total_assets": 619003,
        "total_liabilities": 275524,
        "operating_cash_flow": 136171,
        "net_margin_pct": 36,
    },
    "tesla": {
        "display_name": "Tesla",
        "fiscal_year": 2025,
        "total_revenue": 94827,
        "net_income": 3794,
        "net_income_prior_year": 7091,
        "net_income_growth_pct": -46,
        "total_assets": 137806,
        "total_liabilities": 54941,
        "operating_cash_flow": 14747,
        "net_margin_pct": 4,
    }
}

short_cuts = {
    "apple": "apple",
    "aapl": "apple",
    "microsoft": "microsoft",
    "msft": "microsoft",
    "tesla": "tesla",
    "tsla": "tesla",
}

'''
Supported predefined queries (company name required in the question):
      1. "What is the total revenue for <company>?"
      2. "How has net income changed over the last year for <company>?"
      3. "What are the total assets for <company>?"
      4. "What is the net margin for <company>?"
      5. "Which company had the highest revenue growth?"
      6. "What is total liabilities for <company>?"
      7. "What is operating cash flow for <company>?"
'''      

def find_company(question : str):
    question_lower = question.lower()
    for key , key_words in short_cuts.items():
        if key in question_lower:
            return key_words
    return None    
                
def find_money(amout:int) -> str:
    return f"${amout:,} millon"

def simple_chatbot(question : str) -> str:
    question_lower = question.strip().lower()
    key_words = find_company(question_lower)

    #Question 1
    if "total revenue" in question_lower and key_words:
        data = data_of_companies[key_words]
        return(
            f"{data['display_name']}'s Total Revenue for FY{data['fiscal_year']}"
            f" was {find_money(data['total_revenue'])}."
        )
    #Question 2
    elif "net income" in question_lower and "chang" in question_lower and key_words:
        data = data_of_companies[key_words]
        direction = "increased" if data['net_income_prior_year'] >= 0 else "decreased"
        return(
            f"the net income of {data['display_name']} is {find_money(data['net_income'])}"
            f" and last year is {find_money(data['net_income_prior_year'])}"
            f" it got {direction} to {data['net_income_growth_pct']}%" 
            f" over a year in FY{data['fiscal_year']}."
        )
    #Question 3
    elif "total assets" in question_lower and key_words:
        data = data_of_companies[key_words]
        return(
            f"The Total Assets of {data['display_name']} is {find_money(data['total_assets'])}"
            f"in year FY{data['fiscal_year']}."
        )
    #Question 4
    elif "net margin" in question_lower and key_words:
        data = data_of_companies[key_words]
        return(
            f"{data['display_name']}'s net mergin for FY{data['fiscal_year']}"
            f" was approximately {data['net_margin_pct']}%."
        )
    #Question 5
    elif "highest revenue growth" in question_lower:
        return(
            "Based on FY2025 figures, Microsoft had the highest revenue growth "
            "(about 15% year-over-year), ahead of Apple (about 6%) and Tesla "
            "(about -3%, a slight decline)."
        )
    #Question 6
    elif "total liabilities" in question_lower and key_words:
        data = data_of_companies[key_words]
        return(
            f"{data['display_name']}'s total liabilities for FY{data['fiscal_year']}"
            f" were {find_money(data['total_liabilities'])}."
        )
    #Question 7
    elif "operating cash flow" in question_lower and key_words:
        data = data_of_companies[key_words]
        return(
            f"{data['display_name']}'s operating cash flow for FY{data['fiscal_year']}"
            f" were {find_money(data['operating_cash_flow'])}."
        )
    else:
        return (
            "Sorry, I can only answer predefined questions about total revenue, "
            "net income change, total assets, net margin, operating cash flow, "
            "total liabilities or revenue growth "
            "comparisons for Apple, Microsoft, or Tesla. Please include a "
            "company name in your question."
        )

def run_cli():
    print("Financial Analysis Chatbot (prototype)")
    print("Ask about Apple, Microsoft, or Tesla's revenue, net income change,")
    print("total assets, net margin, operating cash flow, total liabilitiesor or revenue growth. Type 'quit' to exit.\n")  
    while True:
        question = input("YOU: ")   
        if question.strip().lower() in ("quit","exit"):
            print("CHATBOT: Goodbye!")   
            break
        print("CHATBOT:",simple_chatbot(question))

if __name__ == "__main__":
    run_cli()


 
      