#flask application
from flask import Flask,url_for,render_template,request,redirect
import requests
import abc,aifc,argparse,array,ast,asynchat,asyncio,asyncore,atexit,audioop

aDict={
	'abc':abc.__doc__,
	'aifc':aifc.__doc__,
	'array':array.__doc__,
	'ast':ast.__doc__,
	'asynchat':asynchat.__doc__,
	'asyncio':asyncio.__doc__,
	'asyncore':asyncore.__doc__,
	'atexit':atexit.__doc__,
	'audioop':'Manipulate raw audio data'
}
import base64,bdb,binascii,binhex,bisect,builtins,bz2

bDict={
	'base64':base64.__doc__,
	'bdb':bdb.__doc__,
	'binascii':binascii.__doc__,
	'binhex':binhex.__doc__,
	'bisect':bisect.__doc__,
	'builtins':builtins.__doc__,
	'bz2':bz2.__doc__
}
import calendar,cgi,cgitb,chunk,cmath,cmd,code,codecs,codeop,collections,colorsys,compileall,concurrent,configparser,contextlib,contextvars,copy,copyreg,cProfile,csv,ctypes

cDict={
	'calendar':calendar.__doc__,
	'cgi':cgi.__doc__,
	'cgitb':__doc__,
	'chunk':__doc__,
	'cmath':cmath.__doc__,
	'cmd':cmd.__doc__,
	'code':code.__doc__,
	'codecs':codecs.__doc__,
	'codeop':codeop.__doc__,
	'collections':collections.__doc__,
	'colorsys':colorsys.__doc__,
	'compileall':compileall.__doc__,
	'concurrent':concurrent.__doc__,
	'configparser':configparser.__doc__,
	'contextlib':contextlib.__doc__,
	'contextvars':contextvars.__doc__,
	'copy':copy.__doc__,
	'copyreg':copyreg.__doc__,
	'cProfile':cProfile.__doc__,
	'csv':csv.__doc__,
	'ctypes':ctypes.__doc__
}
import dataclasses,datetime,dbm,decimal,difflib,dis,distutils,doctest
dDict={
	'dataclasses':dataclasses.__doc__,
	'datetime':datetime.__doc__,
	'dbm':dbm.__doc__,
	'decimal':decimal.__doc__,
	'difflib':difflib.__doc__,
	'dis':dis.__doc__,
	'distutils':distutils.__doc__,
	'doctest':doctest.__doc__
}

import email,encodings,ensurepip,enum,errno
eDict={
	'email':email.__doc__,
	'encodings':encodings.__doc__,
	'ensurepip':ensurepip.__doc__,
	'enum':enum.__doc__,
	'errno':errno.__doc__
}

import faulthandler,filecmp,fileinput,fnmatch,fractions,ftplib,functools
fDict={
	'faulthandler':faulthandler.__doc__,
	#'fcntl':fcntl.__doc__,
	'filecmp':filecmp.__doc__,
	'fnmatch':fnmatch.__doc__,
	'fractions':fractions.__doc__,
	'ftplib':ftplib.__doc__,
	'functools':functools.__doc__
}

import gc,getopt,getpass,gettext,glob,graphlib,gzip
gDict={
	'gc':gc.__doc__,
	'getopt':getopt.__doc__,
	'getpass':getpass.__doc__,
	'gettext':gettext.__doc__,
	'glob':glob.__doc__,
	'graphlib':graphlib.__doc__,
	'gzip':gzip.__doc__
}

import hashlib,heapq,hmac,html,http
hDict={
	'hashlib':hashlib.__doc__,
	'heapq':heapq.__doc__,
	'hmac':hmac.__doc__,
	'html':html.__doc__,
	'http':http.__doc__
}

import imaplib,imghdr,imp,importlib,inspect,io,ipaddress,itertools
iDict={
	'imaplib':imaplib.__doc__,
	'imghdr':imghdr.__doc__,
	'imp':imp.__doc__,
	'importlib':importlib.__doc__,
	'inspect':inspect.__doc__,
	'io':io.__doc__,
	'ipaddress':ipaddress.__doc__,
	'itertools':itertools.__doc__
}

