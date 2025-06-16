from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Participante, Prova, LeituraGabarito 

def index(request):
    return render(request,'cadastro/cadastro.html')

# --- SUA NOVA VIEW DA API ---
@csrf_exempt
def upload_gabarito_view(request):
    # 1. Apenas aceitamos requisições do tipo POST
    if request.method != 'POST':
        return JsonResponse({'status': 'erro', 'message': 'Este endpoint suporta apenas POST'}, status=405)

    # 2. Pegamos os dados enviados na requisição
    image_file = request.FILES.get('gabarito_image')
    participante_id = request.POST.get('participante_id')
    prova_id = request.POST.get('prova_id')

    # 3. Validamos se todos os dados necessários foram enviados
    if not all([image_file, participante_id, prova_id]):
        return JsonResponse({'status': 'erro', 'message': 'Faltando parâmetros: image, participante_id ou prova_id'}, status=400)

    print(f"Requisição recebida para o participante {participante_id} e prova {prova_id}.")

    # 4. Tentamos executar a lógica principal
    try:
        participante = Participante.objects.get(id=participante_id)
        prova = Prova.objects.get(id=prova_id)
        
        return JsonResponse({
            'status': 'sucesso', 
            'message': f'Lógica para {participante.nome} e {prova.nome} a ser implementada.'
        })

    except Participante.DoesNotExist:
        return JsonResponse({'status': 'erro', 'message': f'Participante com id {participante_id} não encontrado.'}, status=404)
    except Prova.DoesNotExist:
        return JsonResponse({'status': 'erro', 'message': f'Prova com id {prova_id} não encontrada.'}, status=404)
    except Exception as e:
        return JsonResponse({'status': 'erro', 'message': f'Um erro inesperado ocorreu: {str(e)}'}, status=500)