import json
from langchain.llms import OpenAI
from langchain.agents import initialize_agent
from langchain.agents.agent_toolkits import ZapierToolkit
from langchain.utilities.zapier import ZapierNLAWrapper

def handler(event, context):
    print('received event:')
    print(event)

    if 'body' in event:
        try:
            parsed_body = json.loads(event['body'])
            email = parsed_body.get('email', '') 
            productPanelContent = parsed_body.get('productPanelContent', '')
        except json.JSONDecodeError:
                print('Error parsing JSON body')

    llm = OpenAI(temperature=.3)
    zapier = ZapierNLAWrapper()
    toolkit = ZapierToolkit.from_zapier_nla_wrapper(zapier)
    agent = initialize_agent(toolkit.get_tools(), llm, agent="zero-shot-react-description", verbose=True)
    agent.run(
        f"write email to {email} you should mention the brief "
        f"information about the product {productPanelContent} "
        f"and highlight its advantages"
    )

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': json.dumps('Hello from your new Amplify Python lambda!')
    }