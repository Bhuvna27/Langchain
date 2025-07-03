from langchain import PromptTemplate

template = """Question: {question}  


Answer: """
prompt = PromptTemplate(template=template,input_variables = ['question'])

question = "Which NFL team do you think will win the Super Bowl in the 2010 season?"

import os
os.environ['HUGGINGFACEHUB_API_TOKEN'] = ''
