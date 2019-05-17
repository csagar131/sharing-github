#!pip3 install google
import  sys,time
import  webbrowser
try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found")

i="wikipedia"	#  write  code   here to google search 
print(i)
lst=[]
#time.sleep(5)
webbrowser.open_new_tab("https://www.google.com/search?q="+i)
n=(int)(input("how much to websites to print???"))
for j in search(i, tld="co.in", num=n, stop=1, pause=4): 
    print(j)
#lst.append(search(i,tld=".com",num=n,stop=1,pause=3))
#for k in range(0,len(lst)):
#    print((lst[k]))
#
