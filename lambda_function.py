import json
import boto3

### You can choose one of three options below ###
DEEPSEEK_R1_Llama_8B_IMPORTED_MODEL = 'Enter the Model ARN generated after importing the model from the Bedrock custom import model'
  # e.g. DEEPSEEK_R1_Llama_8B_IMPORTED_MODEL = "arn:aws:bedrock:us-west-2:[YOUR_ACCOUNT_ID]:imported-model/xxxxxxxxx"
DEEPSEEK_R1_Llama_8B_MARKET_PLACE = 'Enter the Sagemaker Endpoint ARN created after subscribing to the model in Marketplace'
  # e.g. DEEPSEEK_R1_Llama_8B_MARKET_PLACE = "arn:aws:sagemaker:us-west-2:[YOUR_ACCOUNT_ID]:endpoint/endpoint-deepseek-llama-8b"
DEEPSEEK_R1_Llama_8B_JUMPSTART = 'Enter Sagemaker Endpoint ARN deployed through SageMaker jumpstart'
  # e.g. DEEPSEEK_R1_Llama_8B_JUMPSTART = "arn:aws:sagemaker:us-west-2:[YOUR_ACCOUNT_ID]:endpoint/jumpstart-deepseek-llm-r1-disti-20250209-125605"

client = boto3.client("bedrock-runtime", region_name="us-west-2")
default_prompt = "I have 10 apples now. I gave two of them to my friend. How many apples do I have now?"

def call_deepseek_r1(prompt=default_prompt): 
    body = json.dumps({
        "prompt": prompt
    })
    response = client.invoke_model(
        body=body, 
        modelId=DEEPSEEK_R1_Llama_8B_MARKET_PLACE 
        #modelId=DEEPSEEK_R1_Llama_8B_IMPORTED_MODEL
        #modelId=DEEPSEEK_R1_Llama_8B_MARKETPLACE
    )
    response_body = json.loads(response.get('body').read())
    return response_body
    
def lambda_handler(event, context):
    sentence = event['prompt']
    response = {
        "result": call_deepseek_r1(sentence)
    }
    
    return response
