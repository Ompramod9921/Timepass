import streamlit as st
import json
from streamlit_lottie import st_lottie
from streamlit_observable import observable
import joke_generator
from dadjokes import Dadjoke
import random
import requests
import randfacts 
from json import loads
from animals import Animals

st.set_page_config(page_title='Timepass',page_icon='👽')
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            footer:after {
	content:'Made with ❤️ by om pramod'; 
	visibility: visible ;
}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
st.sidebar.success("TIMEPASS Menu 👇🏼")
box = st.sidebar.selectbox('',("Home","Advices","Jokes","Facts","Quotes","Animal Gallery","World Tour","Love Calculator","APOD","Don't touch me"))
st.sidebar.write("")
st.sidebar.image("app.jpeg",width=310)

def home() :
    st.markdown("<h1 style='text-align: center; color:black ;font-family: fantasy'>T I M E P A S S</h1>", unsafe_allow_html=True)
    st.markdown("****")

    st.error(" ⚠️ Disclaimer : This application is made solely for entertainment purposes")

    def load_lottiefile(filepath: str):
        with open(filepath, "r") as f :
            return json.load(f)

    lottie_coding = load_lottiefile("main.json")

    st_lottie(
        lottie_coding,
        speed= 1.5,
        reverse=False,
        loop=True,
        height=400,
        width= 700,
        key=None
    )

    st.header(":mailbox: Get In Touch With Me!")

    contact_form = """
    <form action="https://formsubmit.co/ompramod9921@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here"></textarea>
        <button type="submit">Send</button>
    </form>
    """

    st.markdown(contact_form, unsafe_allow_html=True)

    # Use Local CSS File
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    local_css("style/style.css")

    st.markdown("connect with me on [linkedin] (https://www.linkedin.com/in/omkar-h-7944a4202)")

def advices():
    st.title("😺 Bored ?")
    st.markdown("****")
    st.markdown("Boredom can feel impossible to escape. Well, dont't worry ; boredom is a state of mind, and we want to break you out of it . This bot helps you find things to do when you're bored !")

    def load_lottiefile(filepath: str):
        with open(filepath, "r") as f :
            return json.load(f)

    lottie_coding = load_lottiefile("advice.json")

    st_lottie(
        lottie_coding,
        speed= 1.5,
        reverse=False,
        loop=True,
        height=300,
        width= 700,
        key=None
    )

    st.subheader("Let's find you something to do..... ")

    if st.button("Get ideas") :
        s = requests.get('https://www.boredapi.com/api/activity')
        p = s.json()
        st.success(p['activity'])

def jokes():
    dadjoke = Dadjoke()
    x = dadjoke.joke

    y =joke_generator.generate()

    list = [x,y]

    def load_lottiefile(filepath: str):
        with open(filepath, "rb") as f :
            return json.load(f)

    lottie_coding = load_lottiefile("joke.json")

    st_lottie(
        lottie_coding,
        speed= 1.5,
        reverse=False,
        loop=True,
        height=200,
        width= 700,
        key=None
    )

    st.markdown("<h1 style='text-align: center; color:black ;font-family: fantasy'>Funny Jokes</h1>", unsafe_allow_html=True)
    st.markdown("****")
    st.subheader('''"A laugh a day keeps the doctor away ! " - Saying''')
    st.markdown("Looking for funny jokes ? Settle in: You're in the right place. From clean knock-knock jokes and the top corny jokes to hilarious one-liners and clever riddles, we've got the jokes guaranteed to bring on serious laughs.")
    if st.button('get jokes'):
        st.success(random.choice(list))

def facts():
    m = randfacts.get_fact()

    url = "https://uselessfacts.jsph.pl/random.json?language=en"
    response = requests.request("GET", url)  
    data = json.loads(response.text)
    n = data['text']

    list = [m,n]

    def load_lottiefile(filepath: str):
        with open(filepath, "r") as f :
            return json.load(f)

    lottie_coding = load_lottiefile("fact.json")

    st_lottie(
        lottie_coding,
        speed= 1.5,
        reverse=False,
        loop=True,
        height=300,
        width= 700,
        key=None
    )

    st.markdown("<h1 style='text-align: center; color:blue ;font-family: fantasy'>Random Facts</h1>", unsafe_allow_html=True)
    st.markdown("****")

    st.markdown('''These fun facts about everything from the cosmos to the inner workings of your body will blow your mind.These fun facts will actually surprise and entertain You & You'll Say, "OMG!"''')

    if st.button("get facts") :
        st.success(random.choice(list))

