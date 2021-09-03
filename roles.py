from bs4 import BeautifulSoup
import requests

top = []
jgl = []
mid = []
adc = []
supp = []
allc = []

def set_roles():
    html_text = requests.get('https://na.op.gg/champion/statistics').text
    soup = BeautifulSoup(html_text, 'lxml')
    
    all_champs_items = soup.find_all('div', class_="champion-index__champion-item")
    
    for c in all_champs_items:
        cName = c.find('div', class_="champion-index__champion-item__name").text
        allc.append(cName)
        pos = c.find_all('div', 'champion-index__champion-item__position')
        for p in pos: 
            if p.text == "Top":
                top.append(cName)
            elif p.text == "Jungle":
                jgl.append(cName)
            elif p.text == "Middle":
                mid.append(cName)
            elif p.text == "Bottom":
                adc.append(cName)
            elif p.text == "Support":
                supp.append(cName)
            
            
if __name__ == "__main__":
    set_roles()
    assert(len(allc) == 156)
    print("Top:")
    print(top)
    print("\n\n")
    print("Jgl:")
    print(jgl)
    print("\n\n")
    print("Mid:")
    print(mid)
    print("\n\n")
    print("ADC:")
    print(adc)
    print("\n\n")
    print("Supp:")
    print(supp)