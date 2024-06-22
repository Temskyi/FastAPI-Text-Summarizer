from langchain_huggingface.llms import HuggingFacePipeline
from langchain_core.prompts import PromptTemplate


class TextSummarizer:
    # Model Loading
    hf = HuggingFacePipeline.from_model_id(
        model_id="Falconsai/text_summarization",
        task="summarization",
    )

    # Create Chain
    prompt = PromptTemplate.from_template("{text}")
    chain = prompt | hf

    @classmethod
    def summarize(cls, text: str) -> str:
        """
            :param text: Text to summarize
            :return: The summarized text
        """
        return cls.chain.invoke({"text": text})
