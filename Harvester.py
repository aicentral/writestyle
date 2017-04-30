import urllib2
f=open('allarticles.txt','w')
searchstr='<h1 class="entry-title"><a href="'
l=len(searchstr)
urls=[]
for y in range(5):
    for m in range(12):
        if m<9:
            urls.append('https://blogs.lt.vt.edu/engineeredu/index.php/20%d/0%d/'%(12+y,m+1))
        else:
            urls.append('https://blogs.lt.vt.edu/engineeredu/index.php/20%d/%d/'%(12+y,m+1))
urls.append('https://blogs.lt.vt.edu/engineeredu/index.php/20%d/0%d/'%(17,1))
for url in urls:
    try:
        response = urllib2.urlopen(url)
        html = response.read()
        s=html
        idx=s.find(searchstr)
        while idx>0:
            s=s[(idx+l):]
            print>>f, s[0:s.find('"')]
            idx=s.find(searchstr)
    except:
        pass
f.close()


searchstr='<div class="entry-content">'
l=len(searchstr)
furls=open('allarticles.txt','r')
f=open('alltext.txt','w')
for url in furls:
    try:
        response = urllib2.urlopen(url)
        html = response.read()
        s=html
        idx=s.find(searchstr)
        while idx>0:
            s=s[(idx+l):]
            print>>f, s[0:s.find('<div class="sharedaddy sd-sharing-enabled">')]
            idx=s.find(searchstr)
    except:
        pass
f.close()
furls.close()
    