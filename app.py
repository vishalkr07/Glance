from multiprocessing import Process
from  flask import Flask, render_template, request
import os
from spyder import scrap
import subprocess
import re

app = Flask(__name__)
number = 10

@app.route('/')
def main():
    #os.system("(python spyder.py&) && echo /'bitch/'")
    #subprocess.call(['python spyder.py', ''], shell = True)
    #url = "https://www.studentnewsdaily.com/archive/daily-news-article/"
    #scrap(url)
    #subprocess.call('echo "Done"', shell = True)
    headline=[]
    head_list = os.listdir(os.path.join(os.getcwd(),"parse/heads"))
    for i in head_list:
        with open(os.path.join(os.getcwd(),"parse/heads/"+i), "r")as f:
            headline.append(f.read())
    return render_template("index.html",headline=headline)

def readFile(No):
    a = ""
    with open(os.path.join(os.getcwd(),"pretrained/decode/decoded/"+str(No)), "r") as f:
        a = f.read()
    return a

def debug(inp):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print(inp)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

def processRead(query,x):
    a = query[x+5:]
    debug(a)
    return 1
    # if(re.findall("one",a)): return 1
    # elif(re.findall("two|to",a)): return 2
    # elif(re.findall("three|tree|hree|3",a)): return 3
    # elif(re.findall("four|for|4|phor",a)): return 4
    # elif(re.findall("five|fiv|5|fife|fif",a)): return 5
    # else: pass
    return a

@app.route('/Summarize')
def summarize():
    query = request.args.get('command')
    b1 = query.rfind('read');
    b2 = query.rfind('accelerate');
    b3 = query.rfind('skip');
    b4 = query.rfind('stop');
    b5 = query.rfind('summarize');
    b6 = query.rfind('heading');
    debug(b1)
    if b1!=-1:
        no = processRead(query,b1)
        debug(no)
        if(no=="all"):
            response=""
            for i in number:
                response += readFile(i)
        response = readFile(no-1)
        debug(response)
        head=""
        with open(os.path.join(os.getcwd(),"parse/heads/"+str(no)+".head"), "r") as f:
            head=f.read()
        return {"res":response,"head":head}
    elif b2!=-1:
        pass
    elif b3!=-1:
        pass
    elif b4!=-1:
        pass
    elif b5!=-1:
        pass
    elif b6!=-1:
        pass
    else:
        return "Not Recognized"
    # give url to the scrapper
    cwd = os.getcwd()
    os.system(os.path.join(cwd, "exec.sh"))
    return query

def summary():
    #scrap(number)
    #os.system('./exec.sh')
    pass

if __name__=="__main__":
    p1 = Process(target=app.run)
    #p2 = Process(target=scrap)
    p3 = Process(target=summary)
    p1.start()
    #p2.start()
    p3.start()
    p1.join()
    p3.join()
    #app.run()