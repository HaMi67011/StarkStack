import requests

class SupportChatbot:
    def __init__(self,api_key,model="llama-3.1-8b-instant",max_memory=30):
        self.api_key = api_key
        self.model = model
        self.convo_memory = []
        self.max_memory = max_memory
    
    def send_message(self, message):
        self.convo_memory.append({"role": "user", "content": message})
        self.convo_memory = self.convo_memory[-self.max_memory:]
        system_prompt = (
            "You are a helpful technical support chatbot."
            "You remember previous conversation context, but do not invent facts."
            "Use memory only when helpful."
        )
        

        messages = [{'role':'system','content':system_prompt}] + self.convo_memory

        reply = self._call_api(messages)

        self.convo_memory.append({'role':'assistant','content':reply})

        return reply

    def _call_api(self, messages):
        
        url = "https://api.groq.com/openai/v1/chat/completions"

        header = {
            "Authorization":f"Bearer {self.api_key}",
            "Content-Type":'application/json'
        }
        data = {
            "model":self.model,
            "messages":messages,
            "temperature":0.3,
        }
        
        try:
            response = requests.post(url,json=data,headers=header)
            response.raise_for_status()
            return response.json()["choices"][0]['message']['content']
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 401:
                raise ValueError("Unauthorized: Check your API key")
            else:
                raise e
        except Exception as e:
            raise e