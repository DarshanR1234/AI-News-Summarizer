from dotenv import load_dotenv
load_dotenv()
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

search_tool = TavilySearchResults(max_result = 5)

llm = ChatMistralAI(model = "mistral-small-2506"
                    )

prompt = ChatPromptTemplate.from_template(
    """
You are a helpful assistant

summarize the following news into clear bullet points

{news}
"""
)

chain = prompt | llm | StrOutputParser()

while True:
    query = input("Enter your news query (or 'exit' to quit): ").strip()
    if query.lower() in ('exit', 'quit', 'q'):
        print("Goodbye.")
        break

    news_result = search_tool.run(query)
    result = chain.invoke({"news": news_result})

    print("\nSummary:\n")
    print(result)
    print("\n---\n")



