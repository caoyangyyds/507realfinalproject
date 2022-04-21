######
##Name: Caoyang##
##uniq_name: caoyangs##


from tree import BSTNode
import json
import plotly.graph_objects as go
from flask import Flask, render_template

cache_file = open("song_dict.json", 'r')
cache_file_contents = cache_file.read()
cache = json.loads(cache_file_contents)
cache_file.close()
tree_singer = BSTNode()
for i in range(len(cache)):
    tree_singer.insert(cache[i], i+1)
    #print(tree_singer.find(2))
print("Hello, can I help you?")
print("Here are 100 singers in billboard 2021, please give a rank of a singer you want to see.")
ans = input("Do you want to input a range?")
if ans == 'no':
    num = input()
    nm_split = num.split(' ')
    num_list = []
#print(nm_split)
    intnum = int(nm_split[0])
    num_list.append(intnum)
    #print(intnum)
    ll_singer = [tree_singer.find(intnum)]
    #print(tree_singer.find(1))
    list_singer = [ll_singer[0]['name']]
    #print(list_singer)    
else:
    num = input("please follow the format: 20 30" + "\n")
    nm_split = num.split(' ')
    num_list = []
    ll_singer = []
    list_singer = []
            
    for e in range(int(nm_split[0]), int(nm_split[1])+1):
        ll_singer.append(tree_singer.find(e))
        list_singer.append(tree_singer.find(e)['name'])
        num_list.append(e)
for inum in range(len(list_singer)):
    print(f'{num_list[inum]}. {list_singer[inum]}')
    
        


        
print("Please see the result in the host page!")

aws = input('Please input the number of the singer to get his/her/their details'+'\n')
aws_int = int(aws)
if int(aws) not in num_list:
    print("You are out of list.")
else:
    convenient_file = tree_singer.find(aws_int)
    singername = convenient_file['name']
    keyname = list(convenient_file['songs'][0].keys())
            #print(keyname)
    valuefirst = convenient_file['songs'][0].values()
            #print(valuefirst)
    dance_list = []
    energy_list = []
    tempo_list = []
    for val in valuefirst:
        dance_list.append(val["danceability"])
        energy_list.append(val["energy"])
        tempo_list.append(val["tempo"])

#ans_final = input("Do you want to see the data visualization in the website"+'\n')
#if ans_final == 'no':
#    print("ok! Bye!")
#else:
app = Flask(__name__)
@app.route('/')
def plot():
        fig1 = go.Figure()
        data = go.Table(header=dict(values=['Rank', 'Singer']),
                 cells=dict(values=[num_list, list_singer]))
        fig1.add_trace(data)
        fig2 = go.Figure([go.Bar(x=keyname, y=dance_list)])
        fig3 = go.Figure([go.Pie(labels=keyname, values=energy_list)])
        fig4 = go.Figure(data=[go.Scatter(
        x=keyname, y=dance_list,
        mode='markers',
        marker_size=tempo_list)])
        div1 = fig1.to_html(full_html=False)
        div2 = fig2.to_html(full_html=False)
        div3 = fig3.to_html(full_html=False)
        div4 = fig4.to_html(full_html=False)
        return render_template("plot.html", singernn=singername, plot_div1=div1, plot_div2=div2, plot_div3=div3, plot_div4=div4)

if __name__ == '__main__':
    ans_final = input("Do you want to see the data visualization in the website"+'\n')
    if ans_final == 'no':
        print(convenient_file)
        print("Bye!")
    else:
        app.run()