def quotes():
    def second():
        r = requests.get('https://api.quotable.io/random')
        quote = r.json()
        st.success(quote['content']+" ----"+quote['author'])

    def first():
        response = requests.get('http://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en')
        st.success('{quoteText} ---- {quoteAuthor}'.format(**loads(response.text)))

    def load_lottiefile(filepath: str):
        with open(filepath, "rb") as f :
            return json.load(f)

    lottie_coding = load_lottiefile("quotes.json")

    st_lottie(
        lottie_coding,
        speed= 1,
        reverse=False,
        loop=True,
        height=350,
        width= 700,
        key=None
    )
    st.markdown("<h1 style='text-align: center; color:black ;font-family: fantasy'>Cool Quotes & Sayings </h1>", unsafe_allow_html=True)
    st.markdown("A collection of cool quotes to inspire and encourage you, plus ones that will make you smile ! Find wisdom in these awesome quotes to encourage you to always stay calm, cool, and collective !")
    if st.button("Get quotes"):
        try:
            first()
        except :
            second()

def gallery():
    list = ['cat', 'dog', 'koala', 'fox', 'birb', 'red_panda', 'panda', 'racoon', 'kangaroo']
    animal = Animals(random.choice(list))
    a = animal.image()

    c = requests.get('https://some-random-api.ml/animal/birb')
    d = c.json()
    b = d['image']

    list = [a,b]

    st.title('🐇 Do you love animals ?')
    st.markdown("***")
    st.subheader('''"Until one has loved an animal, a part of one's soul remains unawakened." - Anatole France''')
    st.markdown("Animals are creatures that bring so many people happiness every single day. They are loving, compassionate and a friend to all people. Animals make humans more compassionate, positive individuals who are happier in general. Animals help in allowing people to be more loving because of the compassion animals give to them.")
    st.subheader('''Here Are Some Pictures Of Birds & Animals That Will Make You Say “Awww”''')
    if st.button("show images") :
        st.image(random.choice(list),width=700)

def tour():
    observers = observable("World Tour!", 
            notebook="@d3/world-tour",
            targets=["canvas"], 
            observe=["name"]
        )
        
    name = observers.get("name")
        
    st.write(f"Current country: ** *{name}* **") 

def love():
    url = "https://love-calculator.p.rapidapi.com/getPercentage"

    def load_lottiefile(filepath: str):
        with open(filepath, "rb") as f :
            return json.load(f)

    lottie_coding = load_lottiefile("love.json")

    st_lottie(
        lottie_coding,
        speed= 1.5,
        reverse=False,
        loop=True,
        height=400,
        width= 700,
        key=None
    )

    st.markdown("<h1 style='text-align: center; color:red ;font-family: fantasy'>Love Calculator</h1>", unsafe_allow_html=True)
    st.markdown('''Sometimes you'd like to know if a relationship with someone could work out. Therefore Doctor Love himself designed this great machine for you. Love Calculator is a really super-duper funny approach to find the connection with your partner. All people's names have really some decent meaning the ultimate Love Calculator helps you to find compatibility of your love with your partner.Let's find out what the chances for you and your dream partner are...''')
    st.markdown("****")
    you = st.text_input("enter your name :")
    crush = st.text_input("enter your crush's name :")

    querystring = {"fname":you,"sname":crush}

    headers = {
        'x-rapidapi-host': "love-calculator.p.rapidapi.com",
        'x-rapidapi-key': "e4998fab02mshd659411da63b59ap18d367jsn43b1841d6872"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    result = json.loads(response.text)

    def final():
        if int(result["percentage"] ) < 50 :
            st.error('percentage of connection :  ' + result["percentage"])
            st.error('advice :  ' + result["result"])
        else:
            st.success('percentage of connection :  ' + result["percentage"])
            st.success('advice :  ' + result["result"])

    if st.button("Calculate Love") :
        st.markdown("****")
        final()

def APOD():
    link = "https://api.nasa.gov/planetary/apod?api_key=941DEaQNb5YdKODUY7yIHiCvv42OppKFClQpypMm"
    response = requests.request("GET", link)
    final = response.json()
    st.markdown("<h1 style='text-align: center; color:black ;font-family: aerial'>Astronomy Picture Of the Day (APOD)</h1>", unsafe_allow_html=True)
    st.markdown("****")
    st.header(final['title'])
    st.write(final['explanation'])
    st.image(final['url'])
    st.caption('copyright  : '+ final['copyright'])
    st.caption('date  :  '+ final['date'])

if box == "Home" :
    home()
elif box == "Advices":
    advices()
elif box == "Jokes":
    jokes()
elif box == "Facts":
    facts()
elif box == 'Quotes':
    quotes()
elif box == 'Animal Gallery':
    gallery()
elif box == 'World Tour':
    tour()
elif box == 'Love Calculator':
    love()
elif box == 'APOD':
    APOD()
elif box == "Don't touch me":
    st.video("ghost.mp4")


