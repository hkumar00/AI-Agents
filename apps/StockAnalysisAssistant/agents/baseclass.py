from abc import ABC, abstractmethod
import pandas as pd
import ollama
from loguru import logger


class BaseAgent(ABC):
    def __init__(self, name, llm_provider, max_retries=3, debug=False):
        self.LLMProvider = llm_provider
        self.max_retries = max_retries
        self.debug = debug
        self.agentName = name
        self.callLLM = None

        if llm_provider == "local":
            self.callLLM = self.call_ollama
        elif llm_provider == "chatgpt":
            self.callLLM = self.call_chatgpt
        else:
            raise ValueError("Invalid LLM provider")

    @abstractmethod
    def run(self, *args, **kwargs):
        pass

    def call_ollama(self, messages, temperature=0.7, max_tokens=200):
        iteration = 0
        while iteration < self.max_retries:
            try:
                if self.debug:
                    logger.info(f"[{self.agentName} to LLM]:\n")
                    for message in messages:
                        logger.info(f"{message['role']} --> {message['content']}")
                response = ollama.chat(
                    model = "llama3.2:3b",
                    messages = messages,
                    options={"temperature": temperature, "max_tokens": max_tokens}
                )
                llmResponse = response['message']['content']
                if self.debug:
                    logger.info(f"LLM to [{self.agentName}]: {llmResponse}")
                return llmResponse
            except Exception as e:
                iteration += 1
                logger.error(f"{self.agentName} encountered an error: {e}")
                logger.error(f"Used {iteration} out of {self.max_retries} retries")
                continue
        else:
            raise Exception(f"{self.agentName} failed to get a response from LLM, exhausted all {self.max_retries} retries")

    def call_chatgpt(self, messages, temperature=0.7, max_tokens=100):
        pass

