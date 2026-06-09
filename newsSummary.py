from dotenv import load_dotenv
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables
load_dotenv()

# Initialize Tavily Search Tool
search_tool = TavilySearchResults(max_results=5)

# Initialize Mistral LLM
llm = ChatMistralAI(
    model="mistral-small-2506"
)

# Prompt Template
prompt = ChatPromptTemplate.from_template(
    """
You are a professional news analyst.

Your task is to summarize the provided news content.

Instructions:
- Create clear bullet points.
- Keep each point concise.
- Focus only on key developments.
- Remove duplicate information.
- Use simple language.

News Content:
{news}
"""
)

# Create LangChain pipeline
chain = prompt | llm | StrOutputParser()


def summarize_news(topic: str):
    try:
        print(f"\n🔍 Searching latest news about: {topic}...\n")

        news_results = search_tool.run(f"Latest {topic} news")

        print("📝 Generating summary...\n")

        summary = chain.invoke({
            "news": news_results
        })

        print("=" * 60)
        print("NEWS SUMMARY")
        print("=" * 60)
        print(summary)
        print("=" * 60)

    except Exception as e:
        print(f"❌ Error: {e}")


def main():
    print("\n📰 AI News Summarizer")
    print("Type 'exit' to quit\n")

    while True:
        topic = input("Enter a topic: ")

        if topic.lower() == "exit":
            print("Goodbye!")
            break

        summarize_news(topic)


if __name__ == "__main__":
    main()