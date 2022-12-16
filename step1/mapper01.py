#!/usr/bin/env python3 
import os 
import sys 
import string 
import urllib.parse

sys.stdin.reconfigure(encoding='utf-8')

def mapper():
    sys.stderr.write('DEBUG_INFO: inside mapper \n')
    try:
        filepath = os.environ["map_input_file"] 
        filename = os.path.split(filepath)[-1]
    except KeyError:
        sys.stderr.write('filepath error\n')
        # in testing...
        filename = 'smallpagecounts-20160601-000000'
    
    meta_data = filename.split('-')

    for file in sys.stdin: #
        line = file.strip() 
        v = line.split(" ")

        # first field: project
        if (v[0] != "en"): continue 
        
        # second field: pagename
        v[1] = urllib.parse.unquote(v[1])
        # print("unquote " + v[1])
        
        # 3. Skip drop_start
        drop = False
        drop_start = ["Media", "Special", "Talk", "User", "User_talk", "Project", 
            "Project_talk", "File", "File_talk", "MediaWiki", "MediaWiki_talk", 
            "Template", "Template_talk", "Help", "Help_talk", "Category", "Category_talk",
            "Portal", "Wikipedia", "Wikipedia_talk"]
        for d in drop_start:
            if v[1].startswith(d):
                drop = True
                break
        if drop: continue
        # print("drop_start " + v[1])

        drop = False
        drop_end = ["jpg", "gif", ".png", ".JPG", ".GIF", ".PNG", ".ico", ".txt"]
        for d in drop_end:
            if v[1].endswith(d):
                drop = True
                break
        if drop: continue
        # print("drop_end " + v[1])

        # 4. Filter out en articles starts with lowercase
        if (len(v[1]) <= 0 or (v[1][0].isascii() and v[1][0].islower())): continue
        # print("isascii islower " + v[1])

        # 6. Exclude boilerplate pages
        drop = False
        drop_bilerplate = ["404_error", "Main_Page", "Hypertext_Transfer_Protocol", "Favicon.ico", "Search"]
        for d in drop_bilerplate:
            if v[1] == d:
                drop = True
                break
        if drop: continue
        # print("drop_bilerplate " + v[1])
        
        # access date
        sys.stdout.write('%s}%s\t%s\n' % (v[1], meta_data[1], v[2]))

        sys.stderr.write('%s}%s\t%s\n' % (v[1], meta_data[1], v[2]))
        # print(v[1] + '}' + meta_data[1] + ' ' + v[3])

    sys.stderr.write('exit mapper \n')

if __name__=='__main__':
    sys.stderr.write('inside main \n')
    mapper()