import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from openai import OpenAI
from dotenv import load_dotenv

# =====================
# LOAD ENV
# =====================
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")

if not API_KEY:
    raise Exception("OPENAI_API_KEY not found in .env")

client = OpenAI(api_key=API_KEY)


# APP

app = FastAPI()


# MEMORY 

conversation = [
    {"role": "system", "content": "You are Bay_max, a helping assistant."}
]


# FRONTEND (HTML)

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
<title></title>
<style>
body { margin:0; font-family:Arial; background:#343541; color:white; display:flex; flex-direction:column; height:100vh; }
header { background:#202123; padding:15px; text-align:center; }
#chat { flex:1; padding:15px; overflow-y:auto; }
.msg { max-width:70%; padding:12px; margin:8px 0; border-radius:8px; }
.user { background:#0b93f6; margin-left:auto; }
.ai { background:#444654; }
#input { display:flex; padding:10px; background:#202123; }
input { flex:1; padding:12px; font-size:16px; border:none; border-radius:6px; }
button { margin-left:10px; padding:12px 20px; background:#0b93f6; border:none; border-radius:6px; color:white; cursor:pointer; }
</style>
</head>
<body>

<header>Bay_max</header>

<div id="chat"></div>

<div id="input">
    <input id="text" placeholder="Send a message..." />
    <button onclick="send()">Send</button>
</div>

<script>
const chat = document.getElementById("chat");
const input = document.getElementById("text");

input.addEventListener("keypress", e => {
    if (e.key === "Enter") send();
});

function addMsg(text, cls){
    const div = document.createElement("div");
    div.className = "msg " + cls;
    div.innerText = text;
    chat.appendChild(div);
    chat.scrollTop = chat.scrollHeight;
}

async function send(){
    const text = input.value.trim();
    if(!text) return;
    addMsg(text, "user");
    input.value = "";

    addMsg("Giving you a best answer for your Question Sir.....", "ai");

    const res = await fetch("/chat", {
        method: "POST",
        headers: {"Content-Type":"application/json"},
        body: JSON.stringify({message:text})
    });

    chat.lastChild.remove();
    const data = await res.json();
    addMsg(data.reply, "ai");
}
</script>

</body>
</html>
"""

# ROUTES

@app.get("/", response_class=HTMLResponse)
def home():
    return HTML_PAGE


@app.post("/chat")
async def chat(req: Request):
    data = await req.json()
    user_message = data.get("message")

    conversation.append({"role": "user", "content": user_message})

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=conversation,
        temperature=0.7
    )

    reply = response.choices[0].message.content
    conversation.append({"role": "assistant", "content": reply})

    return JSONResponse({"reply": reply})
