# -*- coding: utf-8 -*-
import requests
import time
from chatterbot import ChatBot

# Create a new chat bot named Charlie
chatbot = ChatBot("Char",
                  storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
                  # filters=['chatterbot.filters.RepetitiveResponseFilter'],
                  database='chatterbot-database',
                  # logic_adapters=[
                       # "chatterbot.adapters.logic.approximate_sentence_match.ApproximateSentenceMatchAdapter",
                       # "chatterbot.adapters.logic.sentiment_adapter.SentimentAdapter",
                       # "chatterbot.adapters.logic.closest_meaning.ClosestMeaningAdapter",
                      # "chatterbot.adapters.logic.no_knowledge_adapter.NoKnowledgeAdapter",
                  #       "chatterbot.adapters.logic.no_logic.NoLogic",
                  #     "chatterbot.adapters.logic.closest_match.ClosestMatchAdapter",
                      # "chatterbot.adapters.logic.mathematical_evaluation.MathematicalEvaluation",
                      # "chatterbot.adapters.logic.time_adapter.TimeLogicAdapter"
                      # "chatterbot.adapters.logic.multi_adapter.MultiLogicAdapter"

                  # ],
                  silence_performance_warning=True)

# Get a response to the input "How are you?"


content = "又来了"
while True:
    weixin_url = "http://127.0.0.1:3000/openwx/consult?account=xiaoice-ms&content=" + content  # ms-xiaoice xiaoirobot
    reply = requests.get(weixin_url,timeout=50).json()
    reply = reply["reply"]
    print("小冰："),
    print(reply)
    # time.sleep(7)
    content = reply

    response = chatbot.get_response(content)
    print("Charlie Brown:"),
    print(response)
    content = response.text


    tu_lin_url = "http://www.tuling123.com/openapi/api?key=28deb3371d214504aa1de28886b08418&info=" + content
    content = requests.get(tu_lin_url, timeout=50).json()
    content = content["text"]
    print("图图："),
    print(content)
    time.sleep(3)

    response = chatbot.get_response(content)
    print("Charlie Brown:"),
    print(response)
    content = response.text


    tu_lin_url = "http://i.itpk.cn/api.php?api_key=b91eb483fce9f245bf4769b764611ddb&" \
                "api_secret=ad402p9evmlp&limit=8&question="+content
    content = requests.get(tu_lin_url, timeout=50)   # ITPK茉莉机器人
    content = content.text
    time.sleep(3)
    print("茉莉："),
    print(content)


    response = chatbot.get_response(content)
    print("查理:"),
    print(response)
    content = response.text

    tu_lin_url = "http://api.qingyunke.com/api.php?key=free&appid=0&msg=" + content
    reply = requests.get(tu_lin_url, timeout=50).json()
    content = reply["content"]
    print("云云："),
    print (content)
    # time.sleep(3)

    response = chatbot.get_response(content)
    print("Charlie Brown:"),
    print(response)
    content = response.text


