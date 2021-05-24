from django.shortcuts import render
from Json.models import person, pregunta, RespuestaUsu
from django.http import JsonResponse
from django.contrib.auth import authenticate

# Create your views here.
def preguntaJson(request):
    msn={'msn':'Error al conectar con json'}

    if(request.method == 'GET'):        
        usuId = request.GET.get('id')

        #aqui verifico si ya ha respondido preguntas antes, si no creo el id de la pregunta y lo inicializo en 1
        try:
            usu = person.objects.get(User_id=usuId)

        except:
            persona = person(pregunta = 1,
                User_id=usuId, score = 0)
            persona.save()
        try:    
            #aqui verifico en que id de la pregunta está el usuario 
            usu = person.objects.get(User_id=usuId)
            #aqui llamo la pregunta que corresponde al id 
            pre = pregunta.objects.get(id=usu.pregunta)

            if(pre is not None):
                msn={
                    'id':pre.id,
                    'pregunta': pre.pregunta,
                    'RespuestaA': pre.resA,
                    'RespuestaB': pre.resB,
                    'RespuestaC': pre.resC,
                    'RespuestaD': pre.resD
                }
                #return redirect('index')
            else:
                msn={'msn':'No hay mas preguntas'}
        except:
             msn={'pregunta': 'Ya no hay preguntas para mostrar'}
    return JsonResponse(msn)

def sigPreJson(request):
    msn={'msn':''}
    if(request.method == 'GET'):   
        #aqui llamo a la tabla person donde user = usuId y guardo la respuesta del usuario
        usuId = request.GET.get('id')
        resp  = request.GET.get('res')
        usu = person.objects.get(User_id=usuId)
        respuest = RespuestaUsu(respuesta= resp, User_id=usuId, Pregunta_id=usu.pregunta,)
        respuest.save()
        #aqui aumento el numero de la pregunta en 1 para que proceda con la siguiente pregunta
    
        persona = person(id=usu.id,
            pregunta = int(usu.pregunta+1),User_id=usuId, score = 0)
        persona.save()
        msn={'msn':'Todo correcto y guardado'}
    else:
        msn={'msn':'No hay mas preguntas'}
    return JsonResponse(msn)    

def newRecord(request):
    msn={'msn':''}
    if(request.method == 'GET'):   
        #aqui llamo a la tabla person donde user = usuId y guardo la respuesta del usuario
        usuId = request.GET.get('id')
        score  = request.GET.get('score')
        preg  = request.GET.get('preg')
        usu = person.objects.get(User_id=usuId)
        #aqui aumento el numero de la pregunta en 1 para que proceda con la siguiente pregunta
    
        persona = person(id=usu.id,User_id=usuId, pregunta=preg, score = score)
        persona.save()
        msn={'msn':'Todo correcto y guardado'}
    else:
        msn={'msn':'No hay mas preguntas'}
    return JsonResponse(msn) 

    
    
def datosJson(request):

    msn={
        "usuario":"",
        "pass":""
    }
    if(request.method == 'GET' ):
        username = request.GET.get('usr')
        password = request.GET.get('pass')
        user = authenticate(request, username=username, password=password)
        #aqui creo el id de la pregunta del usuario y su score
        if(user is not None):
            try:
                usur = person.objects.get(User_id=user.id)
            except:
                persona = person(pregunta = 1,User_id=user.id, score = 0)
                persona.save()
                usur = person.objects.get(User_id=user.id)
            msn = {
                'id':user.id,
                'usuario':user.username,
                'Nombre':user.first_name,
                'Apellido':user.last_name,
                'Correo':user.email,
                'score':usur.score,
                'pregunta':usur.pregunta,
                "msn":"Bienvenido",
            }
        else:
            msn={
                "msn":"Usuario o contraseña no encontrados",
                "usuario": username,
                "contra":password
            }
    
    return JsonResponse(msn)
 