import json
jDict={
	'json':json.__doc__
}

import keyword
kDict={
	'keyword':keyword.__doc__
}

import lib2to3,linecache,locale,logging,lzma
lDict={
	'lib2to3':lib2to3.__doc__,
	'linecache':linecache.__doc__,
	'locale':locale.__doc__,
	'logging':logging.__doc__,
	'lzma':lzma.__doc__
}

import mailbox,mailcap,marshal,math,mimetypes,mmap,modulefinder,msilib,msvcrt,multiprocessing
mDict={
	'mailbox':mailbox.__doc__,
	'mailcap':mailcap.__doc__,
	'marshal':marshal.__doc__,
	'math':math.__doc__,
	'mimetypes':mimetypes.__doc__,
	'mmap':mmap.__doc__,
	'modulefinder':modulefinder.__doc__,
	'msilib':msilib.__doc__,
	'msvcrt':msvcrt.__doc__,
	'multiprocessing':multiprocessing.__doc__
}

import netrc,nntplib,numbers
nDict={
	'netrc':netrc.__doc__,
	'nntplib':nntplib.__doc__,
	'numbers':numbers.__doc__
}

import operator,optparse,os
oDict={
	'operator':operator.__doc__,
	'optparse':optparse.__doc__,
	'os':os.__doc__
}

import pathlib,pdb,pickle,pickletools,pkgutil,platform,plistlib,poplib,pprint,profile,pstats,py_compile,pyclbr,pydoc
pDict={
	'pathlib':pathlib.__doc__,
	'pdb':pdb.__doc__,
	'pickle':pickle.__doc__,
	'pickletools':pickletools.__doc__,
	'pkgutil':pkgutil.__doc__,
	'platform':platform.__doc__,
	'plistlib':plistlib.__doc__,
	'poplib':poplib.__doc__,
	'pprint':pprint.__doc__,
	'profile':profile.__doc__,
	'pstats':pstats.__doc__,
	'py_compile':py_compile.__doc__,
	'pyclbr':pyclbr.__doc__,
	'pydoc':pydoc.__doc__
}

import queue,quopri
qDict={
	'queue':queue.__doc__,
	'quopri':quopri.__doc__
}

import random,re,reprlib,rlcompleter,runpy
rDict={
	'random':random.__doc__,
	're':re.__doc__,
	'reprlib':reprlib.__doc__,
	'rlcompleter':rlcompleter.__doc__,
	'runpy':runpy.__doc__
}

import sched,secrets,select,selectors,shelve,shlex,shutil,signal,site,smtpd,smtplib,sndhdr,socket,socketserver,sqlite3,ssl,stat,statistics,string,stringprep,struct,subprocess,sunau,symtable,sys,sysconfig
sDict={
	'sched':sched.__doc__,
	'secrets':secrets.__doc__,
	'select':select.__doc__,
	'selectors':selectors.__doc__,
	'shelve':shelve.__doc__,
	'shlex':shlex.__doc__,
	'shutil':shutil.__doc__,
	'signal':signal.__doc__,
	'site':site.__doc__,
	'smtpd':smtpd.__doc__,
	'smtplib':smtplib.__doc__,
	'sndhdr':sndhdr.__doc__,
	'socket':socket.__doc__,
	'socketserver':socketserver.__doc__,
	'sqlite3':sqlite3.__doc__,
	'ssl':ssl.__doc__,
	'stat':stat.__doc__,
	'statistics':statistics.__doc__,
	'string':string.__doc__,
	'stringprep':stringprep.__doc__,
	'struct':struct.__doc__,
	'subprocess':subprocess.__doc__,
	'sunau':sunau.__doc__,
	'symtable':symtable.__doc__,
	'sys':sys.__doc__,
	'sysconfig':sysconfig.__doc__
}

