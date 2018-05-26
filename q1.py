
def top_level_domain(val):
    return val.split('.')[-1]


url = ['www.annauniv.edu',
       'www.google.com',
       'www.ndtv.com',
       'www.website.org',
       'www.bis.org.in',
       'www.rbi.org.in',
       ]

url.sort(key=top_level_domain)

print(url)
