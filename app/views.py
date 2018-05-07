"""
Definition of views.
"""
from django.shortcuts import render
from django.http import HttpRequest
de django.template import RequestContext
de app.models import Curso
de datetime import datetime

def  home ( request ):
    "" " Renderiza a home page. " ""
    assert  isinstance (request, HttpRequest)
    retornar renderizar (
        pedido,
        ' app / index.html ' ,
        context_instance  = RequestContext (solicitação,
        {
            ' título ' : ' Página inicial ' ,
            ' ano ' : datetime.now (). ano,
        })
    )

 contacto de def ( pedido ):
    "" " Renderiza a página de contato. " ""
    assert  isinstance (request, HttpRequest)
    retornar renderizar (
        pedido,
        ' app / contact.html ' ,
        context_instance  = RequestContext (solicitação,
        {
            ' título ' : ' Contato ' ,
            ' mensagem ' : ' Entre em contato conosco ' ,
            ' ano ' : datetime.now (). ano,
        })
    )

def  sobre ( pedido ):
    "" " Renderiza a página sobre. " ""
    assert  isinstance (request, HttpRequest)
    retornar renderizar (
        pedido,
        ' app / about.html ' ,
        context_instance  = RequestContext (solicitação,
        {
            ' title ' : ' About ' ,
            ' mensagem ' : ' Gerenciador de vestibulares ' ,
            ' ano ' : datetime.now (). ano,
        })
    )

def  cadastro_cursos ( request ):
    assert  isinstance (request, HttpRequest)
    retornar renderizar (
        pedido,
        ' app / cadastro_cursos.html ' ,
        context_instance  = RequestContext (solicitação,
        {
            « título » : « Cadastro de cursos » ,
#             'cursos': ['ADS', 'SI', 'CC'],
            ' cursos ' : Curso.objects.all (),
            ' ano ' : datetime.now (). ano,
        })
    )