import tabnanny,tarfile,telnetlib,tempfile,test,textwrap,threading,time,timeit,tkinter,token,tokenize,trace,traceback,tracemalloc,turtle,turtledemo,types,typing
tDict={
	'tabnanny':tabnanny.__doc__,
	'tarfile':tarfile.__doc__,
	'telnetlib':telnetlib.__doc__,
	'tempfile':tempfile.__doc__,
	'test':test.__doc__,
	'textwrap':textwrap.__doc__,
	'threading':threading.__doc__,
	'time':time.__doc__,
	'timeit':timeit.__doc__,
	'tkinter':tkinter.__doc__,
	'token':token.__doc__,
	'tokenize':tokenize.__doc__,
	'trace':trace.__doc__,
	'traceback':traceback.__doc__,
	'tracemalloc':tracemalloc.__doc__,
	'turtle':turtle.__doc__,
	'turtledemo':turtledemo.__doc__,
	'types':types.__doc__,
	'typing':typing.__doc__
}

import unicodedata,unittest,urllib,uu,uuid
uDict={
	'unicodedata':unicodedata.__doc__,
	'unittest':unittest.__doc__,
	'urllib':urllib.__doc__,
	'uu':uu.__doc__,
	'uuid':uuid.__doc__
}

import venv
vDict={
	'venv':venv.__doc__
}

import warnings,wave,weakref,webbrowser,winreg,winsound,wsgiref
wDict={

	'warnings':warnings.__doc__,
	'wave':wave.__doc__,
	'weakref':weakref.__doc__,
	'webbrowser':webbrowser.__doc__,
	'winreg':winreg.__doc__,
	'winsound':winsound.__doc__,
	'wsgiref':wsgiref.__doc__
}

import xdrlib,xml,xmlrpc
xDict={
	'xdrlib':xdrlib.__doc__,
	'xml':xml.__doc__,
	'xmlrpc':xmlrpc.__doc__
}

import zipapp,zipfile,zipimport,zlib,zoneinfo
zDict={
	'zipapp':zipapp.__doc__,
	'zipfile':zipfile.__doc__,
	'zipimport':zipimport.__doc__,
	'zlib':zlib.__doc__,
	'zoneinfo':zoneinfo.__doc__
}
app = Flask(__name__)

@app.route('/')
def welcome():
   return render_template('home.html')

@app.route('/home')
def home():
   return render_template('home.html')

@app.route('/search',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      letter = request.form['search']
      firstChar=letter[0]
      print(letter)
      print(firstChar)
      if firstChar=='a':
      	return redirect(url_for('a',dictRes=aDict))
      if firstChar=='b':
      	return redirect(url_for('b',dictRes=bDict))
      if firstChar=='c':
      	return redirect(url_for('c',dictRes=cDict))
      if firstChar=='d':
      	return redirect(url_for('d',dictRes=dDict))
      if firstChar=='e':
      	return redirect(url_for('e',dictRes=eDict))
      if firstChar=='f':
      	return redirect(url_for('f',dictRes=fDict))
      if firstChar=='g':
      	return redirect(url_for('g',dictRes=gDict))
      if firstChar=='h':
      	return redirect(url_for('h',dictRes=hDict))
      if firstChar=='i':
      	return redirect(url_for('i',dictRes=iDict))
      if firstChar=='j':
      	return redirect(url_for('j',dictRes=jDict))
      if firstChar=='k':
      	return redirect(url_for('k',dictRes=kDict))
      if firstChar=='l':
      	return redirect(url_for('l',dictRes=lDict))
      if firstChar=='m':
      	return redirect(url_for('m',dictRes=mDict))
      if firstChar=='n':
      	return redirect(url_for('n',dictRes=nDict))
      if firstChar=='o':
      	return redirect(url_for('o',dictRes=oDict))
      if firstChar=='p':
      	return redirect(url_for('p',dictRes=pDict))
      if firstChar=='q':
      	return redirect(url_for('q',dictRes=qDict))
      if firstChar=='r':
      	return redirect(url_for('r',dictRes=rDict))
      if firstChar=='s':
      	return redirect(url_for('s',dictRes=sDict))
      if firstChar=='t':
      	return redirect(url_for('t',dictRes=tDict))
      if firstChar=='u':
      	return redirect(url_for('u',dictRes=uDict))
      if firstChar=='v':
      	return redirect(url_for('v',dictRes=vDict))
      if firstChar=='w':
      	return redirect(url_for('w',dictRes=wDict))
      if firstChar=='x':
      	return redirect(url_for('x',dictRes=xDict))
      if firstChar=='z':
      	return redirect(url_for('z',dictRes=zDict))


#Jinja2 (the template rendering component of Flask) allows you to use the url_for function to dynamically create a url, for a given view function.
#re-directing to the paths
@app.route('/a', methods = ['GET', 'POST'])
def a():
    return render_template("/a.html",dictRes=aDict)

@app.route('/b', methods = ['GET', 'POST'])
def b():
    return (render_template('b.html',dictRes=bDict))

@app.route('/c', methods = ['GET', 'POST'])
def c():
    return (render_template('c.html',dictRes=cDict))
   
@app.route('/d', methods = ['GET', 'POST'])
def d():
    return (render_template('d.html',dictRes=dDict))

@app.route('/e', methods = ['GET', 'POST'])
def e():
    return (render_template('e.html',dictRes=eDict))

@app.route('/f', methods = ['GET', 'POST'])
def f():
    return (render_template('f.html',dictRes=fDict))

@app.route('/g', methods = ['GET', 'POST'])
def g():
    return (render_template('g.html',dictRes=gDict))

@app.route('/h', methods = ['GET', 'POST'])
def h():
    return (render_template('h.html',dictRes=hDict))

@app.route('/i', methods = ['GET', 'POST'])
def i():
    return (render_template('i.html',dictRes=iDict))

@app.route('/j', methods = ['GET', 'POST'])
def j():
    return (render_template('j.html',dictRes=jDict))

@app.route('/k', methods = ['GET', 'POST'])
def k():
    return (render_template('k.html',dictRes=kDict))

@app.route('/l', methods = ['GET', 'POST'])
def l():
    return (render_template('l.html',dictRes=lDict))

@app.route('/m', methods = ['GET', 'POST'])
def m():
    return (render_template('m.html',dictRes=mDict))

@app.route('/n', methods = ['GET', 'POST'])
def n():
    return (render_template('n.html',dictRes=nDict))

@app.route('/o', methods = ['GET', 'POST'])
def o():
    return (render_template('o.html',dictRes=oDict))
   
@app.route('/p', methods = ['GET', 'POST'])
def p():
    return (render_template('p.html',dictRes=pDict))

@app.route('/q', methods = ['GET', 'POST'])
def q():
    return (render_template('q.html',dictRes=qDict))

@app.route('/r', methods = ['GET', 'POST'])
def r():
    return (render_template('r.html',dictRes=rDict))

@app.route('/s', methods = ['GET', 'POST'])
def s():
    return (render_template('s.html.html',dictRes=sDict))

@app.route('/t', methods = ['GET', 'POST'])
def t():
    return (render_template('t.html',dictRes=tDict))

@app.route('/u', methods = ['GET', 'POST'])
def u():
    return (render_template('u.html',dictRes=uDict))

@app.route('/v', methods = ['GET', 'POST'])
def v():
    return (render_template('v.html',dictRes=vDict))

@app.route('/w', methods = ['GET', 'POST'])
def w():
    return (render_template('w.html',dictRes=wDict))

@app.route('/x', methods = ['GET', 'POST'])
def x():
    return (render_template('x.html',dictRes=xDict))

@app.route('/z', methods = ['GET', 'POST'])
def z():
    return (render_template('z.html',dictRes=zDict))
if __name__ == '__main__':
   app.run(debug=True)
